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


class BoardsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    '''
    Method check is page open
    '''
    def is_opened(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            BoardsPageLocators.USER_ICON))
        return self.is_element_displayed(*BoardsPageLocators.USER_ICON)

    '''
    Method for logout
    '''
    def logout(self):      
        self.click(self.element(*BoardsPageLocators.USER_ICON))
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            BoardsPageLocators.LOGOUT_BUTTON))
        self.click(self.element(*BoardsPageLocators.LOGOUT_BUTTON))
        return True

 