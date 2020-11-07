from selenium import webdriver
import pytest
from ..pages.signinPage import LoginPage
import config

@pytest.mark.usefixtures("browser")
class TestSignIn:
    
    @pytest.mark.lowest
    def test_signin_form_exist(self):
        """
        Test is to validate signin existence on the page 
        If Assert = True i.e. Login page available and if its False then
        it mean login form is not available or not loaded
        """
        self.login = LoginPage(self.driver)
        self.driver.get('https://my.symphony.com/')
        # If True Actual Result: Login form exist and visible on screen
        assert self.login.is_login_form_displayed() == True


    @pytest.mark.lowest
    def test_signup_link_clickable(self):
        """ Test is to validate signup link is working"""
        self.login = LoginPage(self.driver)
        self.driver.get('https://my.symphony.com/')
        current_url = self.login.signup_link_clickable()
        assert current_url == 'https://my.symphony.com/#signup'


    @pytest.mark.medium
    def test_invalid_login_credentials(self):
        """ Test is to check validations working when 
            invalid credentials used to login 
        """
        self.login = LoginPage(self.driver)
        self.driver.get('https://my.symphony.com/')
        self.login.enter_username("abheet")
        self.login.enter_password("abheet")
        self.login.click_signin_button()
        error = self.login.get_error_message()
        """ Error messsages received when user input invalid messages"""
        assert error in config.LOGIN_VALIDATION_MESSAGES


    @pytest.mark.highest
    def test_sign_in(self):
        """ Test Login flow with valid flow"""
        self.login = LoginPage(self.driver)
        self.driver.get('https://my.symphony.com/')
        self.login.enter_username("abheet.jamwal@gmail.com")
        self.login.enter_password("Qwerty@123")
        self.login.click_signin_button()
        """ After successfull login user redirected to Auth Screen"""
        if self.login.is_auth_window() == config.LOGIN_2FACTOR_AUTH_HEADER:
            # Enter Auth OTP
            self.login.enter_otp()
            # Verify OTP
            self.login.submit_otp_button()
            assert 'Profile' in self.login.dashboard_content()
            

