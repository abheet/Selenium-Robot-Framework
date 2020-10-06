# Locators for pages
from selenium.webdriver.common.by import By

class LoginPageLocators(object):

    """
    A Class for LoginPage Locators. All identifier details are available here.
    Variable naming conventions are maintened on the bases their identifiers
    i.e. used as suffixes with _id, _name or class
    """

    # ********* Login/SignIn Page 1 *******
    USERNAME_INPUT = (By.ID, "signin-email")
    PASSWORD_INPUT = (By.ID, "signin-password")
    REMEMBER_ME_CHECKBOX = (By.ID, "signin-remember")
    #Error Message container DIV 
    ERROR_DIV = (By.ID,"sysMsg")
    ERROR_SHOWN = (By.CLASS_NAME,"fail show")
    ERROR_MESSAGE = (By.CLASS_NAME,"message") 

    # Click to actions
    FORGET_PASSWORD_HREF = (By.LINK_TEXT, "Forgot your password?")
    SIGNUP_HREF = (By.LINK_TEXT, 'Sign up')
    LOGIN_SUBMIT_BUTTON = (By.NAME,"signin-submit")
    
    #Dashboard Locator
    DASHBOARD_CONTENT = (By.XPATH, "//span[@class='navigation-item-name']")

class AuthPageLocator(object):
    """
     A class for 2-Factor AUTH Section/Page i.e OTP verification
    """
    # ****************Login/SignIn Page 1.1 -> Authentication Required****

    AUTH_CONTAINER_DIV = (By.XPATH, '//*[@id="authentication"]/div[1]/div[1]/div[1]/h1[1]')    
    OTP_INPUT = (By.NAME,"authcode")
    OTP_SUBMIT_BUTTON = (By.NAME,"authcode-submit")
    CANCEL_HREF = (By.LINK_TEXT,"Cancel")
    RESEND_OTP_HREF = (By.LINK_TEXT,"Send Again")


class SignUpPageLocator(object):
    # ********* # SignUp Page 2 *******
    # Inputs: Fist Name, Last Name, Email and Password
    FIRST_NAME_INPUT = (By.ID,"signup-first")
    LAST_NAME_INPUT = (By.ID,"signup-last")
    EMAIL_INPUT = (By.ID,"signup-email")
    PASSWORD_INPUT = (By.ID, "signup-password")
    
    #SIGNUP PAGE SUBHEADER: Sign up with your details
    SIGNUP_PAGE_SUBHEADER = (By.XPATH, "//span[@class='secondary-title']")

    # Click to Action: Submit button (next)
    SIGNUP_BUTTON = (By.XPATH, "//button[text()='Next']")
    LOGIN_LINK = (By.LINK_TEXT, 'Sign in')
    
    DUMMY_EMAIL_ID = (By.ID, 'email_ch_text')
    CONFIRM_EMAIL_TEXT = (By.XPATH, "//a[text()='Confirm Your Email']")

class InvitePersonPageLocator(object):
    # *********Signup > Team Invites Page 2.1 *******
    # Invite Container Title 
    INVITE_PAGE_TITLE = (By.XPATH,"//span[@class='title']")

    #Invite form input fields
    INVITE_EMAIL = (By.CLASS_NAME, "email")
    INVITE_FIRST_NAME = (By.CLASS_NAME, "first_name")
    INVITE_LAST_NAME = (By.CLASS_NAME, "last_name")

    #Click to Action
    SKIP_BUTTON = (By.XPATH,"//div[@class='button negative skip']")
    NEXT_BUTTON = (By.XPATH, "//div[text()='Next']") 

    # Add New Person button
    ADD_INVITE_FORM = (By.CLASS_NAME,"invite-form add-one")
   
    # *********Signup Submited > Page 2.2(resend email link) *******
    SIGNUP_CONFIRMATION_TITLE = (By.XPATH, "//p[text()='Pending email verification']")
    # Click to Action
    RESEND_ACTIVATION_LINK = (By.LINK_TEXT, "Resend") 

class SaveMobilePageLocator(object):
    # *********Signup >  VerifyPhone after email activation step (Mobile OTP) *******
    FLAG_DROPDOWN = (By.ID, "country-listbox")
    COUNTRY_CODE = (By.ID, "iti-item-in")
    MOBILE_NUMBER_INPUT = (By.ID, "mobile-phone-number")

    # Click to Action:button
    MOBILE_SUBMIT_BUTTON = (By.CLASS_NAME, "button green send-phone-number")

    # verify OTP (verify OTP)
    OTP_INPUT = (By.ID, "mobile-verification-code")
    #Click to Action
    RESEND_OTP_BUTTON = (By.CLASS_NAME, "button negative resend-phone-number")
    SUBMIT_OTP_BUTTON =  (By.CLASS_NAME, "button green verify-code")
    CHNAGE_MOBILE = (By.CLASS_NAME, "button negative blue change-number")
 

class ForgetPasswordPageLocator(object):
    """
    A Class is for ForgetPassword page, it contains all locator for forget password page
    """
    
    EMAIL_INPUT = (By.NAME, "recover-email")
    CAPTCHA_CHECKBOX = (By.ID, "recaptcha-anchor")
    CAPTCHA_AUDIO_BUTTON = (By.ID, "recaptcha-audio-button")
    
    PASSWORD_SENT_CONFIRMATION = (By.CLASS_NAME, "password-link__title") #Password reset email sent
    # click to action
    CANCEL_HREF = (By.LINK_TEXT, "Cancel")
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//button[@name='recover-submit']")
    
    PASSWORD_UPDATED_SUCCESS = (By.XPATH, "//div[@class='auth-container']/h1[text()='Success']")
