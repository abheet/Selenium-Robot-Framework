import pytest
from ..pages.forgetPage import ForgetPassword
import config
from selenium import webdriver


@pytest.mark.usefixtures("browser")
class TestForgetPassword:
    
    @pytest.mark.lowest
    def test_forget_passsword_page_load(self):   
        """
        Test is to validate forget password the page 
        If Assert = True i.e. forget password page available and if its False then
        it mean forget password form is not available or not loaded
        """
        #If True Actual Result: forget password form exist and visible on screen
        self.reset_password = ForgetPassword(self.driver)
        self.driver.get("https://my.symphony.com/#forgot-password")
        assert self.reset_password.is_forget_password_page_displayed() == True
    
        
    @pytest.mark.medium    
    def test_blank_email_validation(self):
        """ Test is to check validations working when 
            invalid credentials used to login 
        """
        self.reset_password = ForgetPassword(self.driver)
        self.driver.get("https://my.symphony.com/#forgot-password")
        self.reset_password.enter_email("")
        self.reset_password.click_recover_password_button()
        error = self.reset_password.validation_message()
        """ Error messsages received when user input invalid email"""
        assert  error in config.RESET_PASSWORD_VALIDATION_MESSAGES
        
    @pytest.mark.medium    
    def test_captcha_validation(self):
        """ Test is to check captcha  working when 
            user not click on captcha checkbox and click on recover password button 
        """
        self.reset_password = ForgetPassword(self.driver)
        self.driver.get("https://my.symphony.com/#forgot-password")
        self.reset_password.enter_email("abheet.jamwal@gmail.com")
        self.reset_password.click_recover_password_button()
        error = self.reset_password.validation_message()
        """ Error messsages received when user input invalid messages"""
        assert  error in config.RESET_PASSWORD_VALIDATION_MESSAGES    
        
    