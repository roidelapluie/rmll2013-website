from fabric.api import local, run, env, task

env.use_ssh_config = True
env.hosts = ['rmll4']

def _hyde(args):
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

@task
def publish():
    local('rsync deploy/ -racv --delete rmll4:WEBSITE')
    run('rsync WEBSITE/ -rcv --delete /var/www')
    run('cd /var/www/assets && wget --progress=dot -ci assets-list')
