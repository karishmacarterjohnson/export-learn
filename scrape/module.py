from selenium.webdriver.common.by import By
import time
from .login import *


def save_pages(path, module, driver):
    
    driver.get(module)
    time.sleep(1)
    pages = [page.get_attribute('href') for page in driver.find_elements(By.CLASS_NAME, "lesson")]
    driver.close()
    
    driver = login(path)

    i = 0
    for page in pages:
        if page:
            driver.get(page)
            time.sleep(5)
            if i == 0:
                driver.find_element(By.CLASS_NAME, 'toggleaction').click()
                i = 1
            driver.execute_script('window.print();')
    return driver
  