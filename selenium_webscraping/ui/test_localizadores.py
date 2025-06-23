import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

def test_element_by_class():
    driver = webdriver.Chrome()
    driver.get("https://automationpractice.pl/")

# selecciona el primer elemento de esa clase y da click
    web_element = driver.find_element(By.CLASS_NAME, "item-img")
    web_element.click()

# muestra los elementos que tienen el mismo nombre de clase
    #web_element = driver.find_elements(By.CLASS_NAME, "item-img")
    #print("Cantidad de elementos Clase :", len(web_element))
    time.sleep(10)

def test_element_by_xpath():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    web_element = driver.find_element(By.XPATH,'//*[@id="name"]')
    web_element.send_keys("Juan")
    time.sleep(4)