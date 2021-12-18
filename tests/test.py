from appium import webdriver

from .utils import PATH


desired_caps = dict(
    platformName='Android',
    platformVersion='10',
    automationName='uiautomator2',
    deviceName='Android Emulator',
    app=PATH('app/ApiDemos-debug.apk.zip')
)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


class ModelName:

    def setUpModel(self):
        global driver
        self.driver = driver

    def vertex_A(self):
        pass

    def vertex_B(self):
        pass

    def edge_A(self):
        element = self.driver.find_element_by_accessibility_id('Content')
        element.click()
