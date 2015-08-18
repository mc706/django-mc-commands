from fabric.api import local
from mc_commands.management.commands.helpers._get_config import get_config


def quality_check(directory, release_type):
    config = get_config(directory)
    if config.get("MCConfig", "check_pep8"):
        local('pep8 .')
    if config.get("MCConfig", "check_jshint"):
        local('jshint assets')
    if config.get("MCConfig", "check_cyclomatic"):
        local('xenon . -a %s -m %s -b %s -i core' % (
            config.get('MCConfig', "cyclomatic_average"),
            config.get('MCConfig', "cyclomatic_module"),
            config.get('MCConfig', "cyclomatic_block"),
        ))
    if config.get("MCConfig", "check_prospector"):
        local('prospector')
