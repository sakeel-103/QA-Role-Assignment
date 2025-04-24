from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.NAME, "firstName")
        self.last_name_field = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")

    def add_employee(self, first_name, last_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name_field)).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.save_button).click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("viewPersonalDetails"))