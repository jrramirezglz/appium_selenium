import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options  # 👈 Importar opciones para Android



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

# Step 3 : "Click on the App"
ele_id = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Btn1"]') # xpath cont desc
#ele_id = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]') # xpath resources id
#ele_id = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ENTER SOME VALUE"]') # xpath text
#ele_id = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[3]') # xpath and index value

ele_id.click()
time.sleep(2)

ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText') # xpath text
ele_xpath.send_keys("ramon")
driver.quit()