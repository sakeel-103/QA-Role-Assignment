from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.add_employee_tab = (By.XPATH, "//a[text()='Add Employee']")

    def navigate_to_pim(self):
        pim_menu = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.pim_menu))
        ActionChains(self.driver).move_to_element(pim_menu).click().perform()

    def go_to_add_employee(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.add_employee_tab)).click()