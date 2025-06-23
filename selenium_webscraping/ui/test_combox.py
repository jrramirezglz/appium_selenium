import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pytest import mark

@mark.combobox
def test_combobox_test():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView;", 'country')
    select_country = Select(driver.find_element(By.ID, 'country'))
    select_country.select_by_value('usa')
    time.sleep(5)