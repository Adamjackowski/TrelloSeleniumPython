from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.locators import *
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By


class AfterLogoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    '''
    Method for logging out
    '''
    def is_opened(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            AfterLogoutPageLocators.LOGIN_REGISTER_BUTTONS))
        buttons = self.elements(*AfterLogoutPageLocators.LOGIN_REGISTER_BUTTONS)
        return len(buttons) > 0

 