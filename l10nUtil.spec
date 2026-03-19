# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules

hiddenimports_pymdownx = collect_submodules('pymdownx')
hiddenimports_mdx_truly_sane_lists = collect_submodules('mdx_truly_sane_lists')
hiddenimports_mdx_gh_links = collect_submodules('mdx_gh_links')
hiddenimports_markdown_link_attr_modifier = collect_submodules('markdown_link_attr_modifier')

all_hiddenimports = (
	hiddenimports_pymdownx 
	+ hiddenimports_mdx_truly_sane_lists 
	+ hiddenimports_mdx_gh_links 
	+ hiddenimports_markdown_link_attr_modifier
)

a = Analysis(
	['source\\l10nUtil.py'],
	pathex=[],
	binaries=[('miscDeps/tools/msgfmt.exe', '.')],
	datas=[('data/addonTemplate.yaml', '.'), ('data/nvda.yaml', '.')],
	hiddenimports=all_hiddenimports,
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
	a.binaries,
	a.datas,
	[],
	name='l10nUtil',
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
)
