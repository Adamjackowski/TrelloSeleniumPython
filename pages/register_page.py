from pages.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_opened(self):
        WebDriverWait(self.driver, 3).until(
        EC.visibility_of_element_located(RegisterPageLocators.NEXT_BUTTON_CLEAR))
        return self.check_content()
    
    def check_content(self):
        assert self.is_element_displayed(*RegisterPageLocators.EMAIL_INPUT)
        assert self.is_element_displayed(*RegisterPageLocators.PASSWORD_INPUT)
        assert self.is_element_displayed(*RegisterPageLocators.PASSWORD_REPEAT_INPUT)
        assert self.is_element_displayed(*RegisterPageLocators.NEXT_BUTTON_CLEAR)
        assert self.is_element_displayed(*RegisterPageLocators.FACEBOOK_BUTTON)
        assert self.is_element_displayed(*RegisterPageLocators.LOGIN_BUTTON)
        return True
        
    '''
    Method redirects to register page
    '''
    def fill_fields(self, user):
       self.type(self.element(*RegisterPageLocators.EMAIL_INPUT), user._email)
       self.type(self.element(*RegisterPageLocators.PASSWORD_INPUT), user._password)
       self.type(self.element(*RegisterPageLocators.PASSWORD_REPEAT_INPUT), user._password)
       return self.are_fields_filled_in(user)
    
    def are_fields_filled_in(self, user):
        assert self.check_input_value(self.element(*RegisterPageLocators.EMAIL_INPUT), user._email)
        assert self.check_input_value(self.element(*RegisterPageLocators.PASSWORD_INPUT), user._password)
        assert self.check_input_value(self.element(*RegisterPageLocators.PASSWORD_REPEAT_INPUT), user._password)

    def register(self, user):
        self.fill_fields(user)
        self.are_fields_filled_in(user)
        self.click(self.element(*RegisterPageLocators.NEXT_BUTTON_FILLED_IN))
        return True
