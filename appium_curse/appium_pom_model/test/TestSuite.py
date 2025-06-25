#import the files
import unittest
#from appium_curse.appium_pom_model.test.LoginTest import LoginTest
from appium_curse.appium_pom_model.test.ContactUsFromTest import ContactFormTest

#2 create the object opf the class using unittest
#lgt = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)

# 3 create the TestSuite
#regressionTest = unittest.TestSuite(cf, lgt)
regressionTest = unittest.TestSuite(cf)

#call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)