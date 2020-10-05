
import pytest
from selenium import webdriver
import config


#get driver path
def get_driver_details():
    if config.WHICH_DRIVER == 'IE':
        driver_instance =  webdriver.Ie(executable_path=config.IE_DRIVER)
    elif config.WHICH_DRIVER == 'FIREFOX':
        driver_instance = webdriver.Firefox(executable_path=config.FIREFOX_DRIVER)
    else:
        driver_instance = webdriver.Chrome(executable_path=config.CHROME_DRIVER)       
    return driver_instance

@pytest.fixture()
def driver():
    driver = get_driver_details()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://my.symphony.com/')
    return driver


  