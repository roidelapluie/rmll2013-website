from fabric.api import *

import os
import shutil
import time
import glob
import hashlib
import yaml

def _install_extension():
    local('cd hydewiki && ../../bin/python setup.py install')
    #local('cd mobileplugin && ../../bin/python setup.py install')

def _hyde(args):
    _install_extension()
    return local('../bin/hyde %s' % args)

@task
def regen():
    local('rm -rf deploy')
    local('rm .hyde_deps')
    gen()

@task
def gen():
    _hyde('gen')

@task
def serve():
    gen()
    _hyde('serve')
