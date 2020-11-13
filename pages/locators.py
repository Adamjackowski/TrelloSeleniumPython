from selenium.webdriver.common.by import By

class WelcomePageLocators(object):
   LOGIN_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-sm.btn-link.text-white")

class LoginPageLocators(object):
   EMAIL_INPUT = (By.ID, "user")
   PASSWORD_INPUT = (By.ID, "password")
   LOGIN_BUTTON = (By.ID, "login")
   ERROR_MESSAGE = (By.CSS_SELECTOR, "p.error-message")
   LOGIN_BUTTON_ATTLASIAN = (By.ID, "login-submit")

class BoardsPageLocators(object):
   USER_ICON = (By.CSS_SELECTOR, '[data-test-id="header-member-menu-button"]')
   LOGOUT_BUTTON = (By.CSS_SELECTOR, '[data-test-id="header-member-menu-logout"]')

class AfterLogoutPageLocators(object):
   LOGIN_REGISTER_BUTTONS = (By.CSS_SELECTOR, "a.global-header-section-button.mod-primary")