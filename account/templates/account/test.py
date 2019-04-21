import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class TestScript_AFS:
    main()
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-user-media-security=true")
        self.driver = webdriver.Chrome("C:/Users/Jayanth/Desktop/8210projectT1-Sprint-2/venv/chromedriver.exe")

    def test_login(self):

        driver = self.driver
        #to  maximze the chrome

        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        elem = driver.find_element_by_xpath("// *[ @ id =\"myNavbar\"] / ul[2] / li[4] / a / span")
        elem.click()
        time.sleep(1)

        #logging in as a user
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("jtirupathi@unomaha.edu")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("jayanth1995")
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/button")
        elem.click()
        time.sleep(10)


    def teardown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()