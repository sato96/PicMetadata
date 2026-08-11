# PicMetadata

A desktop tool to fix and manage EXIF date metadata in image files.

## Features

- **Automatic mode** — fixes dates on images whose filename contains a recognizable date pattern (WhatsApp, Windows Camera, standard IMG format)
- **Manual mode** — shows each image without a date and lets you set it manually
- **Hybrid mode** — runs automatic first, then prompts manually for unrecognized filenames
- **Single image mode** — select one or more images individually and set their date manually
- **Multi-language** — English (default), Italian. Follows system locale automatically.

## Screenshots

<!-- Add screenshots here -->

## Requirements

- Python 3.11+
- PySide6
- Pillow
- piexif

## Installation

### From source

```bash
git clone https://github.com/YOUR_USERNAME/PicMetadata.git
cd PicMetadata
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
python main.py
```

### Standalone executable (no Python required)
Download the latest release for your platform from the [Releases](https://github.com/sato96/PicMetadata/releases/latest) page:

| Platform | File |
|---|---|
| Windows | `PicMetadata-windows.zip` |
| macOS | `PicMetadata-macOS.dmg` |
| Linux | `PicMetadata-linux.tar.gz` |

Extract and run — no installation required.

## Build translations

```bash
# Extract strings from source
pyside6-lupdate ui/MainWindow.ui ui/manual_date_dialog.ui \
                main.py controllers/main_controller.py controllers/manual_date_dialog.py \
                -ts translations/app_en.ts translations/app_it.ts

# Compile
pyside6-lrelease translations/app_en.ts -qm translations/app_en.qm
pyside6-lrelease translations/app_it.ts -qm translations/app_it.qm
```

## Project structure

```
PicMetadata/
├── main.py                          # Entry point
├── controllers/
│   ├── main_controller.py           # Main window logic
│   └── manual_date_dialog.py        # Manual date dialog logic
├── services/
│   └── metaDataModifier.py          # Core EXIF logic
├── ui/
│   ├── MainWindow.ui                # Qt Designer — main window
│   ├── manual_date_dialog.ui        # Qt Designer — dialog
│   ├── ui_MainWindow.py             # Generated — do not edit
│   └── ui_manual_date_dialog.py     # Generated — do not edit
├── translations/
│   ├── app_en.ts                    # English strings (source)
│   └── app_it.ts                    # Italian strings
├── requirements.txt
└── pyproject.toml
```

## Versioning

This project follows [Semantic Versioning](https://semver.org/).

## License

MIT License — see [LICENSE](LICENSE) for details.