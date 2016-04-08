# noinspection PyUnresolvedReferences
from shovel import task
from subprocess import PIPE
import subprocess


@task
def run():
    command = ['py.test',
               'tests/',
               '--junitxml=results.xml']

    print(' '.join(command))
    result = subprocess.Popen(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(result.stdout.read(), result.stderr.read())
