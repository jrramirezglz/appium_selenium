import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options  # 👈 Importar opciones para Android
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

options = UiAutomator2Options()  # 👈 Instanciar correctamente
options.set_capability("platformName", "Android")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("platformVersion", "16")
options.set_capability("deviceName", "Pixel 9 Pro XL")
options.set_capability("app", "C:/Users/jr_ra/Downloads/Android_Demo_App.apk")
options.set_capability("appPackage", "com.code2lead.kwad")
options.set_capability("appActivity", "com.code2lead.kwad.MainActivity")
#create a webwebdriver object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

#list of Selenium Exceptions
#https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html

wait =WebDriverWait(driver, 25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
ele = wait.until(lambda x:x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ScrollView"))
ele.click()
ele = wait.until(lambda x:x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON16"))'))
ele.click()
time.sleep(4)
driver.quit()