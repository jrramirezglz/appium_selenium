from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options  # 👈 Importar opciones para Android
import time
#from appium.webdriver.appium_service import AppiumService
#appium_service =AppiumService()
#appium_service.start()
# Step 1 : Create "Desired Capabilities"


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

element = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
print("Text on the Button ", element.text)
print("Text on the Button ", element.get_attribute("text"))
print("Content Des  of the Button ", element.get_attribute("content-desc"))
element.click()

time.sleep(2)

ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_classname.send_keys("Ramon")
time.sleep(2)
ele_classname.clear()
time.sleep(2)
ele_classname.send_keys("Ramon")

time.sleep(2)
driver.quit()