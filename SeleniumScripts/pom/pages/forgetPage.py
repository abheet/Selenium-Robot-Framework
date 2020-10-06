from ..locators.locators import ForgetPasswordPageLocator, LoginPageLocators
from .util_methods import get_values, input_values
import config
from .signinPage import LoginPage


class ForgetPassword:
    
    """ Class contains Forget Page actions """
    def __init__(self, driver):
        self.driver = driver

    def is_forget_password_page_displayed(self):
        try:
            element = self.driver.find_element(
                *ForgetPasswordPageLocator.EMAIL_INPUT)
            config.LOGGER.info("Reset Password page displayed")
            return element.is_displayed()
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing is_forget_password_page_displayed :{}".format(err))

    def validation_message(self):
        error_div = self.driver.find_element(*LoginPageLocators.ERROR_DIV)
        if error_div:
            locator = LoginPageLocators.ERROR_MESSAGE
            error_message = get_values(self.driver, locator, 'innerHTML')
            return error_message

    def enter_email(self, email):
        try:
            self.driver.implicitly_wait(5)
            locator = ForgetPasswordPageLocator.EMAIL_INPUT
            input_values(self.driver, locator, email)
            config.LOGGER.info(
                "Email entered for reset password :{}".format(email))
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing enter_email :{}".format(err))

    def click_recover_password_button(self):
        try:
            element = self.driver.find_element(
                *ForgetPasswordPageLocator.RECOVER_PASSWORD_BUTTON)
            element.click()
            config.LOGGER.info("Recover password button clicked")
        except Exception as err:
            config.LOGGER.error(
                "Error encountered while executing click_recover_password_button :{}".format(err))

    def click_forget_password_link(self):
        
        element = self.driver.find_element(
            *LoginPageLocators.FORGET_PASSWORD_HREF)
        element.click()
