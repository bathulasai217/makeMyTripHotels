import time
from itertools import combinations

from pages.launchpage import LaunchPage
from base.base_driver import BaseDriver
from pages.searchresults import SearchResults
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
    # def tripType(self):
    #     sr = SearchResults(self.driver)
    #     for type in sr.trip_types():
    #         time.sleep(1)
    #         if type.text == "Business":
    #             type.click()
    #             break
    #     time.sleep(5)
    def hotel_name(self):
        hotelnames = []
        sr = SearchResults(self.driver)
        for i in sr.hotelNames():
            time.sleep(2)
            hotelnames.append(i.text)

    def hotel_prices(self):
        hotelprices = []
        sr = SearchResults(self.driver)
        for i in sr.hotelPrices():
            time.sleep(1)
            hotelprices.append(i.text)
        print(hotelprices)
        for i in range(len(hotelprices)):
            hotelprices[i] = hotelprices[i].strip("₹")
            hotelprices[i] = hotelprices[i].strip(" ")
            hotelprices[i] = hotelprices[i].replace(",","")
            hotelprices[i] = int(hotelprices[i])

        print(hotelprices)

        result = combinations(hotelprices, 2)
        b = list(result)
        print(b, "\n")
        c = {}
        for i in b:
            and_op = i[0] & i[1]
            temp_dict = {}
            if i not in temp_dict:
                c[i] = and_op
        print(c, "\n")
        d = {}
        for i in range(len(b) - 1):
            for j in range(i + 1, len(b)):
                and_sum = c[b[i]] + c[b[j]]
                a = (b[i], b[j])
                d[a] = and_sum
        sum_values = sorted(list(d.values()))
        max_sum = sum_values[::-1][0]
        comb_count = 0
        for key, value in d.items():
            key = list(key)
            if value == max_sum:
                print(key[0], key[1], value)
                comb_count += 1
        print("Total maximum sum combinations possibles:", comb_count)
        print("Maximum and sum:", max_sum)










