from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QDateTime
from ui.ui_manual_date_dialog import Ui_ManualDateDialog
from enum import Enum


class DialogResult(Enum):
    CONFIRMED = "confirmed"
    SKIPPED = "skipped"
    ABORTED = "aborted"  # abort the whole loop


class ManualDateDialog(QDialog):
    def __init__(self, img_path: str, parent=None):
        super().__init__(parent)
        self.ui = Ui_ManualDateDialog()
        self.ui.setupUi(self)
        self.result_date = None
        self.dialog_result = DialogResult.ABORTED
        self._original_pixmap = None
        pixmap = QPixmap(img_path)
        if not pixmap.isNull():
            self._original_pixmap = pixmap
            self._fit_window_to_image(pixmap)
        self.ui.fileNameLabel.setText(img_path.split("/")[-1])
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.confirmButton.clicked.connect(self._on_confirm)
        self.ui.skipButton.clicked.connect(self._on_skip)
        self.ui.abortButton.clicked.connect(self._on_abort)

    def _fit_window_to_image(self, pixmap: QPixmap):
        """Resizes the window to fit the image, within reasonable limits."""
        screen = self.screen().availableGeometry() if self.screen() else None
        # Maximum 80% of the screen
        max_w = int(screen.width() * 0.8) if screen else 1200
        max_h = int(screen.height() * 0.8) if screen else 800
        # Space taken up by label + date + buttons (about 120px)
        ui_chrome_height = 120
        img_w = pixmap.width()
        img_h = pixmap.height()
        # Scale the image if it exceeds the limits
        if img_w > max_w or img_h > (max_h - ui_chrome_height):
            scaled = pixmap.scaled(
                max_w, max_h - ui_chrome_height,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        else:
            scaled = pixmap
        # Set the image
        self.ui.imagePreview.setPixmap(scaled)
        # Resize the window: width = image, height = image + chrome
        dialog_w = max(scaled.width() + 32, 300)   # 32px of margins
        dialog_h = scaled.height() + ui_chrome_height + 32
        self.resize(dialog_w, dialog_h)

    def resizeEvent(self, event):
        """Updates the preview if the user resizes the window manually."""
        super().resizeEvent(event)
        if self._original_pixmap is None:
            return
        size = self.ui.imagePreview.size()
        if size.width() > 0 and size.height() > 0:
            scaled = self._original_pixmap.scaled(
                size,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.ui.imagePreview.setPixmap(scaled)

    def _on_confirm(self):
        self.dialog_result = DialogResult.CONFIRMED
        self.result_date = self.ui.dateTimeEdit.dateTime().toString("yyyy:MM:dd HH:mm:ss")
        self.accept()

    def _on_skip(self):
        self.dialog_result = DialogResult.SKIPPED
        self.result_date = None
        self.accept()

    def _on_abort(self):
        self.dialog_result = DialogResult.ABORTED
        self.result_date = None
        self.reject()