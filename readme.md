# Support for translations in NVDA and the add-on template

This repository is intended to support translations for [NVDA](https://github.com/nvaccess/nvda) and add-ons using the [add-on template](https://github.com/nvaccess/addonTemplate).

## Available Commands

- `checkPo` - Check one or more PO files for errors.
  - Required: `poFilePaths` — one or more paths to the PO files to check.

- `xliff2md` - Convert an XLIFF file to a Markdown file.
  - Required: `xliffPath` — path to the source XLIFF file; `mdPath` — path for the resulting Markdown file.
  - Optional: `-u`/`--untranslated` — produce the untranslated version of the Markdown file.

- `md2html` - Convert a Markdown file to HTML.
  - Required: `mdPath` — path to the Markdown file; `htmlPath` — path for the resulting HTML file.
  - Optional: `-l`/`--lang` — language code (default: `en`); `-t`/`--docType` — document type, one of `userGuide`, `developerGuide`, `changes`, `keyCommands`.

- `xliff2html` - Convert an XLIFF file directly to HTML (combines `xliff2md` and `md2html`).
  - Required: `xliffPath` — path to the source XLIFF file; `htmlPath` — path for the resulting HTML file.
  - Optional: `-l`/`--lang` — language code (auto-detected from the XLIFF file if not provided); `-t`/`--docType` — document type, one of `userGuide`, `developerGuide`, `changes`, `keyCommands`; `-u`/`--untranslated` — produce the untranslated version.

- `downloadTranslationFile` - Download a translation file from Crowdin.
  - Required: `language` — language code to download; `crowdinFilePath` — path of the file in Crowdin.
  - Optional: `localFilePath` — local path to save the file (defaults to `crowdinFilePath`); `-c`/`--config` — path to the configuration file.

- `uploadTranslationFile` - Upload a translation file to Crowdin.
  - Required: `language` — language code to upload; `crowdinFilePath` — path of the file in Crowdin.
  - Optional: `localFilePath` — path to the local file to upload (defaults to `crowdinFilePath`); `-o`/`--old` — path to the old unchanged XLIFF file to upload only new or changed translations; `-c`/`--config` — path to the configuration file.

- `uploadSourceFile` - Upload a source file to Crowdin.
  - Required: `localFilePath` — local path to the file to upload.
  - Optional: `-c`/`--config` — path to the configuration file.

- `exportTranslations` - Export translation files from Crowdin as a bundle.
  - Required: `-o`/`--output` — directory to save the exported translation files.
  - Optional: `-l`/`--language` — language code to export (exports all languages if not specified); `-c`/`--config` — path to the configuration file.

- `writeConfig` - Write the current Crowdin configuration (project ID and file list) to a YAML file.
  - Optional: `-c`/`--configFile` — path for the YAML configuration file to write (defaults to `l10nConfig.yaml`); `-i`/`--id` — Crowdin project ID.

## Installation and Building an Executable

To install all dependencies (including PyInstaller) and build a standalone executable using [uv](https://github.com/astral-sh/uv):

1. Install all dependencies:

	```sh
	uv sync
	```

2. Build the executable:

	```sh
	uv run pyinstaller l10nUtil.spec
	```

The resulting executable will be located in the `dist` directory.
