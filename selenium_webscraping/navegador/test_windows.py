import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark

@mark.windows
def test_windows_elements():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.execute_script("arguments[0].scrollIntoView;", 'Posts (Atom)')
    time.sleep(3)
    print(driver.current_window_handle)
    print(len(driver.window_handles))
    driver.find_element(By.XPATH, "//*[@class= 'feed-link' and text() = 'Posts (Atom)']").click()
    time.sleep(3)
    print(len(driver.window_handles))
    driver.switch_to.new_window("tab")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.set_window_size(1024,768)
    time.sleep(5)
    driver.maximize_window()
    time.sleep(5)
    driver.minimize_window()
    time.sleep(5)

    driver.switch_to.new_window('window')
    print(len(driver.window_handles))

@mark.windows
def test_screenshots():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.save_screenshot('./imagen3.png')