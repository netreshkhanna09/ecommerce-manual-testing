# 🛒 E-Commerce Website Manual Testing: Complete Guide & Interview Prep (Easy Language Edition)

> **Audience:** QA Beginners, Manual Testers, and Interview Candidates  
> **Application Under Test:** [SauceDemo Web App](https://www.saucedemo.com/) (Swag Labs)  
> **Credentials:** `standard_user` / `secret_sauce`  
> **Tools:** Web Browser (Chrome/Firefox/Edge), Google Sheets / Excel, GitHub  
> **Pass Rate:** 90.00% (27 Passed, 3 Failed) | **Defects Found:** 6 Genuine Bugs  

---

## 📌 1. What Is This Project About? (In Simple Words)

Imagine you are shopping on an online store like Amazon or Flipkart. Your goal is simple: log in, pick a product, add it to your cart, fill in your delivery address, check the total bill, and complete checkout.

As a **Manual QA Tester**, your job is NOT to build this website. Your job is to **test every single step** to check whether it works smoothly for real users, and to catch mistakes (bugs) before customers get frustrated.

### The Shopping Journey We Tested:
1. **Login:** Entering username and password to enter the store.
2. **Product Catalog:** Viewing 6 items with their photos, descriptions, and prices.
3. **Sorting:** Changing product order (Name A-Z, Z-A, Price Low-High, Price High-Low).
4. **Shopping Cart:** Adding products, checking the red badge counter (1, 2, 3), and deleting items.
5. **Checkout Step 1:** Filling in First Name, Last Name, and Postal/Zip code.
6. **Checkout Step 2:** Verifying price calculations (Subtotal + 8% Sales Tax = Final Grand Total).
7. **Confirmation:** Reaching the "Thank you for your order!" screen and returning home.

---

## 🧭 2. The 7 Project Stages Explained Step-by-Step

### Stage 1: Exploring the Website First
- **Why we did it:** Never write tests blindly.
- **What we did:** We opened `https://www.saucedemo.com` and clicked around like a real user. We observed what happened when we added items, left fields blank, or typed wrong passwords. Understanding the normal flow first makes test writing 10x easier.

### Stage 2: Creating the Master Test Plan
- **Why we did it:** A Test Plan is your project roadmap.
- **What it answers:**
  - *What are we testing?* (Login, catalog, sorting, cart, checkout, taxes).
  - *What are we NOT testing?* (Real credit card payments, backend SQL databases).
  - *What tools will we use?* (Chrome DevTools, Excel/Sheets, GitHub).
  - *When are we done?* (When all 30 tests are executed and pass rate is $\ge 85\%$).

### Stage 3: Writing 30 Clear Test Cases
- **Why we did it:** A test case is like a cooking recipe that anyone can follow to verify a feature.
- **Columns used:** Test Case ID | Module | Scenario | Preconditions | Steps | Expected Result | Actual Result | Status | Severity.

### Stage 4: Executing Tests on the Live Website
- **Why we did it:** Comparing what *should* happen against what *actually* happens.
- **Execution stats:**
  $$\text{Pass Rate} = \frac{27 \text{ Passed}}{27 + 3} \times 100 = 90.00\%$$
  - Total Planned: 30
  - Total Executed: 30 (100% execution)
  - Passed: 27
  - Failed: 3

### Stage 5: Reporting Genuine Defects (Bugs)
- **Why we did it:** When actual behavior does not match expected business logic, we log a defect.
- **What we did:** We documented 6 real bugs in Jira format with exact steps, severity, and screenshots.

### Stage 6: Writing the Final Test Summary Report
- **Why we did it:** A summary for managers and team leads summarizing quality, pass percentage, and a release recommendation (*Conditional Pass*).

### Stage 7: Publishing Your Work on GitHub
- **Why we did it:** To provide recruiters with transparent proof of work.

---

## 🎯 3. Important Testing Concepts in Plain English

### A. Equivalence Class Partitioning (ECP) — "Group Similar Inputs"
Instead of testing 1,000 different wrong passwords, you group inputs into buckets. Testing just one from each bucket gives 100% confidence:
- **Bucket 1 (Valid credentials):** `standard_user` + `secret_sauce` $\rightarrow$ Logs in.
- **Bucket 2 (Wrong password):** `standard_user` + `wrong123` $\rightarrow$ Error: Username and password do not match.
- **Bucket 3 (Empty inputs):** `[blank]` + `secret_sauce` $\rightarrow$ Error: Username is required.
- **Bucket 4 (Locked user):** `locked_out_user` + `secret_sauce` $\rightarrow$ Error: Sorry, this user has been locked out.

### B. Boundary Value Analysis (BVA) — "Test at the Edges"
Errors usually happen at the boundaries (limits).
- **Cart Boundary:** Minimum valid checkout boundary is **1 item**. When we tested the lower edge of **0 items**, we caught **BUG-02**: the app let us click "Checkout" with nothing in the cart!
- **Price Boundary:** Lowest price item ($7.99 Onesie) up to highest price item ($49.99 Fleece Jacket).

### C. Negative Testing — "Trying to Break the App"
Positive testing enters valid data. Negative testing intentionally enters wrong data (e.g. typing symbols in postal code `!@#$%`, leaving mandatory fields empty, or accessing `/inventory.html` without logging in) to ensure the system defends itself with helpful error banners.

### D. Financial Tax Calculation Math (8.00% Tax)
We manually calculated the numbers to ensure the website wasn't mischarging customers:
- Items chosen: Sauce Labs Backpack ($29.99) + Bike Light ($9.99) = **$39.98 Subtotal**
- Tax at 8.00%: $39.98 \times 0.08 = 3.1984 \rightarrow$ Rounded to 2 decimals = **$3.20 Tax**
- Grand Total: $39.98 + $3.20 = **$43.18**
- **Actual result on screen:** Screen displayed Item total: `$39.98`, Tax: `$3.20`, Total: `$43.18` (100% match!).

---

## 🐛 4. The 6 Genuine Bugs We Found (Explained Simply)

| Bug ID | Severity | Summary | Plain English Explanation |
|:---:|:---:|:---|:---|
| **BUG-01** | Medium (S3) | Missing product search bar | Customers cannot search products by keyword; they can only sort via dropdown. |
| **BUG-02** | High (S2) | Checkout allowed with 0 items | With an empty cart, clicking Checkout proceeds to address entry and allows placing a $0 order! |
| **BUG-03** | Medium (S3) | Postal code accepts symbols (`!@#$%`) | Field does not validate whether postal code is numeric or alphanumeric, risking lost delivery parcels. |
| **BUG-04** | High (S2) | Inventory "Remove" fails (`problem_user`) | Clicking "Remove" on catalog page fails to remove the item or decrement the cart badge. |
| **BUG-05** | Low (S4) | Broken photos showing dog pictures | For `problem_user`, all product photos fail to load and show a dog with a camera. |
| **BUG-06** | Critical (S1) | Last Name field is frozen (`problem_user`) | The Last Name field freezes during checkout, making it impossible to complete an order. |

---

## 💡 5. Top QA Interview Questions & Answers (Speak Like a Pro)

### Q1: "Tell me about this E-Commerce testing project."
> **Answer:** *"I tested an online shopping website called SauceDemo. I tested the complete customer journey from login, to searching and sorting products, adding items to the cart, filling in the checkout form, verifying the 8% tax calculation, and finishing the order. I wrote 30 test cases, ran them all, achieved a 90% pass rate, and found 6 real bugs—including a major bug where users can checkout with 0 items in their cart."*

### Q2: "What is Boundary Value Analysis? Did you use it?"
> **Answer:** *"Boundary Value Analysis means testing the edges or limits of an input, because developers most often make mistakes at boundaries. I used it on the shopping cart: the minimum allowed boundary to checkout should be 1 item. When I tested 0 items (below boundary), I discovered that the website still allowed me to checkout, which is a real bug!"*

### Q3: "What is the difference between Severity and Priority? Give examples from your project."
> **Answer:** *"Severity is how badly the bug damages the system technically. Priority is how quickly developers need to fix it.*  
> - *Critical Severity + High Priority: When using `problem_user`, the Last Name field freezes, blocking checkout completely. No customer can buy anything (S1/P1).*  
> - *Medium Severity + Medium Priority: The missing search bar (BUG-01). Users can still buy items using sorting, so it is not blocking sales immediately, but it hurts usability."*

### Q4: "How did you verify the price and tax calculation?"
> **Answer:** *"I picked two products: Sauce Labs Backpack ($29.99) and Bike Light ($9.99). Their subtotal was $39.98. The website charges 8% tax. I calculated 39.98 * 0.08 = 3.1984. Rounding to 2 decimal places gives $3.20 tax. Adding $39.98 + $3.20 gave a grand total of $43.18. I compared this with the screen, and the website matched my math with 100% precision."*

### Q5: "What will you do if a developer says 'The empty cart checkout is not a bug'?"
> **Answer:** *"I will politely explain the business impact: allowing orders with 0 items creates $0 invoices, triggers automatic confirmation emails to customers, and creates confusing orders in the warehouse logistics queue. If we still disagree, I will bring the issue to the Product Owner with clear steps and let them decide based on business rules."*

### Q6: "What is the difference between Smoke Testing and Regression Testing?"
> **Answer:** *"Smoke Testing is a quick check to see if basic core features work before doing deep testing (e.g., Can the user log in and view products?). Regression Testing is re-running old tests after a bug fix to make sure the fix didn't break anything that used to work."*

---

## 💼 6. Resume Bullet Points & Elevator Pitch

### 4 Concise Resume Bullet Points:
```markdown
• Executed 30 manual test cases for an e-commerce platform covering login, catalog sorting, cart management, and checkout, achieving a 90% pass rate.
• Applied ECP and BVA techniques to validate form inputs, negative edge cases, and verify 8.00% sales tax and price calculations.
• Identified and logged 6 defects in Jira format with clear reproduction steps, including a high-severity bug allowing checkout with an empty cart.
• Authored full QA documentation—including an IEEE 829 Test Plan, test matrices, and execution reports—published on GitHub.
```

### 30-Second Elevator Pitch (For HR / Recruiter Phone Calls):
> *"I recently completed an end-to-end manual QA testing project on an e-commerce website. I designed and executed 30 test cases covering authentication, product sorting, cart operations, form validation, and tax calculations. I applied testing methods like Equivalence Partitioning and Boundary Value Analysis to find edge cases, and I documented 6 real bugs in Jira format. All my test plans, Excel sheets, and reports are published on my GitHub. I am ready to bring this structured testing approach to your QA team!"*
