# main.py
import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator, QLocale
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


def main():
    app = QApplication(sys.argv)

    base_path = get_base_path()
    system_lang = QLocale.system().name().split("_")[0]

    # Carica sempre l'inglese come base
    load_translator(app, "en", base_path)

    # Se il sistema non è inglese, prova a caricare la lingua locale
    if system_lang != "en":
        load_translator(app, system_lang, base_path)

    controller = MainController()
    controller.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()