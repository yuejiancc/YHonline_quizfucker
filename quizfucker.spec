# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['quizfucker.py'],
    pathex=[],
    binaries=[],
    datas=[('%替换成你的python安装目录%\\Lib\\site-packages\\onnxruntime\\capi\\onnxruntime_providers_shared.dll','onnxruntime\\capi'),('%替换成你的python安装目录%\\AppData\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\ddddocr\\common_old.onnx','ddddocr'),('%替换成你的python安装目录%\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\ddddocr\\common.onnx','ddddocr')],
    hiddenimports=[],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='quizfucker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\yueji\\Desktop\\Working_dir\\YHonline_quizfucker\\quizfucker.ico'],
)
