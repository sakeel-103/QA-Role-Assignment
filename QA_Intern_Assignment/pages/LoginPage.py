from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.username_field)).send_keys(username)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.password_field)).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))