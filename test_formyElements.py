from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# Set up ChromeDriver service    
service = ChromeService(executable_path=ChromeDriverManager().install())
# Create a WebDriver instance for Chrome
driver = webdriver.Chrome(service=service)

# Define a test function for the Formy website
def testFormySite():
    # Maximize the browser window
    driver.maximize_window()
    # Open the Formy website
    driver.get("https://formy-project.herokuapp.com/form")
    # Pause execution for 1 second to allow page load
    time.sleep(1) 
    
# Define a test function for testing the input fields (first name and last name)
def testNames():
    # Call the testFormySite function to open the Formy website
    testFormySite()
    # Locate the first name input field by its ID and clear any existing text
    elemFirstName = driver.find_element(By.ID, 'first-name') 
    elemFirstName.clear()
    # Enter test data "Test First Name !@#$%^" into the first name input field
    elemFirstName.send_keys("Test First Name !@#$%^") 
    # Locate the last name input field by its ID and clear any existing text
    elemLastName = driver.find_element(By.ID, 'last-name') 
    elemLastName.clear()
    # Enter test data "Test Last Name !@#$%^" into the last name input field
    elemLastName.send_keys("Test Last Name !@#$%^")
    # Pause execution for 1 second to allow time for the input fields to be populated
    time.sleep(1) 
    
# Define a test function to test the education radio buttons
def testTitle():
    # Call the testFormySite function to open the Formy website
    testFormySite() 
    # Locate the job title input field by its ID and clear any existing text
    elemJobTitle = driver.find_element(By.ID, 'job-title') 
    elemJobTitle.clear()
    # Enter the job title "Software Testing Automation" into the input field
    elemJobTitle.send_keys("Software Testing Automation") 
    # Pause execution for 1 second to allow time for the input field to be populated
    time.sleep(1)
    
# Generic function to test the selection of elements (radio buttons or checkboxes)
def Selection(elements):
    # Open the Formy website and reset the form
    testFormySite()

    # Verify that all elements are initially not selected
    for element in elements:
        assert not element.is_selected()

    # Select the first element
    elements[0].click()
    time.sleep(1)

    # Verify that only the first element is selected
    assert elements[0].is_selected()

    # Verify that other elements are not selected
    for i in range(1, len(elements)):
        assert not elements[i].is_selected()

    # Try to select other elements while the first one is already selected
    for i in range(1, len(elements)):
        elements[i].click()
        time.sleep(1)

        # Verify that other elements are not selected due to multi-selection restriction
        assert not elements[i].is_selected()

    # Verify that the first element is still selected
    assert elements[0].is_selected()

# Test function to verify the education radio button selection
def testEducationSelection():
    radio_buttons = [driver.find_element(By.ID, 'radio-button-1'),
                     driver.find_element(By.ID, 'radio-button-2'),
                     driver.find_element(By.ID, 'radio-button-3')]
    Selection(radio_buttons)

# Test function to verify the gender checkbox selection
def testGenderSelection():
    checkboxes = [driver.find_element(By.ID, 'checkbox-1'),
                  driver.find_element(By.ID, 'checkbox-2'),
                  driver.find_element(By.ID, 'checkbox-3')]
    Selection(checkboxes)

# Define a test function to test the "Years of Experience" dropdown menu
def testYearOfExperience():
        # Call the testFormySite function to open the Formy website
    testFormySite()
        # Locate the "Years of Experience" dropdown menu options by their XPATH and select each one
    elemExperience = driver.find_element(By.XPATH, '//*[@id="select-menu"]/option[2]') 
    elemExperience.click()
        # Pause execution for 1 second to allow time for the change to take effect
    time.sleep(1)
    elemExperience = driver.find_element(By.XPATH, '//*[@id="select-menu"]/option[3]') 
    elemExperience.click()
    time.sleep(1)
    elemExperience = driver.find_element(By.XPATH, '//*[@id="select-menu"]/option[4]') 
    elemExperience.click()
    time.sleep(1)
    elemExperience = driver.find_element(By.XPATH, '//*[@id="select-menu"]/option[5]') 
    elemExperience.click()
    time.sleep(1)
    
# Define a test function to test the date picker
def testDatePicker():
    # Loop over days 1 to 29
    for i in range(1,30):
        # Loop over months 1 to 11 (Note: December is skipped as there are only 11 months in the loop)
        for j in range(1,12):
            # Call the testFormySite function to open the Formy website for each date selection
            testFormySite()
            # Locate the date picker element by its ID
            elemCalendar = driver.find_element(By.ID, 'datepicker')
            # Enter the date "i/j/2023" into the date picker and press RETURN key
            elemCalendar.send_keys("{}/{}/2023".format(i,j), Keys.RETURN)
            # Locate the "Submit" button element by its XPATH
            submitKey = driver.find_element(By.XPATH,"/html/body/div/form/div/div[8]/a" ) 
            # Press RETURN key on the "Submit" button to submit the form  
            submitKey.send_keys(Keys.RETURN)
