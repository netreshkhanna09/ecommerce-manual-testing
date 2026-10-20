# Manual Test Cases: SauceDemo E-Commerce Platform

**Document Identifier:** TC-SAUCEDEMO-001  
**Project:** SauceDemo Functional & Manual Testing  
**Total Test Cases:** 30  
**Executed:** 30 | **Passed:** 27 | **Failed:** 3 | **Blocked:** 0  
**Pass Rate:** 90.00%  

---

## Summary Matrix by Module

| Module ID | Module Name | Total Cases | Passed | Failed | Blocked |
|:---|:---|:---:|:---:|:---:|:---:|
| **MOD-01** | Authentication & Session Management | 8 | 8 | 0 | 0 |
| **MOD-02** | Product Catalog, Search & Sorting | 7 | 6 | 1 | 0 |
| **MOD-03** | Shopping Cart Operations | 6 | 6 | 0 | 0 |
| **MOD-04** | Checkout Step 1: Customer Information | 5 | 3 | 2 | 0 |
| **MOD-05** | Checkout Step 2: Price & Tax Verification | 2 | 2 | 0 | 0 |
| **MOD-06** | Order Confirmation & App State Management | 2 | 2 | 0 | 0 |
| **TOTAL** | | **30** | **27** | **3** | **0** |

---

## Detailed Test Cases

### Module 1: Authentication & Session Management

#### TC01: Log in with valid standard credentials
- **Module:** Authentication
- **Test Type:** Functional / Smoke / Positive
- **Preconditions:** User is on the login page (`https://www.saucedemo.com/`).
- **Test Steps:**
  1. Enter `standard_user` into the Username field.
  2. Enter `secret_sauce` into the Password field.
  3. Click the "Login" button.
- **Test Data:** `standard_user` / `secret_sauce`
- **Expected Result:** User is successfully authenticated and redirected to the Inventory page (`/inventory.html`). "Products" title and cart icon are visible.
- **Actual Result:** Authenticated successfully, redirected to `/inventory.html`. Products and cart icon are displayed.
- **Status:** **PASS**
- **Severity:** Critical (S1)

#### TC02: Log in with valid username and incorrect password
- **Module:** Authentication
- **Test Type:** Functional / Negative
- **Preconditions:** User is on the login page.
- **Test Steps:**
  1. Enter `standard_user` into the Username field.
  2. Enter `wrong_password_123` into the Password field.
  3. Click the "Login" button.
- **Test Data:** `standard_user` / `wrong_password_123`
- **Expected Result:** Login is rejected. Red error banner appears stating: `"Epic sadface: Username and password do not match any user in this service"`.
- **Actual Result:** Login rejected with exact error message banner: `"Epic sadface: Username and password do not match any user in this service"`.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC03: Log in with unregistered username
- **Module:** Authentication
- **Test Type:** Functional / Negative
- **Preconditions:** User is on the login page.
- **Test Steps:**
  1. Enter `nonexistent_user_99` into the Username field.
  2. Enter `secret_sauce` into the Password field.
  3. Click the "Login" button.
- **Test Data:** `nonexistent_user_99` / `secret_sauce`
- **Expected Result:** Login is rejected with error banner: `"Epic sadface: Username and password do not match any user in this service"`.
- **Actual Result:** Login rejected with expected error banner. No session initiated.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC04: Log in with blank username field
- **Module:** Authentication
- **Test Type:** Negative / Form Validation
- **Preconditions:** User is on the login page.
- **Test Steps:**
  1. Leave Username field empty.
  2. Enter `secret_sauce` into Password field.
  3. Click "Login" button.
- **Test Data:** Username: `[empty]`, Password: `secret_sauce`
- **Expected Result:** Form validation prevents submission. Error banner displays: `"Epic sadface: Username is required"`.
- **Actual Result:** Error banner displayed: `"Epic sadface: Username is required"`. Input border highlights in red.
- **Status:** **PASS**
- **Severity:** Medium (S3)

#### TC05: Log in with blank password field
- **Module:** Authentication
- **Test Type:** Negative / Form Validation
- **Preconditions:** User is on the login page.
- **Test Steps:**
  1. Enter `standard_user` into Username field.
  2. Leave Password field empty.
  3. Click "Login" button.
- **Test Data:** Username: `standard_user`, Password: `[empty]`
- **Expected Result:** Form validation prevents submission. Error banner displays: `"Epic sadface: Password is required"`.
- **Actual Result:** Error banner displayed: `"Epic sadface: Password is required"`.
- **Status:** **PASS**
- **Severity:** Medium (S3)

#### TC06: Log in with locked out user account
- **Module:** Authentication
- **Test Type:** Negative / Business Logic
- **Preconditions:** User is on the login page.
- **Test Steps:**
  1. Enter `locked_out_user` into Username field.
  2. Enter `secret_sauce` into Password field.
  3. Click "Login" button.
- **Test Data:** `locked_out_user` / `secret_sauce`
- **Expected Result:** Access is denied. Error banner states: `"Epic sadface: Sorry, this user has been locked out."`.
- **Actual Result:** Error banner states: `"Epic sadface: Sorry, this user has been locked out."`. Account is barred from catalog.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC07: Password field masking verification
- **Module:** Authentication
- **Test Type:** Security / UI
- **Preconditions:** User is on the login page.
- **Test Steps:**
  1. Type characters into the Password input field.
  2. Inspect displayed text visually and verify input element attributes.
- **Test Data:** Password: `secret_sauce`
- **Expected Result:** Characters are masked with bullets/dots. The input HTML attribute is `type="password"`.
- **Actual Result:** Input characters are masked as bullets. Inspecting element shows `type="password"`.
- **Status:** **PASS**
- **Severity:** Medium (S3)

#### TC08: Verify user logout functionality
- **Module:** Authentication
- **Test Type:** Functional / Session
- **Preconditions:** User is logged in and on the inventory page.
- **Test Steps:**
  1. Click the top-left hamburger menu button (`#react-burger-menu-btn`).
  2. Click the "Logout" link (`#logout_sidebar_link`).
- **Test Data:** N/A
- **Expected Result:** User is logged out and redirected back to the login page. Session storage is cleared.
- **Actual Result:** Redirected back to `https://www.saucedemo.com/`. Username and password fields are empty.
- **Status:** **PASS**
- **Severity:** High (S2)

---

### Module 2: Product Catalog, Search & Sorting

#### TC09: Direct URL access protection without login
- **Module:** Security & Navigation
- **Test Type:** Security / Negative
- **Preconditions:** Browser has no active SauceDemo session (incognito or logged out).
- **Test Steps:**
  1. Directly navigate to URL: `https://www.saucedemo.com/inventory.html`.
- **Test Data:** URL: `/inventory.html`
- **Expected Result:** Direct access blocked. User redirected to `/` with error message: `"Epic sadface: You can only access '/inventory.html' when you are logged in."`.
- **Actual Result:** Access blocked, redirected to login page with exact error banner.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC10: Product Catalog default display verification
- **Module:** Product Catalog
- **Test Type:** Functional / UI
- **Preconditions:** User is logged in as `standard_user`.
- **Test Steps:**
  1. Observe the inventory grid on `/inventory.html`.
  2. Verify all 6 products display title, description, price, product image, and "Add to cart" button.
- **Test Data:** 6 standard inventory items
- **Expected Result:** All 6 products display high-resolution images, valid descriptions, correct prices ($7.99 - $49.99), and active "Add to cart" buttons.
- **Actual Result:** All 6 products loaded with respective images, text descriptions, prices, and functional buttons.
- **Status:** **PASS**
- **Severity:** Medium (S3)

#### TC11: Sort products by Name: A to Z (Alphabetical Ascending)
- **Module:** Product Catalog / Sorting
- **Test Type:** Functional
- **Preconditions:** User is on `/inventory.html`.
- **Test Steps:**
  1. Click the product sort dropdown (`.product_sort_container`).
  2. Select "Name (A to Z)".
  3. Verify the alphabetical order of the first and last displayed items.
- **Test Data:** Sort option: `az`
- **Expected Result:** First item is "Sauce Labs Backpack" (starts with S-B) and last item is "Test.allTheThings() T-Shirt (Red)" (starts with T).
- **Actual Result:** First item: "Sauce Labs Backpack", Last item: "Test.allTheThings() T-Shirt (Red)". Strict ascending alphabetical order verified.
- **Status:** **PASS**
- **Severity:** Medium (S3)

#### TC12: Sort products by Name: Z to A (Alphabetical Descending)
- **Module:** Product Catalog / Sorting
- **Test Type:** Functional
- **Preconditions:** User is on `/inventory.html`.
- **Test Steps:**
  1. Click the sort dropdown.
  2. Select "Name (Z to A)".
  3. Verify product order.
- **Test Data:** Sort option: `za`
- **Expected Result:** Products re-render in reverse alphabetical order. First item is "Test.allTheThings() T-Shirt (Red)", last item is "Sauce Labs Backpack".
- **Actual Result:** First item: "Test.allTheThings() T-Shirt (Red)", Last item: "Sauce Labs Backpack". Reverse alphabetical order verified.
- **Status:** **PASS**
- **Severity:** Medium (S3)

#### TC13: Sort products by Price: Low to High (Numerical Ascending)
- **Module:** Product Catalog / Sorting
- **Test Type:** Functional / Equivalence Partitioning
- **Preconditions:** User is on `/inventory.html`.
- **Test Steps:**
  1. Click sort dropdown.
  2. Select "Price (low to high)".
  3. Verify prices across the inventory list.
- **Test Data:** Sort option: `lohi`
- **Expected Result:** Products appear in strictly ascending price order: $7.99 (Sauce Labs Onesie) → $9.99 → $15.99 → $15.99 → $29.99 → $49.99 (Sauce Labs Fleece Jacket).
- **Actual Result:** First product is Onesie at $7.99, last product is Fleece Jacket at $49.99. All prices strictly ascending.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC14: Sort products by Price: High to Low (Numerical Descending)
- **Module:** Product Catalog / Sorting
- **Test Type:** Functional / Equivalence Partitioning
- **Preconditions:** User is on `/inventory.html`.
- **Test Steps:**
  1. Click sort dropdown.
  2. Select "Price (high to low)".
  3. Verify prices across the inventory list.
- **Test Data:** Sort option: `hilo`
- **Expected Result:** Products appear in strictly descending price order: $49.99 (Fleece Jacket) → $29.99 → $15.99 → $15.99 → $9.99 → $7.99 (Onesie).
- **Actual Result:** First item priced at $49.99, last item priced at $7.99. All prices strictly descending.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC15: Product Details page navigation and data consistency
- **Module:** Product Catalog
- **Test Type:** Functional / Navigation
- **Preconditions:** User is on `/inventory.html`.
- **Test Steps:**
  1. Click on the title link "Sauce Labs Backpack".
  2. Verify details page (`/inventory-item.html?id=4`) opens with identical title, price ($29.99), and description.
  3. Click "Back to products" button.
- **Test Data:** Item ID 4 (Sauce Labs Backpack)
- **Expected Result:** Details page displays full-size image, accurate price of $29.99, and "Back to products" returns user to `/inventory.html`.
- **Actual Result:** Detailed item view rendered accurately; navigation back to inventory succeeded.
- **Status:** **PASS**
- **Severity:** Medium (S3)

#### TC16: Search bar functionality check
- **Module:** Product Catalog / Search
- **Test Type:** Functional / Usability
- **Preconditions:** User is on `/inventory.html`.
- **Test Steps:**
  1. Search for a product by keyword (e.g., "shirt", "backpack").
- **Test Data:** Search keyword: `backpack`
- **Expected Result:** Search bar should exist in the header or catalog view, allowing users to query items by name/keyword.
- **Actual Result:** **No search bar or search input field exists anywhere on the application.** Users cannot search products directly.
- **Status:** **FAIL** (Logged as Defect **BUG-01**)
- **Severity:** Medium (S3)

---

### Module 3: Shopping Cart Operations

#### TC17: Add a single product to shopping cart
- **Module:** Shopping Cart
- **Test Type:** Functional / Smoke
- **Preconditions:** User is on `/inventory.html`, cart is empty.
- **Test Steps:**
  1. Click "Add to cart" button for "Sauce Labs Backpack".
  2. Observe the button state and header cart icon.
- **Test Data:** "Sauce Labs Backpack" ($29.99)
- **Expected Result:** The button text toggles to "Remove" (with red outline). Shopping cart badge displays number `1`.
- **Actual Result:** Button immediately switched to "Remove", shopping cart badge displayed `1`.
- **Status:** **PASS**
- **Severity:** Critical (S1)

#### TC18: Add multiple products and verify cart badge counter
- **Module:** Shopping Cart
- **Test Type:** Functional / Boundary Value Analysis
- **Preconditions:** User is on `/inventory.html`, 1 item in cart.
- **Test Steps:**
  1. Click "Add to cart" on "Sauce Labs Bike Light".
  2. Click "Add to cart" on "Sauce Labs Bolt T-Shirt".
  3. Check the cart badge counter value.
- **Test Data:** 3 total items added
- **Expected Result:** Cart badge counter increments sequentially from 1 → 2 → 3.
- **Actual Result:** Cart badge displays `3` accurately.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC19: Remove product from inventory page
- **Module:** Shopping Cart
- **Test Type:** Functional
- **Preconditions:** 3 items in cart (`standard_user`).
- **Test Steps:**
  1. Click "Remove" button on "Sauce Labs Bike Light" on the inventory page.
  2. Observe button state and cart badge.
- **Test Data:** "Sauce Labs Bike Light"
- **Expected Result:** Button switches back to "Add to cart". Cart badge decrements from 3 to 2.
- **Actual Result:** Button changed to "Add to cart", cart badge updated to `2`.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC20: View Cart page and verify item listing and details
- **Module:** Shopping Cart
- **Test Type:** Functional / Data Integrity
- **Preconditions:** 2 items in cart.
- **Test Steps:**
  1. Click the shopping cart container icon in header (`.shopping_cart_link`).
  2. Verify URL is `/cart.html`.
  3. Verify item names, descriptions, individual prices, and quantity `1` displayed.
- **Test Data:** Backpack ($29.99), Bolt T-Shirt ($15.99)
- **Expected Result:** Cart displays exactly 2 items with correct titles, prices ($29.99, $15.99), quantity 1 each, and "Continue Shopping" / "Checkout" buttons.
- **Actual Result:** Both items rendered accurately with correct prices, descriptions, and action buttons.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC21: Remove product from inside the Shopping Cart page
- **Module:** Shopping Cart
- **Test Type:** Functional
- **Preconditions:** User is on `/cart.html` with 2 items.
- **Test Steps:**
  1. Click "Remove" button next to "Sauce Labs Bolt T-Shirt".
  2. Observe the cart list and badge.
- **Test Data:** "Sauce Labs Bolt T-Shirt"
- **Expected Result:** Item is immediately removed from cart list. Badge decrements from 2 to 1.
- **Actual Result:** Item removed from DOM list; cart badge updated to `1`.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC22: Shopping Cart state persistence across page refresh
- **Module:** Shopping Cart
- **Test Type:** Session / State Persistence
- **Preconditions:** 1 item in cart.
- **Test Steps:**
  1. Refresh the browser page (`F5` / `Ctrl+R`).
  2. Check if cart badge remains `1`.
  3. Navigate to `/cart.html` and check item presence.
- **Test Data:** 1 item in cart
- **Expected Result:** Cart state persists across page reload. Cart badge remains 1 and item is intact.
- **Actual Result:** Cart state fully maintained in session storage. Item remains in cart after refresh.
- **Status:** **PASS**
- **Severity:** Medium (S3)

---

### Module 4: Checkout Step 1: Customer Information

#### TC23: Attempt checkout with an empty shopping cart (0 items)
- **Module:** Checkout / Business Logic
- **Test Type:** Negative / Business Logic / Boundary
- **Preconditions:** Shopping cart is completely empty (0 items). User is on `/cart.html`.
- **Test Steps:**
  1. Verify cart has no items.
  2. Click the green "Checkout" button (`#checkout`).
- **Test Data:** Empty cart (0 items)
- **Expected Result:** System should prevent checkout initiation when cart is empty, disabling the Checkout button or displaying warning: *"Your cart is empty"*.
- **Actual Result:** **System permits user to proceed to `/checkout-step-one.html` and continue checkout with zero items in cart.**
- **Status:** **FAIL** (Logged as Defect **BUG-02**)
- **Severity:** High (S2)

#### TC24: Submit Checkout Step 1 with empty First Name
- **Module:** Checkout Step 1
- **Test Type:** Negative / Form Validation
- **Preconditions:** Cart has 1 item. User is on `/checkout-step-one.html`.
- **Test Steps:**
  1. Leave First Name blank.
  2. Enter `Doe` into Last Name.
  3. Enter `90210` into Zip/Postal Code.
  4. Click "Continue" button.
- **Test Data:** First Name: `[empty]`, Last Name: `Doe`, Zip: `90210`
- **Expected Result:** Submission blocked. Error banner displayed: `"Error: First Name is required"`.
- **Actual Result:** Submission blocked with exact error banner: `"Error: First Name is required"`.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC25: Submit Checkout Step 1 with empty Last Name
- **Module:** Checkout Step 1
- **Test Type:** Negative / Form Validation
- **Preconditions:** User is on `/checkout-step-one.html`.
- **Test Steps:**
  1. Enter `John` into First Name.
  2. Leave Last Name blank.
  3. Enter `90210` into Zip/Postal Code.
  4. Click "Continue" button.
- **Test Data:** First Name: `John`, Last Name: `[empty]`, Zip: `90210`
- **Expected Result:** Submission blocked. Error banner displayed: `"Error: Last Name is required"`.
- **Actual Result:** Submission blocked with exact error banner: `"Error: Last Name is required"`.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC26: Submit Checkout Step 1 with empty Zip/Postal Code
- **Module:** Checkout Step 1
- **Test Type:** Negative / Form Validation
- **Preconditions:** User is on `/checkout-step-one.html`.
- **Test Steps:**
  1. Enter `John` into First Name.
  2. Enter `Doe` into Last Name.
  3. Leave Zip/Postal Code blank.
  4. Click "Continue" button.
- **Test Data:** First Name: `John`, Last Name: `Doe`, Zip: `[empty]`
- **Expected Result:** Submission blocked. Error banner displayed: `"Error: Postal Code is required"`.
- **Actual Result:** Submission blocked with exact error banner: `"Error: Postal Code is required"`.
- **Status:** **PASS**
- **Severity:** High (S2)

#### TC27: Checkout Step 1: Boundary & format validation on Postal Code field
- **Module:** Checkout Step 1
- **Test Type:** Boundary Value Analysis / Equivalence Partitioning / Negative
- **Preconditions:** User is on `/checkout-step-one.html`.
- **Test Steps:**
  1. Enter `John` into First Name.
  2. Enter `Doe` into Last Name.
  3. Enter invalid special characters `!@#$%^&*()` or extreme length string (100 characters) into Zip/Postal Code.
  4. Click "Continue".
- **Test Data:** First Name: `John`, Last Name: `Doe`, Zip: `!@#$%^&*()`
- **Expected Result:** Application should validate postal code format and reject non-alphanumeric/special characters.
- **Actual Result:** **Application accepts special characters and proceeds to `/checkout-step-two.html` without format or length validation.**
- **Status:** **FAIL** (Logged as Defect **BUG-03**)
- **Severity:** Medium (S3)

---

### Module 5: Checkout Step 2: Price & Tax Verification

#### TC28: Cancel button on Checkout Step 1 returns to Cart
- **Module:** Checkout Step 1 / Navigation
- **Test Type:** Functional / Navigation
- **Preconditions:** User is on `/checkout-step-one.html` with items in cart.
- **Test Steps:**
  1. Fill form partially or leave blank.
  2. Click the "Cancel" button (`#cancel`).
- **Test Data:** N/A
- **Expected Result:** User is navigated back to `/cart.html` and cart items are preserved.
- **Actual Result:** Redirected to `/cart.html`. Items and cart count remain intact.
- **Status:** **PASS**
- **Severity:** Medium (S3)

#### TC29: Verify Item Total, Sales Tax (8.00%), and Grand Total calculation
- **Module:** Checkout Step 2 / Financial Computation
- **Test Type:** Functional / Mathematical Calculation
- **Preconditions:** Cart contains:
  1. Sauce Labs Backpack ($29.99)
  2. Sauce Labs Bike Light ($9.99)
  User completes Step 1 and arrives on `/checkout-step-two.html`.
- **Test Steps:**
  1. Calculate Expected Item Total = $29.99 + $9.99 = $39.98.
  2. Calculate Expected Tax at 8.00% = round(39.98 * 0.08, 2) = round(3.1984, 2) = $3.20.
  3. Calculate Expected Total = $39.98 + $3.20 = $43.18.
  4. Compare calculated values against displayed values on the screen.
- **Test Data:** Items: $29.99 + $9.99
- **Expected Result:** 
  - Item total: `$39.98`
  - Tax: `$3.20`
  - Total: `$43.18`
- **Actual Result:** 
  - Screen displays `Item total: $39.98`
  - Screen displays `Tax: $3.20`
  - Screen displays `Total: $43.18`
  Calculations match expected financial results with 100% precision.
- **Status:** **PASS**
- **Severity:** Critical (S1)

---

### Module 6: Order Confirmation & App State Management

#### TC30: Complete Checkout and verify Order Confirmation & Reset State
- **Module:** Order Confirmation / App State
- **Test Type:** End-to-End Functional / Smoke
- **Preconditions:** User is on `/checkout-step-two.html`.
- **Test Steps:**
  1. Click the "Finish" button (`#finish`).
  2. Verify URL is `/checkout-complete.html`.
  3. Verify confirmation heading: "Thank you for your order!".
  4. Verify green dispatch pony badge and message: "Your order has been dispatched, and will arrive just as fast as the pony can get there!".
  5. Click "Back Home" button (`#back-to-products`).
  6. Open hamburger menu and click "Reset App State".
- **Test Data:** Completed order
- **Expected Result:** User reaches `/checkout-complete.html` with thank you header and dispatch message. Cart badge resets to empty. "Back Home" returns user to inventory.
- **Actual Result:** Reached confirmation page with header "Thank you for your order!". Cart badge cleared. "Back Home" successfully navigated to `/inventory.html`.
- **Status:** **PASS**
- **Severity:** Critical (S1)
