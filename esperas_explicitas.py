from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.google.com")

elemento = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.NAME, "q"))
)

elemento.clear()
elemento.send_keys("Selenium")
elemento.send_keys(Keys.ENTER)