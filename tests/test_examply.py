import pytest
from selenium import webdriver
import os

# Fixtures are a way to setup data dependencies in automated tests.
@pytest.fixture(scope="function")
def driver(request):
    desired_caps = {}
    wd = None

    if os.environ['RUN_TARGET'] == "SAUCE":
        # sauce labs.
        desired_caps['browserName'] = ""
        desired_caps['appiumVersion'] = "1.4.16"
        #desired_caps['deviceName'] = "iPhone 5"
        desired_caps['deviceName'] = "iPhone Simulator"
        desired_caps['deviceOrientation'] = "portrait"
        desired_caps['platformVersion'] = "9.2"
        desired_caps['platformName'] = "iOS"
        desired_caps['app'] = "sauce-storage:TapIt.zip"
        desired_caps['name'] = os.environ['TEST_NAME']
        # saucelabs connection string.
        sauce_user = os.environ['SAUCE_USER']
        sauce_key = os.environ['SAUCE_KEY']
        wd = webdriver.Remote("http://{sauce_user}:{sauce_key}@ondemand.saucelabs.com:80/wd/hub".format(
            sauce_user=sauce_user,
            sauce_key=sauce_key),
            desired_caps)

    elif os.environ['RUN_TARGET'] == "AMAZON_DEVICE_FARM" or os.getenv('SCREENSHOT_PATH') is not None :
        # Using a hack that SCREENSHOT_PATH is provided by Amazon Device Farm.
        # We have to do this because when running with the ADF Jenkins Plugin, we do not have the
        # opportunity to set the enviornment variables.
        wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    else:
        # Localhost appium
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.2'
        desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['app'] = os.path.abspath('staging/TapIt.app')
        # local host
        wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)



    wd.implicitly_wait(300)

    # A finalizer is added if there needs to be a teardown to undo the effects of the automated test.
    def fin():
        wd.quit()

    request.addfinalizer(fin)
    return wd # Returns a fixture that contains the test data we need for the test.

# Test classes start with the word "Test".  It should be named Test + Feature you are testing.
class TestExample:

    # Test methods start with the word "test", name this using the pattern,
    # "test_ + (what you are testing) + "_" + (what is the expected result)
    # The parameters for a test are fixtures needed.  Use the fixture's return to feed data into
    # a test.
    def test_example_works(self, driver):

        driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()

        score = driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAStaticText[2]").text
        assert "1" in score

