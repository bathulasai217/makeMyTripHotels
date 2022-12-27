import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
class LaunchPage(BaseDriver):
    txt_notificationhandle_xpath = "//iframe[@title = 'notification-frame-~55854522']"
    txt_notificationclose_xpath = "//i[@class = 'wewidgeticon we_close']"
    txt_click_hotel_xpath = "//div[@class='bgGradient webpSupport landingPageBg']"
    txt_categories_xpath = "//ul[@class='makeFlex font12']/li/div/a"

    txt_city_css = "div[class='hsw_inputBox selectHtlCity  ']"
    txt_entercity_xpath = "//input[@placeholder='Enter city/ Hotel/ Area/ Building']"
    txt_cityname = "bengalore"
    txt_select_city_css = "li[id=react-autowhatever-1-section-0-item-0]"

    txt_month_css = "div.DayPicker-Caption>div"
    txt_days_css = "div.DayPicker-Body>div>div"
    txt_attribute = "aria-label"
    txt_attribute_Value_cehckin= "Sun Feb 05 2023"
    txt_attribute_value_checkout = "Mon Feb 06 2023"
    txt_clicknext_css = "span[class='DayPicker-NavButton DayPicker-NavButton--next']"

    txt_rooms_xpath = "//span[contains(@data-testid,'room_count')]"
    txt_norooms_css = "ul.gstSlct__list>li"

    txt_click_adult_xpath = "//span[contains(@data-testid,'adult_count')]"
    txt_click_childc_xpath = "//span[contains(@data-testid,'children_count')]"
    txt_nfchildrens_css = "ul.gstSlct__list>li"
    txt_apply_xpath = "//button[@class = 'primaryBtn btnApplyNew pushRight capText']"
    txt_search_xpath = "//button[@id='hsw_search_button']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    def notificationHandle(self):
        try:
            self.switch_to_frame(self.findelement(By.XPATH,self.txt_notificationhandle_xpath))
            self.wait_presence_of_element(By.XPATH,self.txt_notificationclose_xpath).click()
        except:
            pass
    def click_on_hotels(self):
        click_on = self.findelement(By.XPATH,self.txt_click_hotel_xpath).click()
        return click_on
    def categories(self):
        elements = self.findelements(By.XPATH,self.txt_categories_xpath)
        return elements
    def select_city(self):
        self.findelement(By.CSS_SELECTOR,self.txt_city_css).click()
        self.findelement(By.XPATH,self.txt_entercity_xpath).send_keys(self.txt_cityname)
        time.sleep(2)
        self.wait_presence_of_element(By.CSS_SELECTOR,self.txt_select_city_css).click()
    def select_month(self):
        month = self.findelement(By.CSS_SELECTOR,self.txt_month_css).text
        return month
    def select_days(self):
        days = self.wait_for_presence_all_elements(By.CSS_SELECTOR,self.txt_days_css)
        return days
    def click_onnext(self):
        nextclick = self.findelement(By.CSS_SELECTOR,self.txt_clicknext_css).click()
        return nextclick


    def clickOnRooms(self):
        cr = self.findelement(By.XPATH,self.txt_rooms_xpath).click()
        return cr
    def no_of_rooms(self):
        nor = self.wait_for_presence_all_elements(By.CSS_SELECTOR,self.txt_norooms_css)
        return nor
    def no_of_person(self):
        nop = self.findelements(By.CSS_SELECTOR,self.txt_nfchildrens_css)
        return nop
    def no_of_childs(self):
        noc = self.findelements(By.CSS_SELECTOR,self.txt_nfchildrens_css)
        return noc

    def clickOnAdultcount(self):
        ad = self.wait_presence_of_element(By.XPATH,self.txt_click_adult_xpath).click()
        return ad
    def clickOnChildcount(self):
        cc = self.findelement(By.XPATH,self.txt_click_childc_xpath).click()
        return cc
    def clickOnsearch(self):
        ele = self.findelement(By.XPATH,self.txt_search_xpath).click()
        time.sleep(5)
        return ele
    def clickOnApply(self):
        ele = self.findelement(By.XPATH,self.txt_apply_xpath).click()
        return ele






