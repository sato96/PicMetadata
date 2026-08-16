# -*- mode: python ; coding: utf-8 -*-
# Build with: pyinstaller PicMetadata.spec

from PyInstaller.utils.hooks import collect_all

# 1. Raccoglie automaticamente TUTTE le DLL (inclusa icuuc.dll) e le dipendenze di PySide6
pyside_datas, pyside_binaries, pyside_hiddenimports = collect_all('PySide6')

a = Analysis(
    ['main.py'],
    pathex=[],
    # 2. Aggiunge i binari di PySide6 alla build
    binaries=[] + pyside_binaries,
    datas=[
        ('ui/MainWindow.ui',            'ui'),
        ('ui/manual_date_dialog.ui',    'ui'),
        ('ui/resources/style.qss',      'ui/resources'),
        ('ui/resources/style_dark.qss', 'ui/resources'),
        ('ui/resources/icons',          'ui/resources/icons'),
        ('translations/app_en.qm',      'translations'),
        ('translations/app_it.qm',      'translations'),
    ] + pyside_datas, # 3. Somma i dati aggiuntivi rilevati
    hiddenimports=[
        'PySide6.QtXml',
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'PySide6.QtPrintSupport',
        'PIL._tkinter_finder',
    ] + pyside_hiddenimports, # 4. Somma gli import nascosti rilevati
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PicMetadata',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,        # nessun terminale visibile
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlement_file=None,
    icon='ui/resources/icons/app_icon.ico',   # icona dell'eseguibile (Windows Explorer)
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PicMetadata',
)

# Bundle .app per macOS — ignorato su Windows/Linux
app = BUNDLE(
    coll,
    name='PicMetadata.app',
    bundle_identifier='com.sato96.picmetadata',
    icon='ui/resources/icons/app_icon.icns',  # icona del bundle .app (Finder/Dock)
    info_plist={
        'NSHighResolutionCapable': True,
        'LSBackgroundOnly': False,
        'CFBundleShortVersionString': '0.1.2',
        'CFBundleName': 'PicMetadata',
    },
)