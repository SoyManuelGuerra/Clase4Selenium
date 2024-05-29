from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")



# Create a webdriver instance
with webdriver.Chrome(options=chrome_options) as driver:
    # Navigate to a URL
    driver.get('https://www.w3schools.com/html/html_iframe.asp')

    # Switch to iframe
    iframe = driver.find_element(By.XPATH, "//iframe[@title='W3Schools HTML Tutorial']")
    driver.switch_to.frame(iframe)

    # Interact with elements inside the iframe
    boton_dentro_del_iframe = driver.find_element(By.XPATH, "//a[@class='w3-left w3-btn'][@href='/default.asp']")
    boton_dentro_del_iframe.click()

    # Switch back to default content
    driver.switch_to.default_content()
    
    time.sleep(60)