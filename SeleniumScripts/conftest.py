import pytest
from selenium import webdriver
import config


#Pytest Fixture get driver path
@pytest.fixture(scope="class", params=[config.WHICH_DRIVER])
def browser(request):
    #Setup details 
    driver_instance = ""
    if request.param == 'IE':
            driver_instance =  webdriver.Ie(executable_path=config.IE_DRIVER)
    elif request.param == 'FIREFOX':
        driver_instance = webdriver.Firefox(executable_path=config.FIREFOX_DRIVER)
    elif request.param == 'CHROME':
        driver_instance = webdriver.Chrome(executable_path=config.CHROME_DRIVER)  
    
    driver_instance.maximize_window()    
    request.cls.driver = driver_instance
    config.LOGGER.info("Driver inititalized")
    yield
    #Teardown steps
    driver_instance.quit()
    config.LOGGER.info("Driver closed")


  