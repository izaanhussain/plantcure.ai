# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_all, collect_data_files, collect_submodules, copy_metadata

base_path = os.path.abspath(os.getcwd())

datas = [
    ('model', 'model'),
    ('history', 'history'),
    ('reports', 'reports'),
    ('assets', 'assets'),
]
binaries = []
hiddenimports = []

packages_to_collect = [
    'gradio',
    'gradio_client',
    'safehttpx',
    'groovy',
    'fastapi',
    'starlette',
    'uvicorn',
    'pydantic',
    'httpx',
    'aiohttp',
    'jinja2',
    'markupsafe',
    'python_dateutil',
    'typing_extensions',
    'anyio',
    'h11',
    'werkzeug',
    'certifi',
    'pydantic_core',
    'typing_inspection',
]

for package_name in packages_to_collect:
    try:
        pkg_binaries, pkg_datas, pkg_hiddenimports = collect_all(package_name)
        binaries += pkg_binaries
        datas += pkg_datas
        hiddenimports += pkg_hiddenimports
    except Exception as exc:
        print(f'WARNING: collect_all({package_name}) failed: {exc}')

    try:
        datas += collect_data_files(package_name)
    except Exception:
        pass

    try:
        hiddenimports += collect_submodules(package_name)
    except Exception:
        pass

    try:
        datas += copy_metadata(package_name)
    except Exception:
        pass

seen = set()
unique_datas = []
for item in datas:
    if item not in seen:
        seen.add(item)
        unique_datas.append(item)
datas = unique_datas

hiddenimports = list(dict.fromkeys(hiddenimports))
binaries = list(dict.fromkeys(binaries))

a = Analysis(
    ['app.py'],
    pathex=[base_path],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PlantCure',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PlantCure',
)