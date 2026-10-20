import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

BASE_DIR = r"C:\Users\BIT\.gemini\antigravity\scratch\ecommerce-manual-testing"
PDF_PATH = os.path.join(BASE_DIR, "Ecommerce_Manual_Testing_Complete_Guide_Interview_Prep.pdf")

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#4A5568"))

        # Header on later pages
        if self._pageNumber > 1:
            self.drawString(36, 762, "E-Commerce Manual Testing Guide & Interview Prep (Easy Language Edition)")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.5)
            self.line(36, 756, 576, 756)

        # Footer on all pages
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(576, 25, footer_text)
        self.drawString(36, 25, "SauceDemo Manual QA Portfolio Guide • Made for Beginners & Job Seekers")
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.5)
        self.line(36, 35, 576, 35)

        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=46,
        bottomMargin=46
    )

    styles = getSampleStyleSheet()

    c_navy = colors.HexColor("#1B365D")
    c_blue = colors.HexColor("#2B6CB0")
    c_dark = colors.HexColor("#2D3748")
    c_box_bg = colors.HexColor("#EDF2F7")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=c_navy,
        spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=10
    )
    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=16,
        textColor=c_navy,
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13.5,
        textColor=c_blue,
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=c_dark,
        spaceAfter=4
    )
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=c_dark,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3
    )
    q_style = ParagraphStyle(
        'Question',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=13,
        textColor=c_navy,
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True
    )
    a_style = ParagraphStyle(
        'Answer',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=c_dark,
        leftIndent=8,
        spaceAfter=5
    )
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=c_dark
    )
    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.white
    )

    story = []

    # Title & Intro Banner
    story.append(Paragraph("E-Commerce Website Manual Testing: Complete Guide & Interview Prep", title_style))
    story.append(Paragraph("A Step-by-Step Practical Handbook Written in Easy, Simple Language for QA Beginners", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_navy, spaceAfter=8))

    meta_table_data = [
        [
            Paragraph("<b>Website Tested:</b> SauceDemo (saucedemo.com)", table_cell),
            Paragraph("<b>Testing Type:</b> Manual, Functional, Negative", table_cell),
            Paragraph("<b>Pass Rate:</b> 90.00% (27 Passed, 3 Failed)", table_cell)
        ],
        [
            Paragraph("<b>User Tested:</b> standard_user / secret_sauce", table_cell),
            Paragraph("<b>Tools Used:</b> Browser, Google Sheets/Excel, GitHub", table_cell),
            Paragraph("<b>Bugs Found:</b> 6 Real Defect Reports", table_cell)
        ]
    ]
    meta_table = Table(meta_table_data, colWidths=[180, 180, 180])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_box_bg),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 8))

    # SECTION 1: What is this project about?
    story.append(Paragraph("1. What Is This Project About? (In Simple Words)", h1_style))
    story.append(Paragraph(
        "Imagine you are shopping on an online store like Amazon or Flipkart. Your goal is simple: log in, pick a product, "
        "add it to your cart, fill in your delivery address, check the total bill, and pay. "
        "As a <b>Manual QA Tester</b>, your job is NOT to build this website. Your job is to <b>test every single step</b> "
        "to check whether it works smoothly for real users, and to catch mistakes (bugs) before customers get frustrated.",
        body_style
    ))
    story.append(Paragraph(
        "<b>The Shopping Journey We Tested:</b>"
        "<br/>1. <b>Login:</b> Entering username and password to enter the store."
        "<br/>2. <b>Product Catalog:</b> Viewing 6 items with their photos, descriptions, and prices."
        "<br/>3. <b>Sorting:</b> Changing product order (Name A-Z, Z-A, Price Low-High, Price High-Low)."
        "<br/>4. <b>Shopping Cart:</b> Adding products, checking the red badge counter (1, 2, 3), and deleting items."
        "<br/>5. <b>Checkout Step 1:</b> Filling in First Name, Last Name, and Postal/Zip code."
        "<br/>6. <b>Checkout Step 2:</b> Verifying price calculations (Subtotal + 8% Sales Tax = Final Grand Total)."
        "<br/>7. <b>Confirmation:</b> Reaching the 'Thank you for your order!' screen and returning home.",
        body_style
    ))
    story.append(Spacer(1, 6))

    # SECTION 2: Step-by-Step QA Workflow
    story.append(Paragraph("2. The 7 Project Stages Explained Step-by-Step", h1_style))
    stages = [
        ("Stage 1: Exploring the Website First",
         "Never write tests blindly. First, open https://www.saucedemo.com. Click around like a real user. See what happens when you add items, when you leave fields blank, or when you type wrong passwords. Once you understand the normal flow, you are ready to write tests."),

        ("Stage 2: Creating the Test Plan",
         "A Test Plan is simply a roadmap. It answers: What are we testing? (Login, cart, checkout). What are we NOT testing? (Payment gateways, backend databases). What tools will we use? (Chrome, Excel). When are we done? (When all 30 tests are run and the pass rate is at least 85%)."),

        ("Stage 3: Writing 30 Clear Test Cases",
         "A test case is like a cooking recipe with steps and an expected outcome. For example: Step 1 - Enter valid username. Step 2 - Enter valid password. Step 3 - Click Login. Expected Result: User lands on products page."),

        ("Stage 4: Executing Tests on the Live Website",
         "You open the website, follow the steps exactly, and write down what REALLY happened (Actual Result). If expected matches actual, it is a PASS. If not, it is a FAIL. Out of 30 tests, 27 Passed and 3 Failed (giving a 90% Pass Rate)."),

        ("Stage 5: Reporting Genuine Defects (Bugs)",
         "When a test fails, you write a bug report. You explain: What went wrong? How to reproduce it step-by-step? How serious is it? We found 6 real defects (such as being allowed to checkout with 0 items in the cart!)."),

        ("Stage 6: Writing the Final Test Execution Report",
         "A summary for managers showing total tests run, how many passed, how many failed, what bugs were found, and our final recommendation: The website is mostly good, but 2 major bugs must be fixed before public launch."),

        ("Stage 7: Publishing Your Work on GitHub",
         "We uploaded the Test Plan, Test Cases, Bug Reports, Excel files, and PDF to GitHub so recruiters can click the link and see your proof of work immediately.")
    ]
    for s_title, s_desc in stages:
        story.append(Paragraph(f"• <b>{s_title}:</b> {s_desc}", bullet_style))

    story.append(Spacer(1, 6))

    # SECTION 3: Key QA Concepts
    story.append(Paragraph("3. Important Testing Concepts Explained in Plain English", h1_style))

    story.append(Paragraph(
        "<b>A. Equivalence Class Partitioning (ECP) — 'Group Similar Inputs':</b><br/>"
        "Instead of testing 1,000 different wrong passwords, you group inputs into buckets. "
        "Bucket 1: Valid credentials (standard_user / secret_sauce). "
        "Bucket 2: Wrong password (standard_user / wrong123). "
        "Bucket 3: Empty inputs (leaving username or password blank). "
        "Testing just one from each bucket gives 100% confidence without wasting time.",
        body_style
    ))

    story.append(Paragraph(
        "<b>B. Boundary Value Analysis (BVA) — 'Test at the Edges':</b><br/>"
        "Errors usually happen at the boundaries (limits). "
        "For example, the boundary of a shopping cart is <b>0 items</b> vs. <b>1 item</b>. "
        "When we tested 0 items, we caught Bug BUG-02: the app let us click 'Checkout' even though the cart had nothing in it! "
        "Another boundary is price: verifying the lowest price ($7.99 Onesie) up to the highest price ($49.99 Fleece Jacket).",
        body_style
    ))

    story.append(Paragraph(
        "<b>C. Negative Testing — 'Trying to Break the App':</b><br/>"
        "Positive testing is entering correct data. Negative testing is entering wrong data on purpose: "
        "typing symbols in postal code (!@#$%), leaving mandatory fields empty, or trying to access /inventory.html without logging in. "
        "The app must gracefully show an error banner instead of crashing.",
        body_style
    ))

    story.append(Paragraph(
        "<b>D. Financial Tax Calculation Math (8.00% Tax):</b><br/>"
        "E-commerce apps must calculate taxes accurately to 2 decimal places. We checked SauceDemo's tax formula: "
        "<br/>• We picked 2 items: Backpack ($29.99) + Bike Light ($9.99) = <b>$39.98 Subtotal</b>"
        "<br/>• Tax at 8.00% = 39.98 * 0.08 = 3.1984 -> Rounded to 2 decimals = <b>$3.20 Tax</b>"
        "<br/>• Grand Total = $39.98 + $3.20 = <b>$43.18</b>"
        "<br/>The website showed exactly $39.98, $3.20, and $43.18. This proved the financial calculation was 100% accurate.",
        body_style
    ))
    story.append(Spacer(1, 6))

    # SECTION 4: Test Cases Summary
    story.append(Paragraph("4. Quick Summary of the 30 Test Cases", h1_style))
    tc_quick_data = [
        [Paragraph("Range", table_header), Paragraph("Module", table_header), Paragraph("What We Tested", table_header), Paragraph("Result", table_header)],
        [Paragraph("TC01 - TC08", table_cell), Paragraph("Login & Auth", table_cell), Paragraph("Valid login, wrong password, blank username, blank password, locked user, password masking, logout", table_cell), Paragraph("8 / 8 Pass", table_cell)],
        [Paragraph("TC09", table_cell), Paragraph("Security", table_cell), Paragraph("Direct URL access to /inventory.html without logging in (Redirects to login with error)", table_cell), Paragraph("1 / 1 Pass", table_cell)],
        [Paragraph("TC10 - TC16", table_cell), Paragraph("Catalog & Sort", table_cell), Paragraph("6 items display, 4 sorting options (A-Z, Z-A, Low-High, High-Low), item details page, search bar check", table_cell), Paragraph("6 Pass, 1 Fail (No search bar)", table_cell)],
        [Paragraph("TC17 - TC22", table_cell), Paragraph("Shopping Cart", table_cell), Paragraph("Add single/multi items, cart badge count (1->2->3), remove from catalog, remove from cart, page reload persistence", table_cell), Paragraph("6 / 6 Pass", table_cell)],
        [Paragraph("TC23 - TC27", table_cell), Paragraph("Checkout Form", table_cell), Paragraph("Empty cart checkout, missing First Name, missing Last Name, missing Zip, special characters in Zip", table_cell), Paragraph("3 Pass, 2 Fail (Empty cart & Zip regex)", table_cell)],
        [Paragraph("TC28 - TC30", table_cell), Paragraph("Tax & Complete", table_cell), Paragraph("Cancel checkout, 8% tax and subtotal math verification, finish order, thank you banner, Reset App State", table_cell), Paragraph("3 / 3 Pass", table_cell)]
    ]
    t_quick = Table(tc_quick_data, colWidths=[70, 85, 305, 80])
    t_quick.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_navy),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F7FAFC")]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_quick)
    story.append(Spacer(1, 8))

    # SECTION 5: Defects Found
    story.append(Paragraph("5. The 6 Genuine Bugs We Found (Explained Simply)", h1_style))
    bugs = [
        ("BUG-01: No Search Bar Available (Medium Severity)",
         "In any real shopping site, customers expect a search box at the top to type 'shirt' or 'bag'. In SauceDemo, there is no search bar at all. Customers can only sort with a dropdown."),

        ("BUG-02: User Can Checkout with an Empty Cart (High Severity)",
         "If your cart has 0 items, the 'Checkout' button should be greyed out (disabled). In SauceDemo, you can click Checkout, enter your address, and place an order for $0.00! In real life, this creates ghost orders and wastes warehouse time."),

        ("BUG-03: Postal Code Accepts Weird Symbols like !@#$% (Medium Severity)",
         "The Zip Code field accepts any random characters like '!@#$%^&*()'. It does not check if the postal code is actually numbers or valid letters. This can cause shipping delivery packages to get lost."),

        ("BUG-04: 'Remove' Button Doesn't Work on Inventory Page for problem_user (High Severity)",
         "SauceDemo provides a test user named 'problem_user'. When you add an item and click 'Remove' on the catalog page, nothing happens! The button stays 'Remove' and the item remains in the cart."),

        ("BUG-05: Broken Product Photos Showing Dog Pictures (Low Severity)",
         "For 'problem_user', all product photos fail to load and show the exact same photo of a dog with a camera. This looks unprofessional and confuses buyers."),

        ("BUG-06: Last Name Field is Frozen and Cannot Be Typed (Critical Severity)",
         "For 'problem_user', you cannot type your Last Name during checkout. Because Last Name is required, the user is permanently blocked and can NEVER complete their purchase.")
    ]
    for b_title, b_desc in bugs:
        story.append(Paragraph(f"• <b>{b_title}:</b> {b_desc}", bullet_style))

    story.append(Spacer(1, 8))

    # SECTION 6: Interview Questions & Answers
    story.append(Paragraph("6. Top QA Interview Questions & Answers (Speak Like a Pro)", h1_style))

    qa_list = [
        ("1. Tell me about this E-Commerce testing project.",
         "I tested an online shopping website called SauceDemo. I tested the complete customer journey from login, to searching and sorting products, adding items to the cart, filling in the checkout form, verifying the 8% tax calculation, and finishing the order. I wrote 30 test cases, ran them all, achieved a 90% pass rate, and found 6 real bugs—including a major bug where users can checkout with 0 items in their cart."),

        ("2. What is Boundary Value Analysis? Did you use it?",
         "Boundary Value Analysis means testing the edges or limits of an input, because developers most often make mistakes at boundaries. I used it on the shopping cart: the minimum allowed boundary to checkout should be 1 item. When I tested 0 items (below boundary), I discovered that the website still allowed me to checkout, which is a real bug!"),

        ("3. What is the difference between Severity and Priority? Give examples from your project.",
         "Severity is how badly the bug damages the system technically. Priority is how quickly developers need to fix it.<br/>"
         "Example of High Severity + High Priority: When using problem_user, the Last Name field freezes, blocking checkout completely. No customer can buy anything (Critical/P1).<br/>"
         "Example of Medium Severity + Medium Priority: The missing search bar (BUG-01). Users can still buy items using sorting, so it's not blocking sales immediately, but it hurts usability."),

        ("4. How did you verify the price and tax calculation?",
         "I picked two products: Sauce Labs Backpack ($29.99) and Bike Light ($9.99). Their subtotal was $39.98. The website charges 8% tax. I calculated 39.98 * 0.08 = 3.1984. Rounding to 2 decimal places gives $3.20 tax. Adding $39.98 + $3.20 gave a grand total of $43.18. I compared this with the screen, and the website matched my math with 100% precision."),

        ("5. What will you do if a developer says 'The empty cart checkout is not a bug'?",
         "I will politely explain the business impact: allowing orders with 0 items creates $0 invoices, triggers automatic confirmation emails to customers, and creates confusing orders in the warehouse logistics queue. If we still disagree, I will bring the issue to the Product Owner with clear steps and let them decide based on business rules."),

        ("6. What is the difference between Smoke Testing and Regression Testing?",
         "Smoke Testing is a quick check to see if basic core features work before doing deep testing (e.g., Can the user log in and view products?). Regression Testing is re-running old tests after a bug fix to make sure the fix didn't break anything that used to work."),

        ("7. What are the essential fields in a good Bug Report?",
         "A great bug report needs: 1. Bug ID, 2. Clear Title/Summary, 3. Severity and Priority, 4. Environment (Browser/OS), 5. Step-by-step reproduction instructions, 6. Expected Result, 7. Actual Result, and 8. Screenshots or video proof.")
    ]

    for q, a in qa_list:
        story.append(Paragraph(f"<b>{q}</b>", q_style))
        story.append(Paragraph(f"<b>How to Answer:</b> {a}", a_style))

    story.append(Spacer(1, 8))

    # SECTION 7: Resume Bullets & Elevator Pitch
    story.append(Paragraph("7. Resume Bullet Points & 30-Second Elevator Pitch", h1_style))
    story.append(Paragraph("<b>4 Concise Resume Bullet Points (Copy & Paste):</b>", h2_style))
    story.append(Paragraph("• <b>Executed 30 manual test cases</b> for an e-commerce platform covering login, catalog sorting, cart management, and checkout, achieving a <b>90% pass rate</b>.", bullet_style))
    story.append(Paragraph("• <b>Applied ECP and BVA techniques</b> to validate form inputs, negative edge cases, and verify <b>8.00% sales tax and price calculations</b>.", bullet_style))
    story.append(Paragraph("• <b>Identified and logged 6 defects in Jira format</b> with clear reproduction steps, including a high-severity bug allowing checkout with an empty cart.", bullet_style))
    story.append(Paragraph("• <b>Authored full QA documentation</b>—including an IEEE 829 Test Plan, test matrices, and execution reports—published on GitHub.", bullet_style))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>30-Second Elevator Pitch (For HR / Recruiter Phone Calls):</b>", h2_style))
    story.append(Paragraph(
        "<i>\"I recently completed an end-to-end manual QA testing project on an e-commerce website. "
        "I designed and executed 30 test cases covering authentication, product sorting, cart operations, form validation, and tax calculations. "
        "I applied testing methods like Equivalence Partitioning and Boundary Value Analysis to find edge cases, and I documented 6 real bugs in Jira format. "
        "All my test plans, Excel sheets, and reports are published on my GitHub. I am ready to bring this structured testing approach to your QA team!\"</i>",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Clean, easy-language PDF generated successfully at:", PDF_PATH)

if __name__ == "__main__":
    build_pdf()
