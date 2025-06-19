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

# Step 2 : Wait for 2 seconds
time.sleep(5)

driver.execute_script("mobile: shell", {
    "command": "am",
    "args": ["start", "-n", "com.android.chrome/com.google.android.apps.chrome.Main"],
    "includeStderr": True,
    "timeout": 5000
})
# Step 5 : Close the driver object
time.sleep(5)

driver.execute_script("mobile: shell", {
    "command": "am",
    "args": ["start", "-n", "com.code2lead.kwad/com.code2lead.kwad.MainActivity"],
    "includeStderr": True,
    "timeout": 5000
})
time.sleep(5)

driver.quit()
#appium_service.stop()