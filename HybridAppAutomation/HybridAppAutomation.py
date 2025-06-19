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

# Step 3 : "Click on the App"
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

# Step 4 : Wait for 2 seconds
time.sleep(2)

# Step 5 : Close the driver object
driver.quit()
#appium_service.stop()

from appium import webdriver
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""
1.) Mobile Browser version and ChromeDriver or respective Browser Driver should be in same version 
2.) 
Two Ways of Identifying locators on webview i) open chrome browser and type "chrome://inspect/#devices" ii) Use Browser 
inspectors 

"""
options = UiAutomator2Options()  # 👈 Instanciar correctamente
options.set_capability("platformName", "Android")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("platformVersion", "16")
options.set_capability("deviceName", "Pixel 9 Pro XL")
options.set_capability("app", "C:/Users/jr_ra/Downloads/Android_Demo_App.apk")
options.set_capability("appPackage", "com.android.chrome")
options.set_capability("appActivity", "com.google.android.apps.chrome.Main")
#create a webwebdriver object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

# 2. Create WebDriverWait
wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

# 3. Open the URL in Browser
ele = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.android.chrome:id/signin_fre_dismiss_button"))
ele.click()
ele = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.android.chrome:id/ack_button"))
ele.click()
ele = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.android.chrome:id/search_box_text"))
ele.click()
ele = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.android.chrome:id/url_bar"))
ele.click()
ele.send_keys("https://www.google.com/")
driver.press_keycode(66)
time.sleep(5)
# 4. Get the list of Contexts in App
appContext =driver.current_context
print("AppContext: ", appContext)
# 5. switch to webview to perform action on Required URL or on WebView
for appType in appContext:
    if appType == "WEBVIEW_chrome":
        driver.switch_to.context(appType)
# 6. Do testing on Webview screen in chrome browser or any if we want
ele = wait.until(lambda  x: x.find_element(AppiumBy.XPATH,"//*[@class='android.widget.EditText']"))
ele.send_keys("Ramon")

# 7. Switch back to native view to perform action
for appType in appContext:
    if appType == "NATIVE_chrome":
        driver.switch_to.context(appType)

# 8. Do testing on native app screen if we want
ele = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.android.chrome:id/url_bar"))
ele.click()
ele.send_keys("https://www.google.com/")
driver.press_keycode(66)

# 9. Quit or close the driver object

time.sleep(5)
driver.quit()
