from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmployeeListPage:
    def __init__(self, driver):
        self.driver = driver
        self.employee_rows = (By.XPATH, "//div[@role='row']//div[@role='cell']")

    def navigate_to_employee_list(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Employee List']"))).click()

    def verify_employee(self, first_name, last_name):
        full_name = f"{first_name} {last_name}"
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(self.employee_rows))
        rows = self.driver.find_elements(*self.employee_rows)
        if not rows:
            print(f"No employees found in the list for {full_name}")
            return False
    
        print(f"Total cells found: {len(rows)}")
        for i, cell in enumerate(rows):
            print(f"Cell {i}: {cell.text}")
        
        found = False
        num_cells_per_row = 8  
        for i in range(0, len(rows), num_cells_per_row):
            row_cells = rows[i:i + num_cells_per_row]
            if len(row_cells) >= 3:  
                row_first_name = row_cells[1].text  
                row_last_name = row_cells[2].text   
                if f"{row_first_name} {row_last_name}".strip() == full_name:
                    print(f"Name Verified: {full_name}")
                    found = True
                    break
        if not found:
            print(f"Employee {full_name} not found in the list")
        return found