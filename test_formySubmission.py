from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class WebFormTest:
    def __init__(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://formy-project.herokuapp.com/form")
        assert "Formy" in self.driver.title

    def test_form_submission(self):
        # Enter valid data in all the form fields.
        first_name = self.driver.find_element(By.ID, 'first-name')
        last_name = self.driver.find_element(By.ID, 'last-name')
        job_title = self.driver.find_element(By.ID, 'job-title')
        education = self.driver.find_element(By.ID, 'radio-button-1')
        gender = self.driver.find_element(By.ID, 'checkbox-1')
        years_of_experience = self.driver.find_element(By.ID, 'select-menu')
        date_picker = self.driver.find_element(By.ID, 'datepicker')

        first_name.send_keys("John")
        last_name.send_keys("Doe")
        job_title.send_keys("Software Engineer")
        education.click()
        gender.click()
        years_of_experience.send_keys("3-5 years")
        date_picker.send_keys("09/04/2023")

        # Click on the "Submit" button.
        submit_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Submit')]")
        submit_button.click()

        # Assert that the form submission is successful by verifying the success message or a page redirect.
        success_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success']")
        assert success_message.is_displayed()

    def test_required_fields_validation(self):
        # Leave one or more required fields empty.
        first_name = self.driver.find_element(By.ID, 'first-name')
        first_name.clear()

        # Click on the "Submit" button.
        submit_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Submit')]")
        submit_button.click()

        # Assert that appropriate error messages are displayed for the empty fields.
        error_message = self.driver.find_element(By.XPATH, "//span[contains(text(),'This field is required.')]")
        assert error_message.is_displayed()

# Run the test cases
web_form_test = WebFormTest()
web_form_test.test_form_submission()
web_form_test.test_required_fields_validation()
