#!/usr/bin/env python3

from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
VSCODE_CONFIG_DIR = Path.home() / '.config/Code/User'

VSCODE_CONFIG_FILENAMES = ['keybindings.json', 'settings.json']


def main():
    for filename in VSCODE_CONFIG_FILENAMES:
        PROJECT_FILE = PROJECT_DIR / filename
        VSCODE_FILE = VSCODE_CONFIG_DIR / filename

        if not VSCODE_FILE.is_symlink or VSCODE_FILE.resolve() != PROJECT_FILE:
            make_backup(VSCODE_FILE)
            print(f'Create symlink "{VSCODE_FILE}" -> "{PROJECT_FILE}".')
            VSCODE_FILE.symlink_to(PROJECT_FILE)
        else:
            print(f'The Visual Studio Code file "{VSCODE_FILE}" is already pointing to "{PROJECT_FILE}".')


def make_backup(file):
    backup_file = file.parent / (file.name + '.bak')
    print(f'Create backup file "{file}" -> "{backup_file}".')
    file.rename(backup_file)


if __name__ == "__main__":
    main()
