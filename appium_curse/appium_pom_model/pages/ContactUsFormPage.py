from appium_curse.appium_pom_model.base.BasePage import BasePage



class ContactForm(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver =driver

    # Locators values in Contact us form
    _contactFromButton = "com.code2lead.kwad:id/ContactUs"  # id
    _pagetitle = "Contact Us form"  # text
    _enterName = "Enter Name"  # text
    _enterEmail = "Enter Email"  # text
    _enterAddress = "Enter Address"  # text
    _enterMobileNumber = "Enter Mobile No"  # text
    _submitButton = "SUBMIT"  # text

    def clickContactFormButton(self):
        self.clickElement(self._contactFromButton, "id")

    def verifyContactPage(self):
        element = self.isDisplayed(self._pagetitle, "text")
        assert element == True

    def enterName(self):
        self.sendText("Juan Ramon",self._enterName,"text")

    def enterEmail(self):
        self.sendText("jrramirezglz@gmail.com",self._enterEmail,"text")

    def enterAddress(self):
        self.sendText("Mexico",self._enterAddress,"text")

    def enterMNumber(self):
        self.sendText("4441213988",self._enterMobileNumber,"text")

    def clickSubmitButton(self):
        self.clickElement(self._submitButton,"text")