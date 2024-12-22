import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver using the Service class and ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# Function to ensure visibility of an element before interacting with it
def wait_for_element(locator, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element
    except Exception as e:
        print(f"Error waiting for element: {e}")
        return None


def log_and_wait(message, seconds=2):
    print(message)
    time.sleep(seconds)


# Test Homepage
def test_homepage():
    try:
        print("Testing homepage...")
        driver.get("file:///F:/sh/SWE_template/SWE-Phase3-isA/index-2.html")
        log_and_wait("Waiting for homepage to load...")
        WebDriverWait(driver, 10).until(EC.title_contains("Homepage Title"))
        print("Homepage loaded successfully.")
    except Exception as e:
        print(f"Error loading homepage: {e}")


# Test Sign-in functionality
def test_signin_signup():
    try:
        print("Testing Sign-in/Sign-up...")

        # Test Sign-up
        driver.get("file:///F:/sh/SWE_template/SWE-Phase3-isA/auth.html")

        sign_up_tab = wait_for_element((By.XPATH, "/html/body/div/div[1]/div[2]"))
        if sign_up_tab:
            sign_up_tab.click()
            log_and_wait("Sign-up tab clicked. Waiting...")

            full_name_input = wait_for_element((By.XPATH, "/html/body/div/div[2]/form[2]/input[1]"))
            email_input = wait_for_element((By.XPATH, "/html/body/div/div[2]/form[2]/input[2]"))
            password_input = wait_for_element((By.XPATH, "/html/body/div/div[2]/form[2]/input[3]"))
            confirm_password_input = wait_for_element(
                (By.XPATH, "/html/body/div/div[2]/form[2]/input[4]"))

            if full_name_input and email_input and password_input and confirm_password_input:
                full_name_input.send_keys("abeer")
                log_and_wait("Filling out Full Name...")
                email_input.send_keys("abeer@gmail.com")
                log_and_wait("Filling out Email...")
                password_input.send_keys("12346")
                log_and_wait("Filling out Password...")
                confirm_password_input.send_keys("12346")
                log_and_wait("Filling out Confirm Password...")

                sign_up_button = wait_for_element((By.XPATH, "/html/body/div/div[2]/form[2]/button"))
                if sign_up_button:
                    sign_up_button.click()
                    log_and_wait("Sign-up button clicked. Waiting for confirmation...")

        # Test Sign-in
        sign_in_tab = wait_for_element((By.XPATH, "/html/body/div/div[1]/div[1]"))
        if sign_in_tab:
            sign_in_tab.click()
            log_and_wait("Sign-in tab clicked. Waiting...")

            email_input = wait_for_element((By.XPATH, "/html/body/div/div[2]/form[1]/input[1]"))
            password_input = wait_for_element((By.XPATH, "/html/body/div/div[2]/form[1]/input[2]"))

            if email_input and password_input:
                email_input.send_keys("abeer@gmail.com")
                log_and_wait("Filling out Email...")
                password_input.send_keys("12346")
                log_and_wait("Filling out Password...")

                signin_button = wait_for_element((By.XPATH, "/html/body/div/div[2]/form[1]/button"))
                if signin_button:
                    signin_button.click()
                    log_and_wait("Sign-in button clicked. Waiting for confirmation...")

    except Exception as e:
        print(f"Error in Sign-in/Sign-up test: {e}")


# Test Product Search Page
def test_product_search():
    try:
        print("Testing Product Search and Add to Cart...")

        driver.get("file:///F:/sh/SWE_template/SWE-Phase3-isA/products.html")

        # Inspect the "Add to Cart" Button for Product 2
        product2_add_to_cart_button = wait_for_element(
            (By.XPATH, "/html/body/main/div[2]/button"))
        if product2_add_to_cart_button:
            product2_add_to_cart_button.click()
            log_and_wait("Product added to cart. Waiting for cart update...")

        log_and_wait("Staying on the Cart page...", 5)

        # Check cart page
        driver.get("file:///F:/sh/SWE_template/SWE-Phase3-isA/cart.html")
        cart_item = wait_for_element((By.XPATH, "/html/body/header/nav/a[5]"))

        if cart_item:
            print("Add to Cart test passed.")
        else:
            print("Add to Cart test failed: Cart not updated.")
    except Exception as e:
        print(f"Error in Product Search and Add to Cart test: {e}")


# Test Add to Cart Page
def test_add_to_cart():
    try:
        print("Testing Add to Cart...")

        driver.get("file:///F:/sh/SWE_template/SWE-Phase3-isA/cart.html")

        add_to_cart_button = wait_for_element((By.ID, "add_to_cart_button"))
        if add_to_cart_button:
            add_to_cart_button.click()

            log_and_wait("Waiting for cart item update...")
            cart_item_count = wait_for_element((By.ID, "cart_item_count"))
            if cart_item_count and cart_item_count.is_displayed():
                print("Add to Cart test passed.")
            else:
                print("Add to Cart test failed: Cart not updated.")
        else:
            print("Add to Cart button not found.")
    except Exception as e:
        print(f"Error adding product to cart: {e}")



# Test Services Page (Scroll down)
def test_services():
    try:
        print("Testing Services Page...")

        driver.get("file:///F:/sh/SWE_template/SWE-Phase3-isA/services.html")

        log_and_wait("Waiting to scroll down the page...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        log_and_wait("Scrolled to the bottom of the page.", 3)
        print("Services page test passed.")
    except Exception as e:
        print(f"Error in Services page test: {e}")


# Test Appointment functionality
def test_appointment():
    try:
        print("Testing Appointment Booking...")

        driver.get("file:///F:/sh/SWE_template/SWE-Phase3-isA/session.html")

        # Select Dr. Rima Seliman
        doctor_button = wait_for_element(
            (By.XPATH, "/html/body/main/div[1]/div/button"))
        if doctor_button:
            doctor_button.click()
            log_and_wait("Doctor button clicked. Waiting for appointment form...")

        # doctor_select = wait_for_element((By.XPATH, "//*[@name='doctor']"))
        date_input = wait_for_element((By.XPATH, "/html/body/div/div/form/input[2]"))
        time_input = wait_for_element((By.XPATH, "/html/body/div/div/form/input[3]"))
        name_input = wait_for_element((By.XPATH, "/html/body/div/div/form/input[4]"))
        contact_input = wait_for_element((By.XPATH, "/html/body/div/div/form/input[5]"))

        if date_input and time_input and name_input and contact_input:
            # doctor_select.send_keys("Dr. Anna Smith")
            date_input.send_keys("12/25/2024")
            log_and_wait("Filling out Date...")
            time_input.send_keys("10:30 AM")
            log_and_wait("Filling out Time...")
            name_input.send_keys("abeer")
            log_and_wait("Filling out Name...")
            contact_input.send_keys("01140506070")
            log_and_wait("Filling out Contact...")

            book_appointment_button = wait_for_element(
                (By.XPATH, "//*[@id='bookAppointment']"))
            if book_appointment_button:
                book_appointment_button.click()
                log_and_wait("Appointment booked. Waiting for confirmation...")

            # Check if the appointment confirmation is correct
            appointment_confirmation = wait_for_element(
                (By.XPATH, "/html/body/div/div/form/button"))
            if appointment_confirmation:
                print("Appointment test passed.")
            else:
                print("Appointment test failed.")
    except Exception as e:
        print(f"Error in Appointment test: {e}")


# Run all tests
test_homepage()
test_signin_signup()
test_product_search()
test_add_to_cart()
test_services()
test_appointment()

# Close the browser after the tests
driver.quit()
