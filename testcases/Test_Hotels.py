import pytest
from pages.launchpage import LaunchPage
from utilities.utilities import Utilities
from pages.searchresults import SearchResults
from base.base_driver import BaseDriver
@pytest.mark.usefixtures("setup")
class TestHotels():
    def test_searchHotels(self):
        lp = LaunchPage(self.driver)
        ut = Utilities(self.driver)
        sr = SearchResults(self.driver)
        lp.notificationHandle()
        lp.click_on_hotels()
        ut.selectingCategory()
        lp.select_city()
        ut.selecting_date()
        lp.clickOnRooms()
        ut.no_of_rooms()
        lp.clickOnAdultcount()
        ut.no_of_persons()
        lp.clickOnChildcount()
        ut.no_childerns()
        lp.clickOnApply()
        lp.clickOnsearch()
        ut.hotel_name()
        ut.hotel_prices()





