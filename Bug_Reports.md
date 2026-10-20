# Defect Log & Bug Reports: SauceDemo E-Commerce Platform

**Document Identifier:** BUG-SAUCEDEMO-001  
**Project:** SauceDemo Manual Functional Testing  
**Total Defects Logged:** 6  
**Defect Status:** 6 Open / Documented  
**Tools:** Jira-Compatible Schema & Google Sheets / Excel  

---

## Defect Summary Overview

| Defect ID | Summary | Module | Severity | Priority | Status |
|:---|:---|:---|:---:|:---:|:---:|
| **BUG-01** | Missing product search functionality on product catalog page | Product Catalog | Medium (S3) | P3 - Medium | Open |
| **BUG-02** | User is permitted to initiate and proceed through Checkout with empty cart (0 items) | Shopping Cart / Checkout | High (S2) | P2 - High | Open |
| **BUG-03** | Postal Code field accepts arbitrary special characters without validation | Checkout Step 1 | Medium (S3) | P3 - Medium | Open |
| **BUG-04** | Clicking "Remove" on inventory page fails to remove item from cart (`problem_user`) | Shopping Cart | High (S2) | P2 - High | Open |
| **BUG-05** | Product catalog displays broken image thumbnails with 404 dog asset (`problem_user`) | Product Catalog | Low (S4) | P3 - Medium | Open |
| **BUG-06** | Last Name field is unresponsive / corrupted during checkout (`problem_user`) | Checkout Step 1 | Critical (S1) | P1 - Immediate | Open |

---

## Detailed Bug Reports

### BUG-01: Missing product search functionality on product catalog page
- **Defect ID:** BUG-01
- **Associated Test Case:** TC16
- **Module:** Product Catalog
- **Severity:** Medium (S3)
- **Priority:** P3 (Medium)
- **Environment:** Windows 11 Pro, Google Chrome v122, `https://www.saucedemo.com/inventory.html`
- **Reporter:** QA Manual Test Engineer
- **Summary:** Standard e-commerce product search input is absent from header and inventory interface.
- **Preconditions:** User is logged in as `standard_user` on `/inventory.html`.
- **Steps to Reproduce:**
  1. Navigate to `/inventory.html`.
  2. Inspect the header, navigation bar, and inventory filter container for a search input field.
  3. Attempt to filter or search products by entering product keywords.
- **Expected Result:** A search bar should be present allowing users to type keywords (e.g., "shirt", "backpack") and dynamically filter the product list.
- **Actual Result:** No search bar or keyword filter exists on the interface. Users can only sort via dropdown.
- **Impact:** Decreased usability and inability to locate specific items efficiently on larger inventory catalogs.

---

### BUG-02: User is permitted to initiate and proceed through Checkout with empty cart (0 items)
- **Defect ID:** BUG-02
- **Associated Test Case:** TC23
- **Module:** Shopping Cart / Checkout Workflow
- **Severity:** High (S2)
- **Priority:** P2 (High)
- **Environment:** Windows 11 Pro, Google Chrome v122, `https://www.saucedemo.com/cart.html`
- **Reporter:** QA Manual Test Engineer
- **Summary:** Application allows checkout initiation and shipping address entry when the cart contains zero items.
- **Preconditions:** User is logged in as `standard_user`. Cart is empty (badge is absent, 0 items in list).
- **Steps to Reproduce:**
  1. Navigate to `/cart.html` with an empty cart.
  2. Observe the "Checkout" button state (it is enabled).
  3. Click the "Checkout" button (`#checkout`).
  4. Fill in First Name: "Jane", Last Name: "Doe", Zip: "10001" on `/checkout-step-one.html`.
  5. Click "Continue".
- **Expected Result:** "Checkout" button should be disabled when the cart is empty, or clicking it should trigger a warning notification: *"Your cart is empty. Please add items before checking out."*.
- **Actual Result:** The application allows the user to proceed to Checkout Step 1 and Checkout Step 2 with an Item Total of `$0.00`, enabling placement of an empty order.
- **Impact:** Creates phantom order transactions with $0 value, resulting in unnecessary server processing and logistics confusion.

---

### BUG-03: Postal Code field accepts arbitrary special characters without validation
- **Defect ID:** BUG-03
- **Associated Test Case:** TC27
- **Module:** Checkout Step 1 (Customer Information)
- **Severity:** Medium (S3)
- **Priority:** P3 (Medium)
- **Environment:** Windows 11 Pro, Google Chrome v122, `https://www.saucedemo.com/checkout-step-one.html`
- **Reporter:** QA Manual Test Engineer
- **Summary:** Zip/Postal Code input field accepts arbitrary symbols, spaces, and excessive strings without alphanumeric validation.
- **Preconditions:** User has at least 1 item in cart and is on `/checkout-step-one.html`.
- **Steps to Reproduce:**
  1. Enter valid First Name: `John`.
  2. Enter valid Last Name: `Smith`.
  3. Enter special characters `!@#$%^&*()` or text string `abc-invalid-zip` into the "Zip/Postal Code" field.
  4. Click "Continue" button.
- **Expected Result:** Form validation should trigger with an informative error message: *"Please enter a valid alphanumeric postal code (e.g., 12345 or A1B 2C3)"*.
- **Actual Result:** Form passes validation without warning and advances to Checkout Step 2 (`/checkout-step-two.html`).
- **Impact:** Compromises data integrity for shipping and delivery logistics systems downstream.

---

### BUG-04: Clicking "Remove" on inventory page fails to remove item from cart (`problem_user`)
- **Defect ID:** BUG-04
- **Associated Test Case:** TC19 (Edge Persona)
- **Module:** Shopping Cart
- **Severity:** High (S2)
- **Priority:** P2 (High)
- **Environment:** Windows 11 Pro, Google Chrome v122, `https://www.saucedemo.com/inventory.html`
- **Reporter:** QA Manual Test Engineer
- **Summary:** When logged in as `problem_user`, clicking the "Remove" button on an added product fails to remove it from the cart or update the badge.
- **Preconditions:** User is logged in using test account `problem_user` / `secret_sauce`.
- **Steps to Reproduce:**
  1. Add "Sauce Labs Backpack" to cart. Notice button turns into "Remove" and badge shows `1`.
  2. Click the "Remove" button directly on the inventory page.
  3. Observe button state and cart badge.
- **Expected Result:** Button should revert to "Add to cart" and cart badge should decrement to 0 / disappear.
- **Actual Result:** Button remains "Remove" and cart badge remains `1`. The item is NOT removed from the cart.
- **Impact:** Breaks core shopping cart interaction, forcing users to navigate to the cart page to attempt deletion.

---

### BUG-05: Product catalog displays broken image thumbnails with 404 dog asset (`problem_user`)
- **Defect ID:** BUG-05
- **Associated Test Case:** TC10 (Edge Persona)
- **Module:** Product Catalog
- **Severity:** Low (S4)
- **Priority:** P3 (Medium)
- **Environment:** Windows 11 Pro, Google Chrome v122, `https://www.saucedemo.com/inventory.html`
- **Reporter:** QA Manual Test Engineer
- **Summary:** All product cards render identical fallback dog placeholder image rather than actual product photos.
- **Preconditions:** User logs in with `problem_user` / `secret_sauce`.
- **Steps to Reproduce:**
  1. Log in with `problem_user`.
  2. View the products grid on `/inventory.html`.
  3. Inspect image sources for Backpack, Bike Light, Bolt T-Shirt, etc.
- **Expected Result:** Each product displays its unique product photo matching its description.
- **Actual Result:** Every item renders the same image asset (`/static/media/sl-404.168b1cce.jpg` - a dog with a camera).
- **Impact:** Misleads customers and degrades brand presentation and product identification.

---

### BUG-06: Last Name field is unresponsive / corrupted during checkout (`problem_user`)
- **Defect ID:** BUG-06
- **Associated Test Case:** TC25 (Edge Persona)
- **Module:** Checkout Step 1
- **Severity:** Critical (S1)
- **Priority:** P1 (Immediate)
- **Environment:** Windows 11 Pro, Google Chrome v122, `https://www.saucedemo.com/checkout-step-one.html`
- **Reporter:** QA Manual Test Engineer
- **Summary:** The "Last Name" input field cannot be filled or auto-resets, causing permanent form validation failure and blocking checkout completion.
- **Preconditions:** User logged in as `problem_user`, has items in cart, and is on `/checkout-step-one.html`.
- **Steps to Reproduce:**
  1. Enter "Alice" in First Name field.
  2. Attempt to type "Smith" in the Last Name field.
  3. Notice input fails to record keystrokes or locks up.
  4. Enter "90210" in Zip Code.
  5. Click "Continue".
- **Expected Result:** Last Name field accepts user typing, and form submits successfully when valid data is entered.
- **Actual Result:** Last Name field remains empty or unresponsive, triggering blocking validation error: `"Error: Last Name is required"`. User is unable to proceed with purchase.
- **Impact:** Complete blocker for revenue and transaction completion for affected user accounts.
