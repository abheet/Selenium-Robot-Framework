from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.locators import LoginPageLocators, SignUpPageLocator, AuthPageLocator
from .util_methods import get_values, input_values, read_sms_otp
import config


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def is_login_form_displayed(self):
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(LoginPageLocators.LOGIN_SUBMIT_BUTTON))
            config.LOGGER.info("Login page displayed on page")
            return element.is_displayed()
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing is_login_form_displayed :{}".format(err))

    def signup_link_clickable(self):
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(LoginPageLocators.SIGNUP_HREF))
            element.click()
            config.LOGGER.info("SignUp link clicked from Login Page")
            return self.driver.current_url
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing click_signup_link :{}".format(err))

    def enter_username(self, username):
        try:
            locator = LoginPageLocators.USERNAME_INPUT
            input_values(self.driver, locator, username)
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing click_signup_link :{}".format(err))

    def enter_password(self, password):
        try:
            locator = LoginPageLocators.PASSWORD_INPUT
            input_values(self.driver, locator, password)
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing enter_password :{}".format(err))

    def click_signin_button(self):
        try:
            element = self.driver.find_element(
                *LoginPageLocators.LOGIN_SUBMIT_BUTTON)
            element.click()
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing click_signin_button :{}".format(err))

    def get_error_message(self):
        error_div = self.driver.find_element(*LoginPageLocators.ERROR_DIV)
        if error_div:
            locator = LoginPageLocators.ERROR_MESSAGE
            error_message = get_values(self.driver, locator, 'innerHTML')
            return error_message

    def is_auth_window(self):
        self.driver.implicitly_wait(10)
        self.locator = AuthPageLocator.AUTH_CONTAINER_DIV
        auth_heading = get_values(self.driver, self.locator, 'innerHTML')
        config.LOGGER.info(auth_heading)
        return auth_heading

    def check_remember_me(self):
        element = self.driver.find_element(
            *LoginPageLocators.REMEMBER_ME_CHECKBOX)
        element.click()

    def enter_otp(self):
        otp_value = read_sms_otp()
        locator = AuthPageLocator.OTP_INPUT
        input_values(self.driver, locator, otp_value)
        config.LOGGER.info("OTP entered is {}".format(otp_value))

    def submit_otp_button(self):
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(AuthPageLocator.OTP_SUBMIT_BUTTON))
            element.submit()
        except Exception as err:
            config.LOGGER.error("Element not found {}".format(err))

    def resend_otp(self):
        element = self.driver.find_element(*AuthPageLocator.RESEND_OTP_HREF)
        element.click()

    def cancel_otp(self):
        element = self.driver.find_element(*AuthPageLocator.CANCEL_HREF)
        element.click()

    def dashboard_content(self):
        try:
            locator = LoginPageLocators.DASHBOARD_CONTENT
            attribute_value = get_values(self.driver, locator, 'innerHTML')
            config.LOGGER.info("Dashboard_content :{}".format(attribute_value))
            return attribute_value
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing dashboard_content :{}".format(err))

    