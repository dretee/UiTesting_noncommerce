# UiTesting_noncommerce
UI TESTING FOR THE WEBPAGE OF A COMMERCE SITE
I understand your concern. Here's a more detailed README.md for your nopCommerce Backend Automation project:

# nopCommerce Backend Automation

Welcome to the nopCommerce Backend Automation project. This repository contains a comprehensive suite of automated tests designed to validate the functionality, reliability, and performance of the backend of the nopCommerce eCommerce platform.

## Project Overview

nopCommerce is a popular and open-source eCommerce solution utilized by online retailers worldwide. This project is dedicated to automating tests for various backend features and functionalities, ensuring they meet the highest quality standards and remain stable across different scenarios.

## Key Features Tested

### 1. Adding Customers

- **Description:** This suite of tests covers the end-to-end process of adding new customers to the nopCommerce platform. It includes filling in customer details, form submission, and validation of successful customer creation.
- **Test Scenarios:**
  - Valid customer creation with all required details.
  - Handling duplicate customer creation.
  - Verification of correct error messages for invalid inputs.

### 2. Customer Search

- **Description:** A comprehensive set of tests that validate the customer search functionality, enabling administrators to locate customers efficiently based on various criteria.
- **Test Scenarios:**
  - Searching customers by email address.
  - Searching customers by company name.
  - Searching customers by first and last name.
  - Handling edge cases and non-existent customer scenarios.

### 3. Data-Driven Testing for Login

- **Description:** This suite focuses on data-driven testing for the login process, allowing testing with different user credentials and evaluating the system's behavior in response to various login attempts.
- **Test Scenarios:**
  - Successful logins with valid credentials.
  - Handling failed login attempts with incorrect credentials.
  - Testing login with a range of user roles and permissions.

## Prerequisites

Before running the tests, ensure you have the following prerequisites in place:

- Python (3.6+)
- Selenium WebDriver
- pytest
- Chrome, Firefox, Edge, or IE WebDriver (based on your choice)
- Excel file for data-driven testing (if applicable)

## Running Tests

To execute the tests, utilize the following commands:

- To run tests with a specific browser (e.g., Chrome):

  ```bash
  pytest -v -s testCases/test_AddCustomer.py --browser chrome
  ```

- To generate detailed HTML reports for the tests:

  ```bash
  pytest -v -s --html=Reports\reports.html testCases/test_AddCustomer.py --browser chrome
  ```

## Reporting

The project generates comprehensive HTML reports in the "Reports" directory. These reports provide detailed insights into test results, including successes, failures, and errors. Additionally, they help pinpoint issues and facilitate efficient debugging.

## Contributors

I'm a dedicated software quality engineer with a strong enthusiasm for enhancing my expertise in UI testing automation. 
You can get in touch with me for potential opportunities at my email address: uyahanthony008@gmail.com.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for detailed licensing information.

## Feedback and Contributions

We welcome contributions and feedback from the open-source community. If you encounter issues, have suggestions, or wish to contribute enhancements, please feel free to open GitHub issues or create pull requests.

Thank you for your interest in the nopCommerce Backend Automation project!


In this enhanced README, I've provided more detailed information about the test suites, test scenarios, and their significance.
Additionally, I've added a section for contributors, emphasizing contributions and feedback from the open-source community.
