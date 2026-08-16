# main.py
import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator, QLocale, Qt
from PySide6.QtGui import QIcon
from controllers.main_controller import MainController


def get_base_path() -> str:
    """
    Restituisce il path base delle risorse.
    - Se siamo dentro PyInstaller → usa _MEIPASS (cartella temporanea del bundle)
    - Se siamo in sviluppo → usa la directory del progetto
    """
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS          # path dentro il bundle PyInstaller
    return os.path.dirname(os.path.abspath(__file__))  # path sviluppo


def load_translator(app: QApplication, lang_code: str, base_path: str) -> QTranslator | None:
    translator = QTranslator()
    qm_path = os.path.join(base_path, "translations", f"app_{lang_code}.qm")
    if translator.load(qm_path):
        app.installTranslator(translator)
        return translator
    return None


def is_system_dark(app: QApplication) -> bool:
    """
    Rileva se il sistema operativo sta usando un tema scuro.
    Usa l'API nativa di Qt (QStyleHints.colorScheme), disponibile da
    Qt 6.5+ e funzionante su Windows, macOS e Linux (via XDG desktop
    portal su GNOME/KDE). Se Qt non riesce a determinarlo (Unknown),
    di default resta sul tema chiaro.
    """
    scheme = app.styleHints().colorScheme()
    return scheme == Qt.ColorScheme.Dark


def load_stylesheet(app: QApplication, base_path: str) -> None:
    """Applies the app-wide modern QSS theme (light or dark) based on the OS setting."""
    filename = "style_dark.qss" if is_system_dark(app) else "style.qss"
    qss_path = os.path.join(base_path, "ui", "resources", filename)
    try:
        with open(qss_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except OSError:
        pass


def load_app_icon(app: QApplication, base_path: str) -> None:
    """
    Imposta l'icona della finestra/app a runtime (taskbar su Windows,
    Dock su macOS, taskbar/launcher su Linux). Un solo PNG funziona
    identicamente su tutti e tre gli OS: è l'icona dell'.exe/.app a
    richiedere formati separati (.ico/.icns), impostata invece in
    PicMetadata.spec al momento della build.
    """
    icon_path = os.path.join(base_path, "ui", "resources", "icons", "app_icon.png")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))


def main():
    app = QApplication(sys.argv)
    base_path = get_base_path()
    load_stylesheet(app, base_path)
    load_app_icon(app, base_path)

    # Riapplica il tema corretto se l'utente cambia chiaro/scuro
    # a livello di OS mentre l'app è già aperta.
    app.styleHints().colorSchemeChanged.connect(
        lambda _scheme: load_stylesheet(app, base_path)
    )

    system_lang = QLocale.system().name().split("_")[0]

    # Tieni i riferimenti in una lista per evitare il garbage collector
    translators = []

    en_translator = load_translator(app, "en", base_path)
    if en_translator:
        translators.append(en_translator)

    if system_lang != "en":
        lang_translator = load_translator(app, system_lang, base_path)
        if lang_translator:
            translators.append(lang_translator)

    controller = MainController()
    controller.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()