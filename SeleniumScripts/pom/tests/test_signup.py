from selenium import webdriver
import pytest
from ..pages.signupPage import SignupPage
from ..pages.signupPage import LoginPage
from ..pages.util_methods import get_dummy_email, get_email_activation_link
import config

@pytest.mark.usefixtures("browser")
class TestSignUp:

    @pytest.mark.lowest
    def test_signup_form_exist(self):   
        """
        Test is to validate SignUp existence on the page and is marked as lowest priority 
        If Assert = True i.e. signup page available and if its False then
        it mean signup form is not available or not loaded
        """
        self.signup = SignupPage(self.driver)
        self.driver.get('https://my.symphony.com/#signup')
        assert self.signup.is_signup_form_displayed() == config.SIGNUP_SUB_TITLE
        
    @pytest.mark.lowest    
    def test_signin_link_working(self):
        """ Test is to validate signup link is working, and is marked as lowest priority  """
        self.driver.get('https://my.symphony.com/#signup')
        self.signup = SignupPage(self.driver)
        current_url = self.signup.click_signin_link()
        config.LOGGER.info("Actual Result: Signin link on SignUp form exist and clicked successfully")
        assert current_url == 'https://my.symphony.com/#login'

    @pytest.mark.medium    
    def test_validation_for_blank_submitions(self):
        """ Test is to check validations working or not ,and is marked as medium priority  """
        self.driver.get("https://my.symphony.com/#signup")
        self.signup = SignupPage(self.driver)
        self.signup.enter_email("test@test.com")
        self.signup.enter_first_name("")
        self.signup.enter_last_name("")
        self.signup.enter_signup_password("")
        self.signup.click_signup_button()
        error = self.signup.get_error_message()
        """ Error messsages received when user input invalid messages"""
        assert  error in config.SIGNUP_VALIDATION_MESSAGES
        
    @pytest.mark.highest
    def test_signup_flow(self):
        """ Test instance flow with valid flow ,and is marked as highest priority"""
        #Generate dummy email address
        global dummy_email
        dummy_email = get_dummy_email(self.driver)
        #start Signup flow
        self.driver.get("https://my.symphony.com/#signup")
        self.signup = SignupPage(self.driver)
        #fill the signup form
        self.signup.enter_first_name("Auto")
        self.signup.enter_last_name("User")
        self.signup.enter_email(dummy_email)
        self.signup.enter_signup_password("Qwerty@123")
        self.signup.click_signup_button()
        # """ After successfull ignup user redirected to Invite Team form"""
        self.signup.skip_invite_team_form()
        #validate after skipping signup user redirected to email activation sent page
        assert self.signup.email_confirmation_sent() == config.SIGNUP_CONFIRMAION
        
    @pytest.mark.highest    
    def test_email_activation(self):
        """ Test email activation flow ,and is marked as highest priority"""
        activation_link = get_email_activation_link(self.driver,dummy_email)
        if activation_link:
            self.driver.get(activation_link)
            self.login = LoginPage(self)
            #If True Email activation completed and Login pages loaded thereafter
            assert self.login.is_login_form_displayed() == True

        