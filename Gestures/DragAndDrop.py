from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException

from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

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

ele = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'))
ele.click()
ele_kw = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ingvw"))

ele_lay = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/layout2"))
# Obtener coordenadas centro del elemento
location = ele_kw.location
size = ele_kw.size
center_x = location['x'] + size['width'] // 2
center_y = location['y'] + size['height'] // 2

location2 = ele_lay.location
size2 = ele_lay.size
center_x2 = location2['x'] + size2['width'] // 2
center_y2 = location2['y'] + size2['height'] // 2

# Crear el input táctil
touch_input = PointerInput("touch", "finger")

# Usar ActionBuilder correctamente
action = ActionBuilder(driver, mouse=touch_input)

# Construir la acción: mover, presionar, pausar, soltar
touch_input.create_pointer_move(x=center_x, y=center_y)
touch_input.create_pointer_down()
touch_input.create_pause(2)  # pausa opcional para simular realismo
touch_input.create_pointer_move(x=center_x2, y=center_y2)

touch_input.create_pointer_up(button=None)

# Ejecutar la acción
action.perform()

time.sleep(3)
driver.quit()
