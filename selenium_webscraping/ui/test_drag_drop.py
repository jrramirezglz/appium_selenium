import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pytest import mark

@mark.dragdrop
def test_dragdrop_test():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.execute_script("arguments[0].scrollIntoView;", 'draggable')
    time.sleep(2)
    source = driver.find_element(By.ID, 'draggable' )
    target = driver.find_element(By.ID, 'droppable')
    action = ActionChains(driver)
    action.drag_and_drop(source, target).perform()
    time.sleep(5)