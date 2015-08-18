from setuptools import setup

import re
VERSIONFILE="mc_commands/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
    major, minor, patch = verstr.split('.')
    release = "%s.%s" %(major, minor)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))
# Setup
setup(
    name='django-mc-commands',
    version=verstr,
    url='https://github.com/mc706/django-mc-commands',
    author='Ryan McDevitt',
    author_email='mcdevitt.ryan@gmail.com',
    license='MIT License',
    packages=['mc_commands', 'mc_commands.management', 'mc_commands.management.commands', 'mc_commands.management.commands.helpers'],
    include_package_data=True,
    description='Additional Management Commands for Django',
    download_url = 'https://github.com/mc706/django-mc-commands/tarball/' + release,
    keywords = ['django', 'management', 'commands', 'mc706'],
    classifiers = [],
)