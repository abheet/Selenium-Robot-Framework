import pytest
from selenium import webdriver
import config
import time

# Pytest Fixture get driver path
@pytest.fixture(scope="class", params=[config.WHICH_DRIVER])
def browser(request):
    # Setup details
    driver_instance = ""
    if request.param == 'IE':
        driver_instance = webdriver.Ie(executable_path=config.IE_DRIVER)
    elif request.param == 'FIREFOX':
        driver_instance = webdriver.Firefox(
            executable_path=config.FIREFOX_DRIVER)
    elif request.param == 'CHROME':
        driver_instance = webdriver.Chrome(
            executable_path=config.CHROME_DRIVER)
    driver_instance.maximize_window()
    driver_instance.get("https://my.site.com")
    time.sleep(5)
    # Skip test if browser is not compatible
    if driver_instance.current_url == 'https://my.site.com/browsers.html':
        driver_instance.close()
        driver_instance.quit()
        pytest.skip("Browser is NOT compatible with App")
        config.LOGGER.info(
            "Browser is not compatible with app. Skipping test..")
       
    else:
        request.cls.driver = driver_instance
        config.LOGGER.info("Driver inititalized")
        
    yield    
    # Teardown steps
    driver_instance.close()
    driver_instance.quit()
    config.LOGGER.info("Driver closed")
        
