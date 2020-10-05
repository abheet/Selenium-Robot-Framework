from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.locators import  SignUpPageLocator
import config


def input_values(web_driver,locator,value=""):
    """Input/Enter Values for specific elements on page"""
    try:
        web_element = WebDriverWait(web_driver,10).until(
            EC.presence_of_element_located(locator))
        web_element.clear()
        web_element.send_keys(value)
    except Exception as err:
        config.LOGGER.error("Element {} not captured {}".format(err,locator))
            


def get_values(web_driver, locator, element_attribute):
    """Get Values for specific elements on page"""
    try:
        element = WebDriverWait(web_driver, 30).until(
            EC.presence_of_element_located(locator))
        element_value = element.get_attribute(element_attribute)
        return element_value
    except Exception as err:
        config.LOGGER.error("Element {} not captured {}".format(err,locator))
    
    
""" Below methods bring Dummy Emails for sign up activation link and password reset """
def get_dummy_email(driver):
    """ 
        Function is to provide random dummy email address for signup flow.
        Returns : Dummy email value
    """
    try:
        #temp storage for activation perpose, as it need to fetch related inbox
        driver.get("https://emailfake.com")
        dummy_email_locator = SignUpPageLocator.DUMMY_EMAIL_ID
        
        #Dummy email address from util function
        email = []
        element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(dummy_email_locator))
        email.append(element.get_attribute('innerHTML'))
        config.LOGGER.info("Dummy email adrress generated: {}".format(email[0]))
        return email[0]
    except Exception as err:
        config.LOGGER.error("Unable to load dummy email address {}".format(err))
        

def get_email_activation_link(driver,email):
    """ Function fetch email activation link from provided dummy Email Inbox"""
    try:
        locator = SignUpPageLocator.CONFIRM_EMAIL_TEXT
        inbox_url = "https://emailfake.com/{}".format(str(email))
        #browse Above url to read received email from inbox
        driver.get(inbox_url)
        driver.implicitly_wait(40)
        driver.refresh()
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located(locator))
        activation_link = []
        activation_link.append(element.get_attribute('href'))
        config.LOGGER.info("Activation link received: {}".format(element.get_attribute('href')))
        return activation_link[0]
    except Exception as err:
        config.LOGGER.error("Look like activation link not received in inbox {}".format(err))
        

def read_sms_otp():
    #Twilio API helps to validate AUTH OTP
    import requests
    url =  'https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json?To=9285855239&DateSent='.format(config.TWILIO_ACCOUNT)
    response = requests.get(url, auth=(config.TWILIO_ACCOUNT, config.TWILIO_AUTH_TOKEN))   
    otp = response.json()['messages'][0]['body'].split(" ")[0]
    return otp
         


           