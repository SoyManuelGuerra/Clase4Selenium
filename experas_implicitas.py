from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inicializar el controlador de Chrome
driver = webdriver.Edge()

# Navegar a la página de Google
driver.get("https://www.google.com")

# Esperar implícitamente hasta 10 segundos
driver.implicitly_wait(10)

# Encontrar el elemento de búsqueda por su nombre y realizar la búsqueda
elemento = driver.find_element(By.NAME, "q")
elemento.clear()
elemento.send_keys("Selenium")
elemento.send_keys(Keys.ENTER)