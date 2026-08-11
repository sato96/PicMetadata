# -*- mode: python ; coding: utf-8 -*-
# Build with: pyinstaller PicMetadata.spec

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ui/MainWindow.ui',            'ui'),
        ('ui/manual_date_dialog.ui',    'ui'),
        ('ui/resources/style.qss',      'ui/resources'),
        ('translations/app_en.qm',      'translations'),
        ('translations/app_it.qm',      'translations'),
    ],
    hiddenimports=[
        'PySide6.QtXml',
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'PySide6.QtPrintSupport',
        'PIL._tkinter_finder',
    ],
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
    entitlements_file=None,
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
    info_plist={
        'NSHighResolutionCapable': True,
        'LSBackgroundOnly': False,
        'CFBundleShortVersionString': '0.1.2',
        'CFBundleName': 'PicMetadata',
    },
)
