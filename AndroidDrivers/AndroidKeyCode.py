
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options  # 👈 Importar opciones para Android
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

# Android Key Codes (para usar con Appium y driver.press_keycode())
KEYCODE_HOME = 3
KEYCODE_BACK = 4
KEYCODE_CALL = 5
KEYCODE_ENDCALL = 6
KEYCODE_0 = 7
KEYCODE_1 = 8
KEYCODE_2 = 9
KEYCODE_3 = 10
KEYCODE_4 = 11
KEYCODE_5 = 12
KEYCODE_6 = 13
KEYCODE_7 = 14
KEYCODE_8 = 15
KEYCODE_9 = 16
KEYCODE_STAR = 17
KEYCODE_POUND = 18
KEYCODE_DPAD_UP = 19
KEYCODE_DPAD_DOWN = 20
KEYCODE_DPAD_LEFT = 21
KEYCODE_DPAD_RIGHT = 22
KEYCODE_DPAD_CENTER = 23
KEYCODE_VOLUME_UP = 24
KEYCODE_VOLUME_DOWN = 25
KEYCODE_POWER = 26
KEYCODE_CAMERA = 27
KEYCODE_CLEAR = 28
KEYCODE_A = 29
KEYCODE_B = 30
KEYCODE_C = 31
KEYCODE_D = 32
KEYCODE_E = 33
KEYCODE_F = 34
KEYCODE_G = 35
KEYCODE_H = 36
KEYCODE_I = 37
KEYCODE_J = 38
KEYCODE_K = 39
KEYCODE_L = 40
KEYCODE_M = 41
KEYCODE_N = 42
KEYCODE_O = 43
KEYCODE_P = 44
KEYCODE_Q = 45
KEYCODE_R = 46
KEYCODE_S = 47
KEYCODE_T = 48
KEYCODE_U = 49
KEYCODE_V = 50
KEYCODE_W = 51
KEYCODE_X = 52
KEYCODE_Y = 53
KEYCODE_Z = 54
KEYCODE_COMMA = 55
KEYCODE_PERIOD = 56
KEYCODE_ALT_LEFT = 57
KEYCODE_ALT_RIGHT = 58
KEYCODE_SHIFT_LEFT = 59
KEYCODE_SHIFT_RIGHT = 60
KEYCODE_TAB = 61
KEYCODE_SPACE = 62
KEYCODE_SYM = 63
KEYCODE_ENTER = 66
KEYCODE_DEL = 67  # Backspace
KEYCODE_GRAVE = 68
KEYCODE_MINUS = 69
KEYCODE_EQUALS = 70
KEYCODE_LEFT_BRACKET = 71
KEYCODE_RIGHT_BRACKET = 72
KEYCODE_BACKSLASH = 73
KEYCODE_SEMICOLON = 74
KEYCODE_APOSTROPHE = 75
KEYCODE_SLASH = 76
KEYCODE_AT = 77
KEYCODE_PLUS = 81
KEYCODE_MENU = 82
KEYCODE_SEARCH = 84
KEYCODE_MEDIA_PLAY_PAUSE = 85
KEYCODE_MEDIA_STOP = 86
KEYCODE_MEDIA_NEXT = 87
KEYCODE_MEDIA_PREVIOUS = 88
KEYCODE_MEDIA_REWIND = 89
KEYCODE_MEDIA_FAST_FORWARD = 90
KEYCODE_MUTE = 91
KEYCODE_PAGE_UP = 92
KEYCODE_PAGE_DOWN = 93
KEYCODE_PICTSYMBOLS = 94
KEYCODE_SWITCH_CHARSET = 95
KEYCODE_BUTTON_A = 96
KEYCODE_BUTTON_B = 97
KEYCODE_BUTTON_C = 98
KEYCODE_BUTTON_X = 99
KEYCODE_BUTTON_Y = 100
KEYCODE_BUTTON_Z = 101
KEYCODE_BUTTON_L1 = 102
KEYCODE_BUTTON_R1 = 103
KEYCODE_BUTTON_L2 = 104
KEYCODE_BUTTON_R2 = 105
KEYCODE_BUTTON_THUMBL = 106
KEYCODE_BUTTON_THUMBR = 107
KEYCODE_BUTTON_START = 108
KEYCODE_BUTTON_SELECT = 109
KEYCODE_BUTTON_MODE = 110


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
ele = wait.until(lambda x:x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue"))
ele.click()
ele = wait.until(lambda x:x.find_element(AppiumBy.XPATH, '//android.widget.EditText'))
ele.send_keys("ramon")
ele.click()
driver.press_keycode(67)
driver.press_keycode(67)


time.sleep(4)
driver.press_keycode(4)
driver.press_keycode(4)
time.sleep(4)

driver.quit()