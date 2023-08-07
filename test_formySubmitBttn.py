from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class TestButtonNavigation:
    def setup_method(self):
        # Set up ChromeDriver service
        service = webdriver.chrome.service.Service(ChromeDriverManager().install())

        # Create a WebDriver instance for Chrome
        self.driver = webdriver.Chrome(service=service)

    def teardown_method(self):
        # Close the browser after each test
        self.driver.quit()

    def test_button_navigation(self):
        # Open the web page with the button to be tested
        self.driver.get("https://formy-project.herokuapp.com/form")

        # Find the button element by its class name
        button = self.driver.find_element(By.CLASS_NAME, "btn-primary")

        # Click the button
        button.click()

        # Get the current URL after clicking the button
        current_url = self.driver.current_url

        # Assert that the current URL is different from the initial page
        assert current_url != "https://formy-project.herokuapp.com/form"

        # Wait for a moment to see the result (optional)
        time.sleep(2)
