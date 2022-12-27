import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
class SearchResults(BaseDriver):
    txt_trip_css = "p.slctTrpTyp__selected"
    txt_triptype_css = "div.slctTrpTyp>ul>li"
    txt_hotelNames_css = "p#hlistpg_hotel_name"
    txt_hotelPrices_css = "p#hlistpg_hotel_shown_price"
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    # def select_trip(self):
    #     self.findelement(By.CSS_SELECTOR,self.txt_trip_css).click()
    # def trip_types(self):
    #     ele = self.findelements(By.CSS_SELECTOR,self.txt_triptype_css)
    #     return ele
    def hotelNames(self):
        ht = self.wait_for_presence_all_elements(By.CSS_SELECTOR,self.txt_hotelNames_css)
        return ht
    def hotelPrices(self):
        pri = self.wait_for_presence_all_elements(By.CSS_SELECTOR,self.txt_hotelPrices_css)
        return pri



