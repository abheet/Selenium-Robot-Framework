**Title:** Page Object Model Implementation with Selenium-Python (Pytest) for Webpage Automation

**Author:** Abheet Singh Jamwal

## Introduction

This repository showcases a Page Object Model (POM) implementation using Selenium-Python and Pytest for automating web page interactions. It includes test scripts for validating login, signup, and forgot password functionalities.

## Prerequisites

* Python 2.x or 3.x (Ensure compatibility with your chosen Selenium version)
* Virtual environment (Recommended for isolated package management)

## Installation

**1. Clone the Repository**

```bash
git clone https://github.com/your-username/SeleniumScript.git
```

**2. Set Up a Virtual Environment (Optional but Recommended)**

[Instructions for creating a virtual environment: Refer to official documentation for your operating system or virtual environment tool.]

**3. Install Dependencies**

```bash
cd SeleniumScript  # Navigate to the project directory
pip install -r requirements.txt  # Install required packages from the requirements file
```

**4. Activate Virtual Environment (if applicable)**

Follow the instructions specific to your chosen virtual environment manager (e.g., `source venv/bin/activate` for virtualenv).

## Running Tests

**1. Navigate to the Project Directory**

```bash
cd SeleniumScript
```

**2. Running All Test Suites**

```bash
pytest  # This command detects all tests in the "tests" folder and executes them
```

**3. Running Specific Test Files**

```bash
pytest -k <test_file_name>  # Example: pytest -k test_login
```

**4. Running Specific Test Cases within a File**

```bash
pytest -k <test_file_name>::<test_case_method_name>  # Example: pytest -k test_signup::test_valid_signup
```

**5. Running Tests by Marker (lowest, medium, highest)**

```bash
pytest -k <test_file_name> -m <marker>  # Example: pytest -k test_forgot_password -m lowest
```

**6. Generating HTML Reports**

```bash
pytest -k <test_file_name> --html=report.html  # Example: pytest -k test_login --html=login_report.html
```

**7. Parallel Test Execution (Optional)**

```bash
pytest -n <number_of_workers>  # Example: pytest -n 4  (Replace 4 with the desired number of worker processes)
```

**Note:** Replace `<test_file_name>` with the actual test file name (e.g., `test_login.py`) and `<test_case_method_name>` with the specific test case method name within the file.

## Additional Notes

* Refer to the `requirements.txt` file for the exact versions of the required packages.
* Ensure compatibility between your chosen Selenium version and the targeted web browser.
* Consider using dedicated test reporting frameworks like Allure or ReportLab for more comprehensive reports.
