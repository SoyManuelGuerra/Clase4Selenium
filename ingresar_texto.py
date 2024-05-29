from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.get("https://www.google.com")

elemento = driver.find_element(By.NAME, "q")

barra_busqueda = driver.find_element(By.NAME, "q")

barra_busqueda.send_keys('Texto precargado')

time.sleep(2)

barra_busqueda.clear()

barra_busqueda.send_keys('Selenium')

barra_busqueda.send_keys(Keys.ENTER)