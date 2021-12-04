from selenium.webdriver.common.by import By
import time
from .login import *

def assessment(driver):
    time.sleep(2)
    if driver.current_url.find('assessment=true') != -1:
        driver.find_element(By.XPATH, "//button[@class='button-wrapper button-solid-primary  ']").click()
        time.sleep(2)
        driver.execute_script('window.print();')


def save_pages(path, module, driver):
    
    driver.get(module)
    time.sleep(1)
    pages = [page.get_attribute('href') for page in driver.find_elements(By.CLASS_NAME, "lesson")]
    pages += [page.get_attribute('href') for page in driver.find_elements(By.CLASS_NAME, "checkpoint")]
    driver.close()
    driver = login(path)
    i = 0
    if pages != []:
        for page in pages:
            if page: 
                driver.get(page)
                assessment(driver)
                if i == 0:
                    driver.find_element(By.CLASS_NAME, 'toggleaction').click()
                    i = 1
                driver.execute_script('window.print();')
            
    else:
        driver.get(module)
        assessment(driver)

    return driver
  