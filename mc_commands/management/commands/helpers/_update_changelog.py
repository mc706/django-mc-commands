import os
import git
from datetime import date

def update_change_log(config, version, new):
    directory = config.get("MCConfig", 'changelog_directory')
    changelog_name = config.get("MCConfig", 'changelog_name')
    change_file = os.path.join(directory, changelog_name)
    try:
        g = git.Git('./')
        log = g.log('%s..' % version, '--no-merges', '--pretty=format:%s').split('\n')
        today = date.today()
        with open(change_file, 'r') as old_changelog:
            old = old_changelog.read()
        minus_header = "\n".join(old.split('\n')[1:])
        with open(change_file, 'w') as new_changelog:
            new_changelog.write('#CHANGELOG\n\n')
            new_changelog.write('##Version %s (%s)\n\n' % (new, today))
            for line in log:
                new_changelog.write("* " + line + "\n")
            new_changelog.write('\n')
            new_changelog.write(minus_header)
    except Exception as ex:
        print ex