import os, sys, inspect
import pytest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox import webdriver
from selenium.webdriver import Firefox
import json
from tests.test_base import TestBase
from pages.register_page import RegisterPage
from pages.objects.user import User
from pages.welcome_page import WelcomePage
from pages.login_page import LoginPage
from pages.boards_page import BoardsPage
from pages.after_logout_page import AfterLogoutPage

class TestLogin(TestBase):
  def test_login_success(self, browsers, users):
    # Init necesarry objects
    user = users(User())
    welcome_page = WelcomePage(browsers)
    login_page = LoginPage(browsers)
    boards_page = BoardsPage(browsers)
    after_logout_page = AfterLogoutPage(browsers)

    assert welcome_page.is_opened()
    assert welcome_page.login()
    assert login_page.is_opened()
    assert login_page.login(user)
    assert boards_page.is_opened()
    assert boards_page.logout()
    assert after_logout_page.is_opened()

    
def test_login_fail(browsers, users):
    # Init necesarry objects
    user = users(User("", ""))
    welcome_page = WelcomePage(browsers)
    login_page = LoginPage(browsers)
    boards_page = BoardsPage(browsers)
    after_logout_page = AfterLogoutPage(browsers)

    assert welcome_page.is_opened()
    assert welcome_page.login()
    assert login_page.is_opened()
    assert login_page.login(user)
    assert login_page.is_login_failed()
    assert welcome_page.open()