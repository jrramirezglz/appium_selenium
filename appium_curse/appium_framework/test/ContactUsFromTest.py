from appium_curse.appium_framework.base.DriverClass import Driver
from appium_curse.appium_framework.base.BasePage import BasePage

import appium_curse.appium_framework.utilities.CustomLogger as cl
driver1 = Driver()
log =cl.customLogger()
driver = driver1.getDriverMethod()
log.info("Launch App")
bp = BasePage(driver)
bp.takeScreenshots("App")
element = bp.isDisplayed("com.code2lead.kwad:id/ContactUs", "id")
print(element)
bp.clickElement("com.code2lead.kwad:id/ContactUs", "id")
bp.sendText("ramon","Enter Name", "text")
bp.takeScreenshots("Final")
