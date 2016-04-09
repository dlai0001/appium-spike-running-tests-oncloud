Proof of concept for CI mobile test builds on SauceLabs and Amazon Device Farm.

Notes:

1. Install python3
2. Install virtualenv
3. virtualenv .env --python3
4. pip install -r requirements.txt
5. pip install shovel  # Note Shovel inside requirements.txt will break ADF build process.

Saucelabs configure enviornment variables:
export RUN_TARGET=SAUCE
export TEST_NAME=name.your.build

export SAUCE_USER=joesomebody
export SAUCE_KEY=very-secret-key
