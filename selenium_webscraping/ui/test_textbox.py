import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark

@mark.textbox
def test_textbox_interaction():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    text_box = driver.find_element(By.ID,"name")
    text_box.send_keys("hola")
    text_box.clear()

    text_box.send_keys("hola de nuevo")
    actual_value = text_box.get_attribute("value")
    print(actual_value)

@mark.checkbox
def test_checkbox_iterraction():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    check_box = driver.find_element(By.ID,"saturday")
    #con este codigo hace scroll hasta encontrar el elemento
    driver.execute_script("arguments[0].scrollIntoView;", 'check_box')
    time.sleep(5)
    print("Seleccionado  :", check_box.is_selected())
    driver.execute_script("arguments[0].click();", 'check_box')
    time.sleep(3)
    #de esta forma se sabe que tipo de elemento es
    print("Tipo de elemento :", check_box.get_attribute("type"))
    #ver si esta seleccionado o no
    print("Seleccionado  :", check_box.is_selected())

@mark.calendario
def test_calendario_iteraction():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.execute_script("arguments[0].scrollIntoView;", 'datepicker')
    calendario = driver.find_element(By.ID, "datepicker")
    calendario.click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@class='ui-state-default' and text()='1']").click()
    time.sleep(2)
    calendario.click()
    driver.find_element(By.XPATH, "//*[@class='ui-state-default' and text()='14']").click()
    time.sleep(2)
    calendario.clear()
    calendario.send_keys('03/12/1991')
    time.sleep(5)

