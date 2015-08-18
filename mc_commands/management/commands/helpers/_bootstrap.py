import os

from mc_commands.management.commands.helpers._get_config import get_config
from mc_commands.management.commands.helpers._generate_docs import generate_docs

_version_number = '__version__ = "0.0.0"'

_installed_apps = 'INTERNAL_APPS = ()'

_change_log = '#CHANGELOG\n'


def bootstrap(directory):
    config = get_config(directory)
    # Create Version File
    version_file = os.path.join(config.get("MCConfig", "version_directory"), config.get("MCConfig", "version_file"))
    if not os.path.isfile(version_file):
        with open(version_file, 'w') as vf:
            vf.write(_version_number)
    if config.get("MCConfig", "separate_internal_apps"):
        internal_apps_file = os.path.join(config.get("MCConfig", "settings_folder"), "installed_apps.py")
        if not os.path.isfile(internal_apps_file):
            with open(internal_apps_file, 'w') as iaf:
                iaf.write(_installed_apps)
    change_file = os.path.join(config.get("MCConfig", 'changelog_directory'), config.get("MCConfig", 'changelog_name'))
    if not os.path.isfile(change_file):
        with open(change_file, 'w') as clf:
            clf.write(_change_log)
    if not os.path.isfile(os.path.join(directory, 'docs', 'mc_commands.md')):
        generate_docs(directory)
