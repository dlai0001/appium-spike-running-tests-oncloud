Proof of concept for CI mobile test builds on SauceLabs and Amazon Device Farm.

Notes:

1. Install python3
2. Install virtualenv
3. virtualenv .env --python3
4. pip install -r requirements.txt
5. pip install shovel  # Note Shovel inside requirements.txt will break ADF build process.

#Sauce Labs


Saucelabs configure enviornment variables:
export RUN_TARGET=SAUCE
export TEST_NAME=name.your.build
export SAUCE_USER=joesomebody
export SAUCE_KEY=very-secret-key

Shell script for Jenkins to run after setting up a Python VirtualEnv

        set -e # immediate stop if error.

        echo "Installing Dependencies"
        pip install -r requirements.txt

        #echo "Publishing app to saucelabs"
        #shovel sauce.deploy

        echo "Running tests"
        shovel test.run


#Amazon Device Farm Setup

Install Amazon Device Farm Jenkins plugin and follow instructions -
 http://docs.aws.amazon.com/devicefarm/latest/developerguide/continuous-integration-jenkins-plugin.html

For the test option, select Python/Appium, then enter "test_bundle.zip"

Then add a build task. In the build task, add a shell script,

        pip install shovel
        shovel amazon.package # this will create a test_bundle.zip file for upload.

