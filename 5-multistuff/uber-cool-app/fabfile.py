# -*- coding: utf-8 -*-

import os

from fabric.api import env, task, roles, execute, sudo, put

env.user = 'vagrant'
env.key_filename = os.getenv('HOME') + '/.vagrant.d/insecure_private_key'

env.roledefs = {
    'front': ['192.168.45.10'],
    'back': ['192.168.45.20', '192.168.45.21']
}

@task
def deploy():
    execute(setup_nginx)
    execute(restart_node)

@roles('front')
def setup_nginx():
    put('deploy/uber-cool-app.nginx', '/etc/nginx/sites-enabled/default', use_sudo=True)
    sudo('/etc/init.d/nginx restart')

@roles('back')
def restart_node():
    sudo('cp /app/deploy/uber-cool-app.conf /etc/supervisor/conf.d')
    sudo('/etc/init.d/supervisor stop')
    sudo('/etc/init.d/supervisor start')
