import threading
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys






def linked_homepage():
        basrurl="https://www.google.com/"
        driver = webdriver.Chrome(r"C:\SeleniumIEDriver\chromedriver.exe")
        driver.get(basrurl)
        driver.maximize_window()
        driver.find_element_by_name("q").send_keys("LinkedIn login")
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        driver.find_element_by_partial_link_text("LinkedIn Login").click()
        driver.find_element_by_id("username").send_keys("SreenivasanMaster")
        time.sleep(5)
        print(driver.title)
        print(driver.current_url)
        driver.close()



t1 = threading.Thread(target=linked_homepage)

t1.start()
time.sleep(10)


