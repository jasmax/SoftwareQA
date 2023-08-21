import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def navigate_to(self, url):
        self.driver.get(url)

    def search_for(self, keyword):
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.clear()
        search_bar.send_keys(keyword)
        search_bar.send_keys(Keys.ENTER)
        
    def click_full_screen(self):
        full_screen_button = self.driver.find_element(By.ID, "full-clk")
        full_screen_button.click()

class GooglePage(Page):

    def __init__(self, driver):
        super().__init__(driver)


class TimeAndDatePage(Page):

    def __init__(self, driver):
        super().__init__(driver)


def main():
    driver = webdriver.Chrome()

    google_page = GooglePage(driver)
    google_page.navigate_to("https://www.google.com.sg")
    google_page.search_for("Singapore Time")
    google_page.take_screenshot("screen1.png")
    driver.back()

    timeanddate_page = TimeAndDatePage(driver)
    timeanddate_page.navigate_to("https://www.timeanddate.com/worldclock/singapore/singapore")
    timeanddate_page.click_full_screen()
    timeanddate_page.take_screenshot("screen2.png")

    driver.quit()


if __name__ == "__main__":
    main()
