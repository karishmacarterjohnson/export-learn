from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import json
import os
from dotenv import load_dotenv

load_dotenv()

def login(path):

    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
    
    chrome_options = webdriver.ChromeOptions()
    settings = {
        "recentDestinations": [{
                "id": "Save as PDF",
                "origin": "local",
                "account": "",
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }

    prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings),
            'savefile.default_directory': path
            }
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    #chrome_options.add_argument('--headless')


    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    driver.get("https://auth.galvanize.com/sign_in")
    driver.find_element_by_id("user_email").send_keys(username)
    driver.find_element_by_id("user_password").send_keys(password)
    driver.find_element_by_name("commit").click()

    return driver

