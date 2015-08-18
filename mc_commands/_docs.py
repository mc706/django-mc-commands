docs = """django-mc-commands
=======================

[![Build Status](https://travis-ci.org/mc706/django-angular-scaffold.svg?branch=master)](https://travis-ci.org/mc706/django-angular-scaffold)
[![PyPI version](https://badge.fury.io/py/django-angular-scaffold.svg)](http://badge.fury.io/py/django-angular-scaffold)
[![Code Health](https://landscape.io/github/mc706/django-angular-scaffold/master/landscape.svg)](https://landscape.io/github/mc706/django-angular-scaffold/master)
[![Coverage Status](https://img.shields.io/coveralls/mc706/django-angular-scaffold.svg)](https://coveralls.io/r/mc706/django-angular-scaffold)

set of django management commands to manage versions and help out around building your app.

build by [@mc706](http://mc706.com)

##Installation

Install using pip

```
pip install django-mc-commands
```

include in your INSTALLED_APPS
```
#settings.py
...
INSTALLED_APPS = (
    ...
    'mc_commands',
    ...
)
```

##Commands

The following are commands that are made available through this package.


###bootstrap

```
./manage.py bootstrap
```

Adds a few key files to your application

* `_version.py`
* `CHANGELOG.md`
* This docs file
* A separate internal app tuple file



###quality_check

```
./manage.py quality_check
```

Runs a few libraries to check the quality of the code in the repository

* pep8
* jshint
* xenon
* prospector

###runtests

```
./manage.py runtests
```

A shortcut command to run the internal apps with coverage and fail if coverage is below a certain amount

###freeze

```
./manage.py freeze
```

Shortcut wrapper around `pip freeze > requirements.txt`


###cut

```
./manage.py cut <type>
```

Cuts a release and pushed it to git. Will update the changelog, and update `_version.py` and tag a release.

Type options are:

* patch (default)
* minor
* major

Version users Semver major.minor.patch

"""