# -*- mode: python ; coding: utf-8 -*-
# Build with: pyinstaller PicMetadata.spec

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ui/MainWindow.ui',            'ui'),
        ('ui/manual_date_dialog.ui',    'ui'),
        ('translations/app_en.qm',      'translations'),
        ('translations/app_it.qm',      'translations'),
    ],
    hiddenimports=[
        'PySide6.QtXml',   # richiesto da Qt internamente
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

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
