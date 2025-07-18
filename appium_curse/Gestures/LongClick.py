from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium_webscraping.webdriver.support.ui import WebDriverWait
from selenium_webscraping.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException

from selenium_webscraping.webdriver.common.actions.action_builder import ActionBuilder
from selenium_webscraping.webdriver.common.actions.pointer_input import PointerInput

import time

# Configuración de Appium y dispositivo
options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("platformVersion", "16")
options.set_capability("deviceName", "Pixel 9 Pro XL")
options.set_capability("app", "C:/Users/jr_ra/Downloads/Android_Demo_App.apk")
options.set_capability("appPackage", "com.code2lead.kwad")
options.set_capability("appActivity", "com.code2lead.kwad.MainActivity")

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

# Scroll y encontrar elemento con texto "LONG CLICK"
ele = wait.until(lambda d: d.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector()).scrollIntoView(text("LONG CLICK"))'
))

# Obtener coordenadas centro del elemento
location = ele.location
size = ele.size
center_x = location['x'] + size['width'] // 2
center_y = location['y'] + size['height'] // 2
# Crear el input táctil
touch_input = PointerInput("touch", "finger")

# Usar ActionBuilder correctamente
action = ActionBuilder(driver, mouse=touch_input)

# Construir la acción: mover, presionar, pausar, soltar
touch_input.create_pointer_move(duration=0, x=center_x, y=center_y, origin="viewport")
touch_input.create_pointer_down()
touch_input.create_pause(5)  # mantener pulsado 2 segundos
touch_input.create_pointer_up(button=None)

# Ejecutar la acción
action.perform()

time.sleep(3)
driver.quit()
