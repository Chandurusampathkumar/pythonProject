from selenium import webdriver
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Chrome(r"C:\SeleniumIEDriver\chromedriver.exe")
    return driver