import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark

@mark.navegador
def test_navegacion_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.nytimes.com/")
    print("URL actual: ",driver.current_url)
    driver.execute_script("arguments[0].scrollIntoView;", 'Games')

    driver.find_element(By.LINK_TEXT, 'Games').click()
    print("URL actual: ",driver.current_url)

    driver.back()
    print("URL actual: ",driver.current_url)

    driver.forward()
    print("URL actual: ",driver.current_url)

    driver.refresh()
    print("URL actual: ",driver.current_url)
    time.sleep(6)
