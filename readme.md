# Support for translations in NVDA and the add-on template

This repository is intended to be used as a submodule for [NVDA](https://github.com/nvaccess/nvda) and the [add-on template](https://github.com/nvaccess/addonTemplate).

## Installation and Building an Executable

To install all dependencies (including PyInstaller) and build a standalone executable using [uv](https://github.com/astral-sh/uv):

1. Install all dependencies:

	```sh
	uv pip install .
	```

2. Build the executable:

	```sh
	uv run pyinstaller --onefile source/l10nUtil.py
	```

The resulting executable will be located in the `dist` directory.

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
  - Optional: `localFilePath` — local path to save the file (defaults to `crowdinFilePath`); `-c`/`--config` — path to the configuration file; `-i`/`--id` — Crowdin project ID.

- `uploadTranslationFile` - Upload a translation file to Crowdin.
  - Required: `language` — language code to upload; `crowdinFilePath` — path of the file in Crowdin.
  - Optional: `localFilePath` — path to the local file to upload (defaults to `crowdinFilePath`); `-o`/`--old` — path to the old unchanged XLIFF file to upload only new or changed translations; `-c`/`--config` — path to the configuration file; `-i`/`--id` — Crowdin project ID.

- `uploadSourceFile` - Upload a source file to Crowdin.
  - Required: `localFilePath` — local path to the file to upload.
  - Optional: `-c`/`--config` — path to the configuration file; `-i`/`--id` — Crowdin project ID.

- `exportTranslations` - Export translation files from Crowdin as a bundle.
  - Required: `-o`/`--output` — directory to save the exported translation files.
  - Optional: `-l`/`--language` — language code to export (exports all languages if not specified); `-c`/`--config` — path to the configuration file; `-i`/`--id` — Crowdin project ID.

- `writeConfig` - Write the current Crowdin configuration (project ID and file list) to a YAML file.
  - Optional: `-c`/`--configFile` — path for the YAML configuration file to write (defaults to `l10nConfig.yaml`); `-i`/`--id` — Crowdin project ID.

## Recommended workflow

- If new files are added to Crowdin, store the file IDs and the project ID running the `writeConfig` command.
Example:

```sh
l10nUtil writeConfig - myConfigFile.yaml -i myProjectId`
```

- If new files haven't been added, run commands with the `-c` or `--config` flag, so that project ID and file IDs can be retrieved from the config file, and yo don't consume resources from your Crowdin API key.

Example:

```sh
l10nUtil exportTranslations -o myFolder -c myConfigFile.yaml
```


