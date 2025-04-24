import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.LoginPage import LoginPage
from pages.PIMPage import PIMPage
from pages.AddEmployeePage import AddEmployeePage
from pages.EmployeeListPage import EmployeeListPage
from pages.DashboardPage import DashboardPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-notifications")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10) 

try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("Navigated to login page...")
    assert "login" in driver.current_url.lower(), "Login page did not load correctly"
    print("Login page loaded successfully")
    print("Starting login process...")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    print("Navigating to PIM module...")
    pim_page = PIMPage(driver)
    pim_page.navigate_to_pim()

    print("Adding employees...")
    pim_page.go_to_add_employee()
    add_employee_page = AddEmployeePage(driver)
    employees = [
        ("Avi", "Patel"),
        ("Arya", "Lohani"),
        ("Aditya", "Kumar")
    ]
    for first_name, last_name in employees:
        print(f"Adding employee: {first_name} {last_name}")
        add_employee_page.add_employee(first_name, last_name)
        pim_page.go_to_add_employee()

    print("Verifying employees in the list...")
    employee_list_page = EmployeeListPage(driver)
    pim_page.navigate_to_pim()
    employee_list_page.navigate_to_employee_list()
    for first_name, last_name in employees:
        employee_list_page.verify_employee(first_name, last_name)

    print("Logging out...")
    dashboard_page = DashboardPage(driver)
    dashboard_page.logout()
    print("Workflow completed successfully!")

except Exception as e:
    print(f"Workflow failed: {str(e)}")
finally:
    if 'driver' in locals() and driver:
        print("Closing the browser...")
        driver.quit()