from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time  # Import the time module

def test():
    try:
        firefox_options = Options()
        firefox = webdriver.Firefox(options=firefox_options)
        firefox.get('https://twitter.com/i/flow/login')
        firefox.maximize_window()
        time.sleep(10)
        
        input_field = firefox.find_element(By.NAME, 'text')
        input_field.send_keys('promonkey9')
        
        time.sleep(200)
       

    except WebDriverException as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser window, even if an exception occurred
        if firefox is not None:
            firefox.quit()

test()
