from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.locators import LoginPageLocators, SignUpPageLocator, AuthPageLocator, InvitePersonPageLocator
from .util_methods import get_values, input_values, get_dummy_email, get_email_activation_link
import config
from .signinPage import LoginPage
import pytest


class SignupPage(LoginPage):

    def is_signup_form_displayed(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    SignUpPageLocator.SIGNUP_PAGE_SUBHEADER))
            config.LOGGER.info(
                "Actual Result: Signup form loaded and displayed successfully")
            return element.get_attribute('innerHTML')
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing is_login_form_displayed :{}".format(err))

    def click_signin_link(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    SignUpPageLocator.LOGIN_LINK))
            element.click()
            config.LOGGER.info(
                "Actual Result: Signin link clicked successfully")
            return self.driver.current_url
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing click_signin_link :{}".format(err))

    def enter_first_name(self, firstname):
        try:
            locator = SignUpPageLocator.FIRST_NAME_INPUT
            input_values(self.driver, locator, firstname)
            config.LOGGER.info(
                "Actual Result: First Name: {} entered successfully".format(firstname))
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing enter_first_name :{}".format(err))

    def enter_last_name(self, lastname):
        try:
            locator = SignUpPageLocator.LAST_NAME_INPUT
            input_values(self.driver, locator, lastname)
            config.LOGGER.info(
                "Actual Result: Last Name: {} entered successfully".format(lastname))
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing enter_last_name :{}".format(err))

    def enter_email(self, email):
        try:
            locator = SignUpPageLocator.EMAIL_INPUT
            input_values(self.driver, locator, email)
            config.LOGGER.info(
                "Actual Result: Email address: {} entered successfully".format(email))
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing enter_email :{}".format(err))

    def enter_signup_password(self, password):
        try:
            locator = SignUpPageLocator.PASSWORD_INPUT
            input_values(self.driver, locator, password)
            config.LOGGER.info(
                "Actual Result: Password: {} entered successfully".format(password))
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing enter_password :{}".format(err))

    def click_signup_button(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    SignUpPageLocator.SIGNUP_BUTTON))
            element.click()
            config.LOGGER.info("Signup form submitted successfully")
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing enter_password :{}".format(err))

    def get_error_message(self):
        error_div = self.driver.find_element(*LoginPageLocators.ERROR_DIV)
        if error_div:
            locator = LoginPageLocators.ERROR_MESSAGE
            error_message = get_values(self.driver, locator, 'innerHTML')
            config.LOGGER.info(
                "Error message {} displayed on screen".format(error_message))
            return error_message

    def is_auth_window(self):
        self.driver.implicitly_wait(10)
        locator = AuthPageLocator.AUTH_CONTAINER_DIV
        page_title = get_values(self.driver, locator, 'innerHTML')
        config.LOGGER.info(
            "Auth Screen Headear {} loaded successfully.".format(page_title))
        return page_title

    def invite_team_page_title(self):
        locator = InvitePersonPageLocator.INVITE_PAGE_TITLE
        page_title = get_values(self.driver, locator, 'innerHTML')
        config.LOGGER.info(
            "Invite Team Screen title {} loaded successfully.".format(page_title))
        return page_title

    def skip_invite_team_form(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(InvitePersonPageLocator.SKIP_BUTTON))
            element.click()
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while skipping invite team :{}".format(err))

    def email_confirmation_sent(self):
        try:
            locator = InvitePersonPageLocator.SIGNUP_CONFIRMATION_TITLE
            page_titles = get_values(self.driver, locator, 'innerHTML')
            return page_titles
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while signup confirmation:{}".format(err))
