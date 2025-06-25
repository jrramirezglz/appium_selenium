from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import appium_curse.appium_pom_model.utilities.CustomLogger as cl
import time
class BasePage:
    log = cl.customLogger()
    def __init__(self,driver):
        self.driver =driver

    def waitForElement(self, locatorValue, locatorType):
        locatorType=locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID,locatorValue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME,locatorValue))
            return element
        elif locatorType == "des":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'description("%s")'%(locatorValue)))
            return element
        elif locatorType == "index":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'index("%d")'%int(locatorValue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")'%locatorValue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s'%(locatorValue)))
            return element
        else:
            self.log.error("Locator value" +  locatorValue + "not found")


    def getElement(self,locatorValue,locatorType ="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue,locatorType)
            self.log.info("Element found with locator value " + locatorValue + " using locator type " + locatorType)
        except:
            self.log.info("WebElement not found with locator value " + locatorValue + " using locator type " + locatorType)
        return element


    def clickElement(self,locatorValue,locatorType ="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue,locatorType)
            element.click()
            self.log.info("Click Element found with locator value " + locatorValue + " using locator type " + locatorType)
        except:
            self.log.info("Unable Click Elementfound with locator value " + locatorValue + " using locator type " + locatorType)
        return element

    def sendText(self, text, locatorValue, locatorType ="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue,locatorType)
            element.send_keys(text)
            self.log.info("Send text on Element found with locator value " + locatorValue + " using locator type " + locatorType)
        except:
            self.log.info("Unable Send text on Element with locator value " + locatorValue + " using locator type " + locatorType)

    def isDisplayed(self, locatorValue, locatorType ="id"):
        elementText = None

        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue,locatorType)
            element.is_displayed()
            self.log.info(" Element is displayed with locator value " + locatorValue + " using locator type " + locatorType  + "is displayed")
            return True
        except:
            self.log.info("Element is not displayed with locator value " + locatorValue + " using locator type " + locatorType  + "is not displayed")
            return False

    def scroll(self, locatorValue, locatorType ="id"):
        actions =ActionChains(self.driver)
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue,locatorType)
            actions.move_to_element(webElement).perform()
            self.log.info(" WebElement is displayedwith locator value " + locatorValue + " using locator type " + locatorType)
        except:
            self.log.info("WebElement is not displayed with locator value " + locatorValue + " using locator type " + locatorType)

    def takeScreenshots(self,screenshotName):
        fileName = screenshotName+"__"+(time.strftime("%d_%m_%y_%H_%M_%S"))+".png"
        screenshotDirectory = "../screenshots/"
        screnshootsPath =screenshotDirectory+fileName
        try:
            self.driver.save_screenshot(screnshootsPath)
            self.log.info("screenshot save to path :" + screnshootsPath)
        except:
            self.log.info("screenshot not save")



