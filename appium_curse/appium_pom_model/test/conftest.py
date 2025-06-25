import time
import pytest
from appium_curse.appium_pom_model.base.DriverClass import Driver


@pytest.fixture(scope="class")
def beforeClass(request):
    print("Before class")
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print("After class")

@pytest.fixture(scope="session")
def beforeMethod():
    print("Before Method")
    yield
    print("After Method")