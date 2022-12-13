import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service


@pytest.fixture(scope="class")
def setup(request):
    serv_obj = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=serv_obj)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


