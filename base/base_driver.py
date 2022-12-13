from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver():
    def __init__(self,driver):
        self.driver =driver

    def wait_for_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element
    def findelement(self,locator_type,locator):
        self.driver.implicitly_wait(20)
        fd = self.driver.find_element(locator_type,locator)
        return fd
    def findelements(self,locatortype,locator):
        fds = self.driver.find_elements(locatortype,locator)
        return fds
    def switch_to_frame(self,locator):
        sw = self.driver.switch_to.frame(locator)
        return sw
    def switch_to_parent(self):
        swp = self.driver.switch_to.parent_frame()
        return swp
    def wait_presence_of_element(self,locator_type, locator):
        wait = WebDriverWait(self.driver,10)
        ele =wait.until(EC.presence_of_element_located((locator_type, locator)))
        return ele
    def save_screenshot(self,location):
        sc = self.save_screenshot(location)
        return sc
    def wait_for_presence_all_elements(self,locator_type, locator):
        wait = WebDriverWait(self.driver,10)
        ele = wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return ele
