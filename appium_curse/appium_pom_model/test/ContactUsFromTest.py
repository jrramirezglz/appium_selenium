import unittest
import pytest
from appium_curse.appium_pom_model.pages.ContactUsFormPage import ContactForm

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class ContactFormTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.ramon(order=2)
    def test_openContactForm(self):
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()

    @pytest.mark.ramon(order=1)
    def test_enterData(self):
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()