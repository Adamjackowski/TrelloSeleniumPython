import inspect
import json
import os
import smtplib
import sys
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webbrowser import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")


@pytest.fixture(autouse=True, scope='session')
def declared_browser(pytestconfig):
    return pytestconfig.getoption("browser")


'''
Fixture method for init and deinit browser before and after all tests. It is called once a test session.
When test fails, the screenshot is beeing taken
'''
@pytest.fixture(scope='session')
def browsers(request, declared_browser):
    choosen_browser = declared_browser
    if choosen_browser == "Chrome":
        web_browser = webdriver.Chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = web_browser(options = chrome_options)
        driver.implicitly_wait(1)
    elif choosen_browser == "Firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        driver = Firefox(firefox_profile = profile)
        driver.implicitly_wait(1)
    elif choosen_browser == "Edge":
        capabilities = DesiredCapabilities.EDGE
        capabilities['ms:inPrivate'] = True
        driver = webdriver.Edge(capabilities=capabilities)
        driver.implicitly_wait(5)
    driver.maximize_window() 
    yield driver
    driver.quit()



'''
Method for taking the screenshot and saving in the /screenshots directory. It is called in browser fixture
'''
def take_screenshot(browsers, test_name):
    screenshots_dir = parentdir + '\screenshots'
    now = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    screenshot_file_path = '{}\{}_{}.png'.format(screenshots_dir, test_name, now)
    browsers.save_screenshot(screenshot_file_path)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True, scope='function')
def screenshot(browsers, request):
    failed_before = request.session.testsfailed
    yield None
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        take_screenshot(browsers, test_name)

@pytest.fixture()
def users():
    def _users(user):
        return user
    return _users
