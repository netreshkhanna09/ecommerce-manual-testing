# Comprehensive Test Plan: SauceDemo E-Commerce Platform

**Document Identifier:** TP-SAUCEDEMO-001  
**Project Name:** SauceDemo E-commerce Manual Functional Testing  
**Application Under Test (AUT):** [SauceDemo Web Application](https://www.saucedemo.com)  
**Author:** QA Manual Test Engineer  
**Version:** 1.0  
**Status:** Approved / Active  
**Standard:** IEEE 829 Test Documentation Standard  

---

## 1. Introduction & Objectives

### 1.1 Purpose
The purpose of this Test Plan is to define the testing approach, scope, test strategy, resources, environment, and schedule for verifying the end-to-end user workflows of the SauceDemo e-commerce web platform. This document serves as the master blueprint for manual functional testing across all core modules.

### 1.2 Testing Objectives
- Validate core end-to-end shopping workflow: User Login → Product Browsing/Sorting → Cart Operations → Multi-step Checkout → Order Confirmation.
- Verify positive, negative, and edge-case behaviors using Equivalence Class Partitioning (ECP) and Boundary Value Analysis (BVA).
- Validate input validation and error handling on all forms (Login, Checkout details).
- Verify financial computations: Item totals, 8.00% sales tax calculation, and order grand totals.
- Uncover functional defects, visual anomalies, and business logic inconsistencies, reporting them with actionable reproduction steps.

---

## 2. Scope of Testing

### 2.1 In-Scope Modules & Features
| Module ID | Module Name | Scope Description |
|:---|:---|:---|
| **MOD-01** | **Authentication** | Valid/invalid credentials, empty inputs, locked accounts, password masking, logout, session expiration. |
| **MOD-02** | **Product Inventory & Sorting** | Product catalog loading, pricing display, product details view, 4 sorting modes (A-Z, Z-A, Low-High, High-Low). |
| **MOD-03** | **Shopping Cart Operations** | Adding single/multiple products, badge counter updates, removing items from inventory and cart views, cart persistence. |
| **MOD-04** | **Checkout Workflow (Step 1)** | First name, last name, and postal code fields; required field validation, invalid format handling, cancellation flow. |
| **MOD-05** | **Checkout Workflow (Step 2)** | Order review, shipping and payment method display, item total summation, 8% tax calculation, grand total accuracy. |
| **MOD-06** | **Order Confirmation & Session** | Order completion message, "Back Home" navigation, Reset App State from hamburger menu, direct URL access protection. |

### 2.2 Out-of-Scope
- Automated testing (Selenium, Playwright, Cypress) — manual functional focus.
- Backend database direct queries (mock front-end demo application).
- Performance, load, and stress testing.
- Live credit card gateway processing (SauceDemo uses mock SauceCard #31337).

---

## 3. Test Types & Methodologies

1. **Smoke Testing:** Verifies basic build stability (user can log in, view catalog, access cart).
2. **Functional Testing:** Validates that each feature behaves in accordance with e-commerce business requirements.
3. **Negative Testing:** Intentionally inputs invalid, unexpected, or empty data to verify proper error messages and system defenses.
4. **Boundary Value Analysis (BVA):** Tests boundary limits on text inputs (e.g., zip code lengths, 0 items in cart).
5. **Equivalence Class Partitioning (ECP):** Groups valid and invalid inputs into partitions to maximize test coverage with efficient test cases.
6. **UI & Usability Testing:** Verifies button responsiveness, badge counters, error banner visibility, and typography.
7. **Regression Testing:** Re-executing critical user journey tests after defect discovery to ensure unchanged features remain operational.

---

## 4. Test Environment & Configurations

| Parameter | Specification |
|:---|:---|
| **Application URL** | `https://www.saucedemo.com/` |
| **Operating System** | Windows 11 Pro 64-bit |
| **Supported Browsers** | Google Chrome (v122+), Mozilla Firefox (v124+), Microsoft Edge (v122+) |
| **Screen Resolutions** | 1920x1080 (Desktop Full HD), 1366x768 (Standard Laptop) |
| **Test Accounts** | `standard_user` (Primary happy path)<br>`locked_out_user` (Account lockout testing)<br>`problem_user` (Defect injection testing)<br>`error_user` (Checkout exception testing) |
| **Default Password** | `secret_sauce` |
| **Test Documentation Tools** | Microsoft Excel / Google Sheets, Jira (Defect Tracking), Markdown Portfolio |

---

## 5. Entry & Exit Criteria

### 5.1 Entry Criteria (When Testing Starts)
- Test Plan document reviewed and approved.
- Web application URL is accessible with HTTP 200 status code.
- Test accounts and credentials are confirmed available.
- Test cases are documented with steps, expected outcomes, and test data.

### 5.2 Exit Criteria (When Testing Completes)
- 100% of planned test cases (30/30) executed.
- Minimum 85% test pass rate achieved on primary functional paths.
- All discovered defects are logged with full reproduction steps, severity, priority, and screenshots/evidence.
- No Critical (Blocker) defects remain unaddressed on core checkout pathways.
- Final Test Execution Report compiled and signed off.

---

## 6. Defect Severity & Priority Classification

| Severity Level | Definition | Example in SauceDemo |
|:---|:---|:---|
| **Critical (S1)** | System crash, security breach, complete blockage of core revenue workflow. | Checkout button completely non-responsive, preventing any purchase. |
| **High (S2)** | Major feature failure with no immediate workaround. | Tax calculation formula computes wrong totals, mischarging customers. |
| **Medium (S3)** | Non-critical functional flaw or missing form input validation. | Postal code field accepts symbols (`!@#$%`) without validation. |
| **Low (S4)** | Minor cosmetic, alignment, or spelling defect that does not affect data integrity. | Slight icon misalignment or missing product search bar. |

| Priority Level | Resolution Urgency |
|:---|:---|
| **P1 - Immediate** | Must be fixed before any production deployment or next test cycle. |
| **P2 - High** | Fix required in the current release sprint. |
| **P3 - Medium** | Fix can be scheduled in the upcoming minor maintenance sprint. |
| **P4 - Low** | Cosmetic adjustment or feature enhancement request. |

---

## 7. Deliverables
1. **Master Test Plan** (`Test_Plan.md`, `Test_Plan.xlsx`)
2. **Comprehensive Test Case Suite** (`Test_Cases.md`, `Test_Cases.xlsx` — 30 test cases)
3. **Defect Log & Bug Reports** (`Bug_Reports.md`, `Bug_Reports.xlsx` — 6 documented defects)
4. **Final Test Execution Summary Report** (`Test_Execution_Report.md`, `Test_Execution_Report.pdf`)
5. **Project README & GitHub Repository Package** (`README.md`)
