import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
class SearchResults():
    def __init__(self,driver):
        super.__init__(driver)
        self.driver = driver
