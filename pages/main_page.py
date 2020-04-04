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


class WelcomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://trello.com")

    '''
    Method for logging out
    For some reason sometimes the alert window is displayed. Then we logout with this window
    '''

    def logout(self):
        
        self.close_all_dialogs()
        
        self.click(self.element(*MainPageLocators.USER_ICON))
        
        self.click(self.element(*MainPageLocators.LOGOUT_BTN))
        try:
            WebDriverWait(self.driver, 1).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            return self.element(*LoginPageLocators.LOGIN_BTN)
        except UnexpectedAlertPresentException:
            return False
        return self.element(*LoginPageLocators.LOGIN_BTN)

    '''
    Method for checking if the page is opened.
    Method waits for page loads
    '''

    def is_opened(self, page):
        WebDriverWait(self.driver, 1).until(EC.invisibility_of_element(
                (By.CSS_SELECTOR, "spinner-wrap.ng-scope.show-spinner")))
        if page == "ASSISTANCES":
            try:
                 WebDriverWait(self.driver, 1).until(
                    EC.visibility_of_element_located(AssistancesListLocatorsSP.CREATE_ASSISTANCE))
            except:
                return False
            return self.element(*AssistancesListLocatorsSP.CREATE_ASSISTANCE).is_displayed()
        if page == "SMARTBOARD":
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "img.photo-icon")))
            return self.element(*SmartBoardPageLocators.PLANNED_INTERVENTION_WIDGET).is_displayed()
        if page == "TECHNICIANS":
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(
                (By.XPATH, "//*[@translate='createTechnician']")))
            return self.element(*TechniciansListLocatorsCommon.CREATE_TECHNICIAN).is_displayed()
        if page == "USERS":
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(
                (By.XPATH, "//*[@translate='createUser']")))
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(UsersListLocatorsCommon.CREATE_USER))
            return self.element(*UsersListLocatorsCommon.CREATE_USER).is_displayed() 

    '''
    Method for opening the page.
    For some reason the exception can be called, so there is a try block to handle it
    '''

    def open(self, page):
        if page == "ASSISTANCES":
            try:
                self.click(self.element(*MainPageLocators.ASSISTANCES))
            except:
                WebDriverWait(self.driver, 1).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, "modal fade ng-isolate-scope ng-animate ng-leave ng-leave-active")))
                self.click(self.element(*MainPageLocators.SMART_MANAGER))
                self.click(self.element(*MainPageLocators.ASSISTANCES))
        if page == "SMARTBOARD":
            try:
                self.click(self.element(*MainPageLocators.SMART_BOARD))
            except:
                WebDriverWait(self.driver, 1).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, "modal fade ng-isolate-scope ng-animate ng-leave ng-leave-active")))
                self.click(self.element(*MainPageLocators.SMART_PARTNER))
                self.click(self.element(*MainPageLocators.SMART_BOARD))
        if page == "TECHNICIANS":
            try:
                self.click(self.element(*MainPageLocators.TECHNICIANS))
            except:
                WebDriverWait(self.driver, 1).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, "modal fade ng-isolate-scope ng-animate ng-leave ng-leave-active")))
                self.click(self.element(*MainPageLocators.SMART_MANAGER))
                self.click(self.element(*MainPageLocators.TECHNICIANS))
        if page == "USERS":
            try:
                self.click(self.element(*MainPageLocators.USERS))
            except:
                WebDriverWait(self.driver, 1).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, "modal fade ng-isolate-scope ng-animate ng-leave ng-leave-active")))
                self.click(self.element(*MainPageLocators.SMART_MANAGER))
                self.click(self.element(*MainPageLocators.USERS))
        return self.is_opened(page)
    '''
    Method for refreshing the page.
    '''

    def refresh(self):
        self.driver.refresh()
        return True
