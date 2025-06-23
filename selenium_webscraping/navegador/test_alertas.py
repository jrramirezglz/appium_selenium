import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from pytest import mark

@mark.alertas
def test_navegacion_browser():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.find_element(By.XPATH, "//*[text() = 'Simple Alert']").click()
    alert = Alert(driver)
    time.sleep(5)
    alert.accept()
    time.sleep(5)

@mark.cookies
def test_cookies_browser():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    print("Cookies:" ,driver.get_cookies())
    driver.add_cookie({"name": "udemy", "value": "cookies browser"})
    print("Cookies:" ,driver.get_cookies())
    driver.delete_cookie("udemy")
    driver.delete_all_cookies()
    print("Cookies:" ,driver.get_cookies())

    time.sleep(5)

