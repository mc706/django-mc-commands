import os

from mc_commands.management.commands.helpers._bootstrap import bootstrap
from mc_commands.management.commands.helpers._get_config import get_config
from mc_commands.management.commands.helpers._bump_major import bump_major
from mc_commands.management.commands.helpers._bump_minor import bump_minor
from mc_commands.management.commands.helpers._bump_patch import bump_patch
from mc_commands.management.commands.helpers._test import test


def cut(directory, release_type):
    config = get_config(directory)
    # Create Version File
    version_file = os.path.join(config.get("MCConfig", "version_directory"), config.get("MCConfig", "version_file"))
    if config.get("MCConfig", "run_tests_before_cut"):
        test
    if not os.path.isfile(version_file):
        bootstrap(directory)
    if release_type is "patch":
        bump_patch(config)
    elif release_type is "minor":
        bump_minor(config)
    elif release_type is "major":
        bump_major(config)
    else:
        bump_patch(config)