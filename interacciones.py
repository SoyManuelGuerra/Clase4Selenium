from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.get("https://www.google.com")

elemento = driver.find_element(By.NAME, "q")

# Hacer doble clic en un elemento
action = ActionChains(driver)

action.click(elemento).key_down(Keys.SHIFT).send_keys("hola estoy utilizando selenium")

action.perform()

action.send_keys(Keys.ENTER).perform()

time.sleep(10)