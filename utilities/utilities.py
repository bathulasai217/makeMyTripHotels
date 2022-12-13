import time
from pages.launchpage import LaunchPage
from base.base_driver import BaseDriver
class Utilities(BaseDriver):

    def selectingCategory(self):
        cate = LaunchPage(self.driver)
        for ele in cate.categories():
            if ele.text == "Hotels":
                ele.click()
    def selecting_date(self):
        ct = LaunchPage(self.driver)
        for c in range(12):
            time.sleep(1)
            if ct.select_month() == "January2023":
                ct.select_days()
                for day in ct.select_days():
                    if day.get_attribute(ct.txt_attribute) == ct.txt_attribute_Value_cehckin:
                        day.click()
                        time.sleep(2)
                    if day.get_attribute(ct.txt_attribute) == ct.txt_attribute_value_checkout:
                        day.click()
                        break
                break
            else:
                ct.click_onnext()
    def no_of_rooms(self):
        cate = LaunchPage(self.driver)
        for ele in cate.no_of_rooms():
            print(ele.text)
            time.sleep(1)
            if ele.text == "02":

                ele.click()
                break
    def no_of_persons(self):
        cate = LaunchPage(self.driver)
        for ele in cate.no_of_person():
            if ele.text == "02":
                ele.click()
                break
    def no_childerns(self):
        cate = LaunchPage(self.driver)
        for ele in cate.no_of_childs():
            if ele.text == "00":
                ele.click()
                break



