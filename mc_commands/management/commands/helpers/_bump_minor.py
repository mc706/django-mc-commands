from fabric.api import local


from _update_changelog import update_change_log


def bump_minor(config):
    version_file = config.get('MCConfig', 'version_file')
    with open(version_file, 'r') as f:
        original = f.read()
        version = original.split('=')[1].strip('\" \n\'')
        major, minor, patch = version.split('.')
        patch = 0
        minor = int(minor) + 1
        new_version = '%s.%s.%s' % (major, minor, patch)
    update_change_log(config, version, new_version)
    with open(version_file, 'w') as f:
        f.write('__version__ = "%s.%s.%s"' % (major, minor, patch))
    local('git add %s' % version_file)
    local('git add CHANGELOG.md')
    local('git commit -m "updated version to %s.%s.%s"' % (major, minor, patch))
    local('git tag %s.%s.%s -m "Update for release"' % (major, minor, patch))
