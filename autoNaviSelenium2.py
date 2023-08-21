from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GooglePage(object):
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self):
        self.driver.save_screenshot("screenshot01.png")
        self.driver.back()

    def navigate_to(self, url):
        self.driver.get(url)

    def search_for(self, keyword):
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.send_keys(keyword)
        search_bar.send_keys(Keys.ENTER)


class TimeAndDatePage(object):
    def __init__(self, driver):
        self.driver = driver

    def click_full_screen(self):
        full_screen_button = self.driver.find_element(By.ID, "full-clk")
        full_screen_button.click()

        self.driver.save_screenshot("screenshot02.png")
        
    def navigate_to(self, url):
        self.driver.get(url)


def main():
    driver = webdriver.Chrome()

    google_page = GooglePage(driver)
    google_page.navigate_to("https://www.google.com.sg")
    google_page.search_for("Singapore Time")
    google_page.take_screenshot()
    

    timeanddate_page = TimeAndDatePage(driver)
    timeanddate_page.navigate_to("https://www.timeanddate.com/worldclock/singapore/singapore")
    timeanddate_page.click_full_screen()
    
    driver.quit()


if __name__ == "__main__":
    main()