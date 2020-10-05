from selenium import webdriver
import pytest
from ..pages.forgetPage import ForgetPassword
import config

@pytest.mark.lowest
def test_forget_passsword_page_load(driver):   
    """
     Test is to validate forget password the page 
     If Assert = True i.e. forget password page available and if its False then
     it mean login form is not available or not loaded
    """
    #If True Actual Result: forget password form exist and visible on screen
    reset_password = ForgetPassword(driver)
    reset_password.click_forget_password_link()
    assert reset_password.is_forget_password_page_displayed()
    driver.close()
   
    
@pytest.mark.medium    
def test_blank_email_validation(driver):
    """ Test is to check validations working when 
        invalid credentials used to login 
    """
    reset_password = ForgetPassword(driver)
    driver.get("https://my.symphony.com/#forgot-password")
    reset_password.enter_email("")
    reset_password.click_recover_password_button()
    error = reset_password.validation_message()
    """ Error messsages received when user input invalid messages"""
    assert  error in config.RESET_PASSWORD_VALIDATION_MESSAGES
    driver.close()
    
@pytest.mark.medium    
def test_captcha_validation(driver):
    """ Test is to check validations working when 
        invalid credentials used to login 
    """
    reset_password = ForgetPassword(driver)
    driver.get("https://my.symphony.com/#forgot-password")
    reset_password.enter_email("abheet.jamwal@gmail.com")
    reset_password.click_recover_password_button()
    error = reset_password.validation_message()
    """ Error messsages received when user input invalid messages"""
    assert  error in config.RESET_PASSWORD_VALIDATION_MESSAGES    
    driver.close()
    
def test_teardown(driver):
    driver.quit()
   