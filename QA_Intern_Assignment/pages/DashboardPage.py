from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_dropdown = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        self.logout_option = (By.XPATH, "//a[text()='Logout']")

    def logout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.profile_dropdown)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_option)).click()