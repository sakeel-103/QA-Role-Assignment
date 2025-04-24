##  ===  QA Intern Assignment 2025 - Automation Project =======

Overview

```bash
This repository contains the automation project submitted for the QA Intern Assignment 2025. The project automates testing of the Orange HRM web application (https://opensource-demo.orangehrmlive.com/web/index.php/auth/login) using Selenium with Python, following the Page Object Model (POM) design pattern. It includes both a main automation workflow and an optional bonus script for login verification.4

```

## ===  Purpose ===== 

```bash

Automate the login flow, navigation to the PIM module, adding employees, verifying employees in the employee list, and logging out.
Provide a bonus script to verify the login functionality with valid credentials.
Document test cases and bugs as part of the deliverable.

```

##  ======  Project Structure =======  

```bash
qa_intern_assignment/
├── pages/
│   ├── LoginPage.py         
│   ├── PIMPage.py           
│   ├── AddEmployeePage.py   
│   ├── EmployeeListPage.py  
│   └── DashboardPage.py     
├── tests/
│   ├── test_workflow.py     
│   └── login_verification.py 
└── README.md                

```

##   ===  Prerequisites ======

- To run this project, ensure the following are installed on your system: -
1. Install python
2. Chrome Browser
3. Dependencies
   - pip install selenium webdriver-manager

##  ======   How to Run the project  =======

Step: -

1. Clone the Repository:
   - 

2. move to the project path
   - cd cd qa_intern_assignment

3. Install Dependencies: -
   - pip install -r requirements.txt
   - pip install selenium
   - pip install webdriver-manager

## 4. Verify your Chrome Binary Path: -

   - Ensure Google Chrome is installed. The script uses the path on the login_Verification.py file.

   1. To run the login_verification.py  (Optional part- script test-)
    - move to logi_verification.py file and add you chrome.exe file
      - here 
        ```bash
          chrome_options.binary_location = "__" 
         ```

    - Tu run the file -
    - Move to the tests folder - cd tests
   - run the command =    " python login_verification.py "

##   2. To run the Automation Testing

     1. move out from the testfolder 

     here - Omnify\QA_Intern_Assignment\tests>     

     run the command - " python tests\test_workflow.py "


##   =============   Demo Video ==========================



   Video -   <video controls src="Omnify.mp4" title="Title"></video>




##  ==============================  END ===============================