AdNabu QA Automation Assignment


Overview:

This project demonstrates automation of an e-commerce workflow using Selenium + Python.

It covers core QA skills including test design, automation, and reporting.

Features:
Product Search Automation
Add to Cart Validation
Shopify Password Page Handling
Page Object Model (POM) Framework
PyTest Integration

Framework Design:
This project follows a Hybrid Automation Framework:
Selenium WebDriver → UI Automation
PyTest → Test execution
Page Object Model (POM) → Maintainability & reusability

Test Scenario Covered:
Open Shopify store
Enter password (AdnabuQA)
Search for product
Select product
Add to cart
Validate cart

Framework Components:

Base Page:
Common reusable methods
click(), send_keys(), waits

Page Classes:
login_page.py → Password handling
search_page.py → Product search
product_page.py → Add to cart

Test Layer
Contains test cases using PyTest

Driver page
Handles browser initialization

Metric                 Value

Total Test Cases       12
Passed                 11
Failed                 1
Pass %                91.6%

Setup instryctions:
1.Clone repository
2.Install dependencies
3.Install chrome driver

To Run all the tests - pytest AUTOMATION/tests -v

-->Core functionalities are properly automated
-->Frameworks is scalable and maintainable.

