# noinspection PyUnresolvedReferences
from shovel import task
from subprocess import PIPE
import subprocess
import os

@task
def deploy():
    #command to push file to sauce storage
    command = ['curl',
               '-u',
               "{sauce_user}:{sauce_key}".format(sauce_user=os.environ['SAUCE_USER'],sauce_key=os.environ['SAUCE_KEY']), #auth info
               '-X',
               'POST',
               '-H',
               '"Content-Type: application/octet-stream"',
               "https://saucelabs.com/rest/v1/storage/{user}/TapIt.zip?overwrite=true".format(user=os.environ['SAUCE_USER']), #sauce storage location
               '--data-binary',
               'staging/TapIt.app.zip'] # file to upload location
    print(' '.join(command))
    result = subprocess.Popen(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(result.stdout.read(), result.stderr.read())

