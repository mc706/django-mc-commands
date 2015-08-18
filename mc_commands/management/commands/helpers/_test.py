from fabric.api import local
from mc_commands.management.commands.helpers._get_config import get_config
from mc_commands.management.commands.helpers._quality_check import quality_check


def test(directory):
    config = get_config(directory)
    #TODO: Get internal apps and import it
    app_list = " ".join(INTERNAL_APPS)
    local('coverage run manage.py test %s' % app_list)
    local('coverage report --fail-under=%s' % config.get("MCConfig", "minimum_test_coverage"))
    if config.get("MCConfig", "check_quality_fater_tests"):
        quality_check()
