import logging
LOGGER = logging.getLogger(__name__)

#Which browser need for test

#Possible values :  CHROME/FIREFOX or IE
WHICH_DRIVER = 'CHROME' 

#driver paths
CHROME_DRIVER = 'BrowserDrivers/Chrome/linux/chromedriver'
FIREFOX_DRIVER = 'BrowserDrivers/Firefox/linux64/geckodriver'

#only for windows
IE_DRIVER = 'BrowserDrivers/InternetExplorer/IEDriverServer.exe'

#Validation messages
LOGIN_VALIDATION_MESSAGES = ('All fields are required.','Invalid username or password.')
SIGNUP_VALIDATION_MESSAGES = ('First name, last name, email and password are required to join Symphony.\nPlease enter all four fields.',
                              'Please provide a valid password.',
                              'An e-mail address is required.',
                              )
RESET_PASSWORD_VALIDATION_MESSAGES = ('An e-mail address is required.','Please fill in the Captcha first.')


#Screen Titles
SIGNUP_SUB_TITLE = "Sign up with your details"
INVITE_TEAM_TITLE = "Invite Your Team"
SIGNUP_CONFIRMAION = "Pending email verification"
LOGIN_2FACTOR_AUTH_HEADER = 'Authentication Required'


#Twilio Account
TWILIO_ACCOUNT = "ACf24b6fc1d2824781c79ec49705cb2205"
TWILIO_AUTH_TOKEN= "cabe53adf11e05f1cd6bd51afade6241"