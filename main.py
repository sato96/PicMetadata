# main.py
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator, QLocale
from controllers.main_controller import MainController


def load_translator(app: QApplication, lang_code: str) -> QTranslator | None:
    """Carica il file .qm per la lingua richiesta. Ritorna None se non trovato."""
    translator = QTranslator()
    if translator.load(f"translations/app_{lang_code}.qm"):
        app.installTranslator(translator)
        return translator
    return None


def main():
    app = QApplication(sys.argv)

    # Lingua del sistema operativo (es. "it", "fr", "de", "ja")
    system_lang = QLocale.system().name().split("_")[0]

    translator = None

    if system_lang != "en":
        # Prova a caricare la lingua del sistema
        translator = load_translator(app, system_lang)

        if translator is None:
            # Lingua non disponibile → carica inglese come default
            translator = load_translator(app, "en")
    # Se system_lang == "en" non carichiamo nulla:
    # il codice sorgente italiano viene sovrascritto dall'inglese? No —
    # vedi nota sotto su come gestire questo

    controller = MainController()
    controller.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()