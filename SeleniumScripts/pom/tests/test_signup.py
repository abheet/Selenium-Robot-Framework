from selenium import webdriver
import pytest
from ..pages.signupPage import SignupPage
from ..pages.signupPage import LoginPage
from ..pages.util_methods import get_dummy_email, get_email_activation_link
import config



@pytest.mark.lowest
def test_signup_form_exist(driver):   
    """
     Test is to validate SignUp existence on the page and is marked as lowest priority 
     If Assert = True i.e. signup page available and if its False then
     it mean signup form is not available or not loaded
    """
    driver.get('https://my.symphony.com/#signup')
    signup = SignupPage(driver)
    assert signup.is_signup_form_displayed() == config.SIGNUP_SUB_TITLE
    
@pytest.mark.lowest    
def test_signin_link_working(driver):
    """ Test is to validate signup link is working, and is marked as lowest priority  """
    driver.get('https://my.symphony.com/#signup')
    signup = SignupPage(driver)
    current_url = signup.click_signin_link()
    config.LOGGER.info("Actual Result: Signin link on SignUp form exist and clicked successfully")
    assert current_url == 'https://my.symphony.com/#login'
    
@pytest.mark.medium    
def test_validation_for_blank_submitions(driver):
    """ Test is to check validations working or not ,and is marked as medium priority  """
    driver.get("https://my.symphony.com/#signup")
    signup = SignupPage(driver)
    signup.enter_email("test@test.com")
    signup.enter_first_name("")
    signup.enter_last_name("")
    signup.enter_signup_password("")
    signup.click_signup_button()
    error = signup.get_error_message()
    """ Error messsages received when user input invalid messages"""
    assert  error in config.SIGNUP_VALIDATION_MESSAGES
       
@pytest.mark.highest
def test_signup_flow(driver):
    """ Test instance flow with valid flow ,and is marked as highest priority"""
    #Generate dummy email address
    global dummy_email
    dummy_email = get_dummy_email(driver)
    #start Signup flow
    driver.get("https://my.symphony.com/#signup")
    signup = SignupPage(driver)
    #fill the signup form
    signup.enter_first_name("Auto")
    signup.enter_last_name("User")
    signup.enter_email(dummy_email)
    signup.enter_signup_password("Qwerty@123")
    signup.click_signup_button()
    # """ After successfull signup user redirected to Invite Team form"""
    signup.skip_invite_team_form()
    #validate after skipping signup user redirected to email activation sent page
    assert signup.email_confirmation_sent() == config.SIGNUP_CONFIRMAION

@pytest.mark.highest    
def test_email_activation(driver):
    """ Test email activation flow ,and is marked as highest priority"""
    activation_link = get_email_activation_link(driver,dummy_email)
    if activation_link:
        driver.get(activation_link)
        login = LoginPage(driver)
        #If True Email activation completed and Login pages loaded thereafter
        assert login.is_login_form_displayed() == True
        

def test_teardown(driver):
    driver.close()
    driver.quit()


    