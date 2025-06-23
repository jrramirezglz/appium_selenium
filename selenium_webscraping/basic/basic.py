import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome()

driver.get("https://www.google.com/")
wait = WebDriverWait(driver, 10)  # Espera máximo 10 segundos
textbox = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="q"]')))
textbox.click()
textbox.send_keys("Ramon")
textbox.send_keys(Keys.ENTER)
time.sleep(10)
driver.quit()
