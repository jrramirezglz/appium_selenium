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
print("Is Displayed : ",element.is_displayed())
print("Is Enabled : ",element.is_enabled())
print("Is selected : ",element.is_selected())
print("Size : ",element.size)
print("Location : ",element.location)