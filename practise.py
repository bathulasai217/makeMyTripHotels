import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
serv_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.makemytrip.com/")
driver.maximize_window()
try:
    driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title = 'notification-frame-~55854522']"))
    driver.find_element(By.XPATH,"//i[@class = 'wewidgeticon we_close']").click()
except:
    pass
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='bgGradient webpSupport landingPageBg']").click()
elements = driver.find_elements(By.XPATH,"//ul[@class='makeFlex font12']/li/div/a")
for ele in elements:
    if ele.text == "Hotels":
        ele.click()
driver.find_element(By.CSS_SELECTOR,"div[class='hsw_inputBox selectHtlCity  ']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter city/ Hotel/ Area/ Building']").send_keys("bengalore")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"li[id=react-autowhatever-1-section-0-item-0]").click()
for c in range(12):
    time.sleep(2)
    month = driver.find_element(By.CSS_SELECTOR, "div.DayPicker-Caption>div").text
    if month == "January2023":
        days = driver.find_elements(By.CSS_SELECTOR, "div.DayPicker-Body>div>div")
        for day in days:
            if day.get_attribute("aria-label") == "Sun Feb 05 2023":
                day.click()
                time.sleep(2)
            #checkout = driver.find_element(By.XPATH,"//div[@class = 'calHeading makeFlex']/div[3]").text
            if day.get_attribute("aria-label") == "Mon Feb 06 2023":
                day.click()
                break

        break
    else:
        driver.find_element(By.CSS_SELECTOR,"span[class='DayPicker-NavButton DayPicker-NavButton--next']").click()
driver.find_element(By.XPATH,"//span[contains(@data-testid,'room_count')]").click()
NoOfRooms = driver.find_elements(By.CSS_SELECTOR,"ul.gstSlct__list>li")
for rooms in NoOfRooms:
    if rooms.text == "02":
        time.sleep(1)
        rooms.click()
        break
driver.find_element(By.XPATH,"//span[contains(@data-testid,'adult_count')]").click()
NoOfPersons = driver.find_elements(By.CSS_SELECTOR,"ul.gstSlct__list>li")
for persons in NoOfPersons:
    if persons.text == "02":
        persons.click()
        break
driver.find_element(By.XPATH,"//span[contains(@data-testid,'children_count')]").click()
NoOfChildrens = driver.find_elements(By.CSS_SELECTOR,"ul.gstSlct__list>li")
for children in NoOfChildrens:
    if children.text == "00":
        children.click()
        break
driver.find_element(By.XPATH,"//button[@class='primaryBtn btnApplyNew pushRight capText']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"button#hsw_search_button").click()
#driver.find_element(By.CSS_SELECTOR,"p.slctTrpTyp__selected").click()
# driver.find_element(By.CSS_SELECTOR,"div[id='listingView'] li:nth-child(1)").click()
# time.sleep(20)
# driver.find_element(By.CSS_SELECTOR,"div.slctTrpTyp").click()
# ele = driver.find_elements(By.CSS_SELECTOR,"div.slctTrpTyp>ul>li")
# for el in ele:
#     print(el.text)
hotels = driver.find_elements(By.CSS_SELECTOR,"p#hlistpg_hotel_name")
for i in hotels:
    time.sleep(1)
    print(i.text)
prices = driver.find_elements(By.CSS_SELECTOR,"p#hlistpg_hotel_shown_price")
for i in prices:
    time.sleep(1)
    print(i.text)


