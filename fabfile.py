from fabric.api import local

def prepare_deploy():
    local("echo ------------------------")
    local("echo DEPLOYING APP TO PRODUCTION")
    local("git add . && git commit")
    local("git push -u origin master")
    local("echo APP PUSHED TO PRODUCTION")
    local("echo ------------------------")

def commit(msg):
    local("git add . && git commit -am %s" % msg)

def deploy():
    prepare_deploy()
    code_dir = "/home/captain/Code/django_apps/TimeLogger"
    with cd(code_dir):
        run("git pull")

def restart_service():
    run("sudo supervisorctl restart django_app")

