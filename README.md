# 🛒 E-Commerce Web Application — Functional & Manual Testing Portfolio

[![Test Suite](https://img.shields.io/badge/Test%20Cases-30%20Executed-blue.svg)](Test_Cases.md)
[![Pass Rate](https://img.shields.io/badge/Pass%20Rate-90.00%25-brightgreen.svg)](Test_Execution_Report.md)
[![Defects Logged](https://img.shields.io/badge/Defects%20Logged-6%20Bugs-red.svg)](Bug_Reports.md)
[![Methodology](https://img.shields.io/badge/Methodology-IEEE%20829%20%7C%20ECP%20%7C%20BVA-orange.svg)](Test_Plan.md)
[![Documentation](https://img.shields.io/badge/Deliverables-Excel%20%7C%20PDF%20%7C%20Markdown-teal.svg)](#repository-artifacts)

A comprehensive, industry-grade **Manual QA & Functional Testing Portfolio Project** evaluating the end-to-end shopping journey of the [SauceDemo](https://www.saucedemo.com/) e-commerce web application.

---

## 📌 Project Overview

This repository demonstrates practical application of core software testing methodologies across a live e-commerce web platform. Testing spans user authentication, product catalog browsing, sorting algorithms, cart state management, checkout form validation, financial tax calculations, and post-order confirmation.

### Application Under Test (AUT)
- **Target Application:** [SauceDemo Web App](https://www.saucedemo.com/)
- **Application Type:** Responsive Single-Page E-Commerce Web Application (React)
- **Test Environment:** Windows 11 Pro, Google Chrome (v122+), Mozilla Firefox, Microsoft Edge
- **Primary Test Accounts:** `standard_user`, `locked_out_user`, `problem_user` (Password: `secret_sauce`)

---

## 📁 Repository Artifacts

| File Name | Format | Description |
|:---|:---:|:---|
| **[README.md](README.md)** | Markdown | Master project portfolio overview, methodology, metrics, and resume bullets. |
| **[Test_Plan.md](Test_Plan.md)** | Markdown | Full IEEE 829-compliant Test Plan (Scope, Strategy, Environments, Exit Criteria). |
| **[Test_Plan.xlsx](Test_Plan.xlsx)** | Excel | Formatted spreadsheet version of the Test Plan with visual hierarchy. |
| **[Test_Cases.md](Test_Cases.md)** | Markdown | Complete suite of 30 test cases with preconditions, steps, test data, and results. |
| **[Test_Cases.xlsx](Test_Cases.xlsx)** | Excel | Formatted test case workbook with Pass/Fail color highlighting and severity tags. |
| **[Bug_Reports.md](Bug_Reports.md)** | Markdown | 6 formal defect reports with steps to reproduce, expected vs. actual, severity & priority. |
| **[Bug_Reports.xlsx](Bug_Reports.xlsx)** | Excel | Jira-style bug tracking matrix for defects discovered during execution. |
| **[Test_Execution_Report.md](Test_Execution_Report.md)** | Markdown | Test summary report, pass rate calculations, module metrics, and sign-off verdict. |
| **[Test_Execution_Report.pdf](Test_Execution_Report.pdf)** | PDF | Executive-ready PDF report generated for stakeholder presentation. |
| **[generate_sheets_and_pdf.py](generate_sheets_and_pdf.py)** | Python | Automated generation script for reproducible Excel workbooks and PDF reporting. |

---

## 🎯 Testing Methodologies & Techniques Applied

### 1. Equivalence Class Partitioning (ECP)
- **Login Credentials:**
  - *Valid Partition:* `standard_user` + `secret_sauce` (Routes to catalog).
  - *Invalid Partition:* Invalid passwords, unregistered usernames (Triggers error notification).
  - *Restricted Partition:* `locked_out_user` (Validates account lockout logic).
- **Checkout Customer Form:**
  - Partitioned Postal Code into valid alphanumeric codes (`90210`, `L4Y 1S1`), empty fields, and special character strings (`!@#$%^&*()`).

### 2. Boundary Value Analysis (BVA)
- **Shopping Cart Quantities:**
  - Evaluated lower boundary of cart items: **0 items** (revealed critical business logic defect `BUG-02` where empty cart checkout is permitted) vs. **1 item** (standard checkout allowed).
- **Product Sorting:**
  - Validated price boundaries: Minimum item price ($7.99 for Sauce Labs Onesie) through Maximum item price ($49.99 for Fleece Jacket).

### 3. Financial & Tax Calculation Verification
- Manually calculated expected sales tax and verified rounding rules to ensure financial accuracy:
  $$\text{Item Total} = \sum (\text{Price}_i)$$
  $$\text{Sales Tax} = \text{Round}(\text{Item Total} \times 0.08, 2)$$
  $$\text{Grand Total} = \text{Item Total} + \text{Sales Tax}$$
- Verified with multi-item scenarios (e.g., $29.99 + $9.99 = $39.98 item subtotal; Tax at 8.00% = $3.20; Total = $43.18).

### 4. Negative & Usability Testing
- Verified input masking on password fields (`type="password"`).
- Verified field validation when mandatory inputs (First Name, Last Name, Zip Code) are omitted.
- Tested persistence of cart items across page refreshes (`F5`).
- Validated direct URL access security (accessing `/inventory.html` without active session redirects to login).

---

## 📊 Test Execution Summary & KPIs

$$\text{Pass Rate} = \frac{\text{Passed}}{\text{Passed} + \text{Failed}} \times 100 = \frac{27}{27 + 3} \times 100 = 90.00\%$$

| Test Metric | Value | Target Benchmark |
|:---|:---:|:---:|
| **Total Test Cases Planned** | 30 | 100% |
| **Total Test Cases Executed** | 30 | 100% |
| **Test Cases Passed** | 27 | ≥ 85.0% |
| **Test Cases Failed** | 3 | ≤ 15.0% |
| **Blocked Test Cases** | 0 | 0 |
| **Defects Identified & Logged** | 6 | Jira / Excel Tracked |
| **Overall Quality Pass Rate** | **90.00%** | **Conditional Pass** |

### Module-Wise Pass Rate Distribution
```
Authentication & Session:       [====================] 100% (8/8 Passed)
Product Catalog & Sorting:      [=================...]  85.7% (6/7 Passed)
Shopping Cart Operations:       [====================] 100% (6/6 Passed)
Checkout Step 1 (Info Form):    [============........]  60.0% (3/5 Passed)
Checkout Step 2 (Price & Tax):  [====================] 100% (2/2 Passed)
Order Confirmation & Reset:     [====================] 100% (2/2 Passed)
```

---

## 🐛 Key Defects Identified

| Bug ID | Severity | Module | Summary | Expected Behavior |
|:---:|:---:|:---|:---|:---|
| **BUG-01** | Medium | Catalog | Missing product search functionality | Search bar should allow keyword filtering of items |
| **BUG-02** | High | Cart / Checkout | Checkout allowed with 0 items in cart | Checkout button should be disabled when cart is empty |
| **BUG-03** | Medium | Checkout Step 1 | Postal Code accepts special characters (`!@#$%`) | Field should validate postal format via regex |
| **BUG-04** | High | Cart | "Remove" button fails in `problem_user` mode | Item should be removed from cart and badge decremented |
| **BUG-05** | Low | Catalog | Broken product thumbnails show 404 dog photo | Each product should render its genuine thumbnail photo |
| **BUG-06** | Critical | Checkout Step 1 | Last Name field is unresponsive in `problem_user` | Field must accept text and allow order completion |

---

## 💼 Resume Bullet Points

You can adapt these bullet points directly into your QA / Software Tester resume:

```markdown
• Designed and executed an end-to-end manual test suite of 30 test cases for an e-commerce platform covering authentication, product catalog, cart operations, and multi-step checkout workflows.
• Applied Equivalence Class Partitioning (ECP) and Boundary Value Analysis (BVA) to validate form inputs, boundary conditions, and error-handling mechanisms.
• Logged and tracked 6 detailed defect reports following IEEE/Jira standards, specifying reproduction steps, severity, priority, expected vs. actual outcomes, and visual evidence.
• Performed mathematical verification of financial computations, confirming sales tax calculations (8.00%) and subtotal summation with 100% arithmetic accuracy.
• Authored comprehensive QA documentation including Master Test Plan (IEEE 829), Requirements Traceability Matrix (RTM), and Executive Test Execution Summary Reports.
```

---

## 💡 Common Interview Questions & Talking Points

### Q1: "Walk me through how you planned your testing for this e-commerce project."
> *"I started by analyzing the user journey from login to order confirmation. I drafted an IEEE 829-compliant Test Plan covering 6 core modules. I created 30 test cases incorporating positive, negative, and boundary scenarios. I executed the tests across multiple browser environments, tracked test metrics, and logged genuine defects like empty-cart checkout and lack of zip code sanitization."*

### Q2: "What was the most critical defect you discovered?"
> *"I identified a high-severity business logic defect (BUG-02) where a user can proceed to Checkout and submit an order with zero items in their cart, creating phantom orders with a $0 total. I documented clear reproduction steps and recommended disabling the checkout button when the cart item array length is zero."*

### Q3: "How did you test financial and tax calculations?"
> *"I used manual equivalence testing with varied cart combinations. For instance, testing items priced at $29.99 and $9.99, I verified that the item subtotal of $39.98 incurred an exact 8.00% tax of $3.20 (rounded to two decimals), yielding an accurate grand total of $43.18 on the confirmation screen."*
