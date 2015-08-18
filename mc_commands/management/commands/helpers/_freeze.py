import os
from fabric.api import local

def freeze():
    local("pip freeze > requirements.txt")
