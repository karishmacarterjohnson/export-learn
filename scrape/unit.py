from selenium.webdriver.common.by import By
import time 


def get_units(driver):
    unit_info = {}
    time.sleep(5)
    units =  driver.find_elements(By.CLASS_NAME, "block-container ")

    for unit in units:
        unit_name = unit.get_attribute('id')
        modules = unit.find_elements(By.CLASS_NAME, "standard-card ")
        module_info = {}
        for module in modules:
            page = module.find_element(By.CLASS_NAME, "standard-card-heading")
            module_info[page.get_attribute('title')] = module.get_attribute('href')
            unit_info[unit_name] = module_info
    return unit_info
