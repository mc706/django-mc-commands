import ConfigParser
import os

_settings_folder, _ = os.environ.get("DJANGO_SETTINGS_MODULE", ".").split(".")

_defaults = {
    "changelog_directory": ".",
    "changelog_name": "CHANGELOG.md",
    "settings_folder": _settings_folder,
    "version_directory": "%(settings_folder)s",
    "version_file": "_version.py",
    "separate_internal_apps": False,
    "run_tests_before_cut": True,
    "check_pep8": True,
    "check_jshint": True,
    "check_prospector": True,
    "check_cyclomatic": True,
    "cyclomatic_average": "A",
    "cyclomatic_module": "A",
    "cyclomatic_block": "A",
    "check_quality_after_tests": True,
    "minimum_test_coverage": 100,
    "use_bower": True
}

def get_config(directory):
    tox_file = os.path.join(directory, 'tox.ini')
    rc_file = os.path.join(directory, '.mcrc')
    Config = ConfigParser.ConfigParser(_defaults)
    Config.read([tox_file, rc_file])
    return Config
