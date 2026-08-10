# controllers/main_controller.py

import threading
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTimer, QThread, Signal, QObject
from ui.ui_MainWindow import Ui_MainWindow
from controllers.manual_date_dialog import ManualDateDialog, DialogResult
from services.metaDataModifier import metaDataModifier


class AnalysisWorker(QObject):
    progress = Signal(dict)
    finished = Signal(dict)
    manual_input_required = Signal(str)

    def __init__(self, service, mode):
        super().__init__()
        self.service = service
        self.mode = mode
        self._event = threading.Event()
        self._manual_result = None
        self._aborted = False  # ← abort flag

    def abort(self):
        self._aborted = True

    def _request_manual_date(self, img_path: str):
        if self._aborted:
            return None
        self._event.clear()
        self._manual_result = None
        self.manual_input_required.emit(img_path)
        self._event.wait()
        return None if self._aborted else self._manual_result

    def set_manual_result(self, date, aborted=False):
        if aborted:
            self._aborted = True
        self._manual_result = date
        self._event.set()

    def run(self):
        result = self.service.folder_analysis(
            mode=self.mode,
            callback=self._on_progress,
            manual_request=self._request_manual_date
        )
        self.finished.emit(result)

    def _on_progress(self, status):
        if self._aborted:
            return
        self.progress.emit(status)


class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.cartella_corrente = None
        self.metaDataModifier = None
        self._thread = None
        self._worker = None

        self._connect_signals()
        QTimer.singleShot(0, self.seleziona_cartella)

    def _connect_signals(self):
        self.ui.changeFolderButton.clicked.connect(self.seleziona_cartella)
        self.ui.updateDataButton.clicked.connect(self.aggiorna_analisi)
        self.ui.autoButton.clicked.connect(self.avvia_modalita_automatica)
        self.ui.manualButton.clicked.connect(self.avvia_modalita_manuale)
        self.ui.singleImgButton.clicked.connect(self.avvia_singola_immagine)
        self.ui.hybridModeButton.clicked.connect(self.avvia_modalita_ibrida)
        self.ui.actionCrediti.triggered.connect(self.credits)
        self.ui.actionGuida.triggered.connect(self.guide)

    def guide(self):
        from PySide6.QtGui import QDesktopServices
        from PySide6.QtCore import QUrl
        QDesktopServices.openUrl(QUrl("https://github.com/sato96/PicMetadata"))

    def credits(self):
        from PySide6.QtGui import QDesktopServices
        from PySide6.QtCore import QUrl
        QDesktopServices.openUrl(QUrl("https://github.com/sato96"))

    # ── Folder ──────────────────────────────────────────────────────────────
    def seleziona_cartella(self):
        cartella = QFileDialog.getExistingDirectory(
            self, self.tr("Select a folder"),
            self.cartella_corrente or "",
            QFileDialog.Option.ShowDirsOnly
        )
        if cartella:
            self.cartella_corrente = cartella
            self.ui.folderPathName.setText(cartella)
            if self.metaDataModifier is None:
                self.metaDataModifier = metaDataModifier(self.cartella_corrente)
            else:
                self.metaDataModifier.folder = self.cartella_corrente
            self._avvia_analisi("analysis")
        elif self.cartella_corrente is None:
            risposta = QMessageBox.question(
                self, self.tr("No folder"),
                self.tr("No folder selected. Do you want to quit?"),
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if risposta == QMessageBox.StandardButton.Yes:
                self.close()

    def aggiorna_analisi(self):
        if not self.cartella_corrente or self.metaDataModifier is None:
            QMessageBox.warning(self, self.tr("Warning"), self.tr("Please select a folder first."))
            return
        self._avvia_analisi("analysis")

    # ── Thread ────────────────────────────────────────────────────────────────
    def _avvia_analisi(self, mode: str):
        if self._thread is not None and self._thread.isRunning():
            return

        self._thread = QThread()
        self._worker = AnalysisWorker(self.metaDataModifier, mode)
        self._worker.moveToThread(self._thread)

        self._thread.started.connect(self._worker.run)
        self._worker.progress.connect(self._on_progress)
        self._worker.finished.connect(self._on_finished)
        self._worker.manual_input_required.connect(self._show_manual_dialog)

        self._worker.finished.connect(self._thread.quit)
        self._worker.finished.connect(self._worker.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        self._thread.finished.connect(self._on_thread_cleanup)

        self._set_ui_loading(True)
        self._thread.start()

    def _on_thread_cleanup(self):
        self._thread = None
        self._worker = None

    # ── Manual popup ─────────────────────────────────────────────────────────
    def _show_manual_dialog(self, img_path: str):
        """
        Called on the UI thread when the worker needs manual input.
        Opens the dialog, then releases the worker with the result.
        """
        dialog = ManualDateDialog(img_path, parent=self)
        dialog.exec()

        if dialog.dialog_result == DialogResult.ABORTED:
            # Stop everything: halt the worker
            self._worker.abort()
            self._worker.set_manual_result(None, aborted=True)
        else:
            self._worker.set_manual_result(dialog.result_date)

    # ── Progress / finished slots ────────────────────────────────────ManualDateDialog───────────
    def _on_progress(self, status: dict):
        analisi = status["analysis"]
        perc = int(analisi["current_percentage"])
        img = status["current_data"]["current_image"].split("/")[-1]
        self.statusBar().showMessage(f"{perc}% — {img}")
        self._popola_tabella(analisi)

    def _on_finished(self, status: dict):
        self._set_ui_loading(False)
        self._popola_tabella(status["analysis"])
        self.statusBar().showMessage("Analysis completed.", 3000)

    def _set_ui_loading(self, loading: bool):
        for btn in [self.ui.updateDataButton, self.ui.changeFolderButton,
                    self.ui.autoButton, self.ui.manualButton,
                    self.ui.singleImgButton, self.ui.hybridModeButton]:
            btn.setEnabled(not loading)

    def _show_summary_dialog(self, title: str, fixed: int, skipped: int):
        """Summary dialog with a guaranteed minimum width."""
        from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
        from PySide6.QtCore import Qt

        dialog = QDialog(self)
        dialog.setWindowTitle(title)
        dialog.setMinimumWidth(400)

        layout = QVBoxLayout(dialog)
        layout.setSpacing(12)
        layout.setContentsMargins(24, 24, 24, 24)

        # Text
        imgModLabel = self.tr("Images modified: ")
        imgFix = f"<b>{fixed}</b><br>"
        imgSkipLabel = self.tr("Skipped: ")
        imgSkip = f"<b>{skipped}</b><br>"
        label = imgModLabel + imgFix + imgSkipLabel + imgSkip
        msg = QLabel(label)
        msg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        msg.setTextFormat(Qt.TextFormat.RichText)
        layout.addWidget(msg)

        # OK button
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        ok_btn = QPushButton(self.tr("OK"))
        ok_btn.setDefault(True)
        ok_btn.clicked.connect(dialog.accept)
        btn_layout.addWidget(ok_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        dialog.exec()

    # ── Table ───────────────────────────────────────────────────────────────
    def _popola_tabella(self, analisi: dict):
        tabella = self.ui.statusTable

        labelsHeader = [
            self.tr("Number of images"),
            self.tr("Images without a date"),
            self.tr("Fixed automatically"),
            self.tr("Fixed manually"),
            self.tr("Skipped")
        ]
        rows = [
            str(analisi["nrImages"]),
            str(analisi["img_no_data"]),
            str(analisi["images_fixed"]),
            str(analisi["images_manual_fix"]),
            str(analisi.get("images_skipped", 0))
        ]

        tabella.setRowCount(len(labelsHeader))
        tabella.setColumnCount(1)
        tabella.setHorizontalHeaderLabels([self.tr("Value")])
        tabella.setVerticalHeaderLabels(labelsHeader)

        for i, valore in enumerate(rows):
            tabella.setItem(i, 0, QTableWidgetItem(valore))


    # ── Modes ──────────────────────────────────────────────────────────────
    def avvia_modalita_automatica(self):
        self._avvia_analisi("auto")

    def avvia_modalita_manuale(self):
        self._avvia_analisi("manual")


    def avvia_singola_immagine(self):
        if not self.cartella_corrente or self.metaDataModifier is None:
            QMessageBox.warning(self, self.tr("Warning"), self.tr("Please select a folder first."))
            return

        # 1. Select N images (starts from the current folder)
        files, _ = QFileDialog.getOpenFileNames(
            self,
            self.tr("Select images"),
            self.cartella_corrente,
            "Images (*.jpg *.jpeg *.bmp *.png *.gif)"
        )

        if not files:
            return

        # 2. Process each image with the manual dialog
        skipped = 0
        fixed = 0
        aborted = False

        for img_path in files:
            dialog = ManualDateDialog(img_path, parent=self)
            dialog.exec()

            if dialog.dialog_result == DialogResult.ABORTED:
                aborted = True
                break
            elif dialog.dialog_result == DialogResult.SKIPPED:
                skipped += 1
            elif dialog.dialog_result == DialogResult.CONFIRMED:
                try:
                    self.metaDataModifier.change_date(img_path, dialog.result_date)
                    fixed += 1
                except Exception as e:
                    QMessageBox.warning(
                        self,
                        self.tr("Save error"),
                        self.tr(f"Unable to save the date for:\n{img_path}\n\n{e}")
                    )

        # 3. Summary message
        if not aborted:
            self._show_summary_dialog(self.tr("Completed"), fixed, skipped)
        else:
            self._show_summary_dialog(self.tr("Aborted"), fixed, skipped)

        # 4. Re-run the analysis
        self._avvia_analisi("analysis")

    def avvia_modalita_ibrida(self):
        self._avvia_analisi("full")