from selenium import webdriver
import pytest
from ..pages.signinPage import LoginPage
import config


@pytest.mark.lowest
def test_signin_form_exist(driver):
    """
     Test is to validate SignUp existence on the page 
     If Assert = True i.e. Login page available and if its False then
     it mean login form is not available or not loaded
    """
    login = LoginPage(driver)
    driver.get('https://my.symphony.com/')
    # If True Actual Result: Login form exist and visible on screen
    assert login.is_login_form_displayed() == True
    driver.close()


@pytest.mark.lowest
def test_signup_link_clickable(driver):
    """ Test is to validate signup link is working"""
    login = LoginPage(driver)
    driver.get('https://my.symphony.com/')
    current_url = login.signup_link_clickable()
    assert current_url == 'https://my.symphony.com/#signup'
    driver.close()


@pytest.mark.medium
def test_invalid_login_credentials(driver):
    """ Test is to check validations working when 
        invalid credentials used to login 
    """
    login = LoginPage(driver)
    driver.get('https://my.symphony.com/')
    login.enter_username("abheet")
    login.enter_password("abheet")
    login.click_signin_button()
    error = login.get_error_message()
    """ Error messsages received when user input invalid messages"""
    assert error in config.LOGIN_VALIDATION_MESSAGES
    driver.close()


@pytest.mark.highest
def test_sign_in(driver):
    """ Test Login flow with valid flow"""
    login = LoginPage(driver)
    driver.get('https://my.symphony.com/')
    login.enter_username("abheet.jamwal@gmail.com")
    login.enter_password("Qwerty@123")
    login.click_signin_button()
    """ After successfull login user redirected to Auth Screen"""
    if login.is_auth_window() == config.LOGIN_2FACTOR_AUTH_HEADER:
        # Enter Auth OTP
        login = LoginPage(driver)
        login.enter_otp()
        # Verify OTP
        login.submit_otp_button()
        assert login.dashboard_content() == 'All Following'
        driver.close()


def test_teardown(driver):
    driver.quit()
