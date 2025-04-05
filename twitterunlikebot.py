from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === SETTINGS ===
USERNAME = ""
CHROMEDRIVER_PATH = ""

# === START CHROME ===
options = Options()
options.add_argument("--start-maximized")
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# === GO TO TWITTER AND LOGIN ===
driver.get("https://twitter.com/login")

# Enter username
username_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "text")))
username_input.send_keys(USERNAME)

# Click the "Next" button
next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]')))
next_button.click()

# Wait for the password screen to load
password_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
password_input.send_keys("your_password")  # Enter your password here

# Click the "Log in" button
login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Log in"]')))
login_button.click()

# After logging in, go to the likes page
driver.get(f"https://twitter.com/{USERNAME}/likes")

input("Please complete the login and press ENTER...")

# === XPATH LIST ===
UNLIKE_XPATHS = [
    '//div[@data-testid="unlike"]',
    '//div[@aria-label="Beğeniyi kaldır"]',
    '//div[@aria-label="Unlike"]',
    '//button[@data-testid="unlike"]'
]

# === SCROLL FUNCTION ===
def scroll_down():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# === FIND UNLIKE BUTTONS FUNCTION ===
def find_unlike_buttons():
    """ Try different XPATHs to find the unlike buttons """
    for xpath in UNLIKE_XPATHS:
        try:
            buttons = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath))
            )
            if buttons:
                return buttons
        except Exception as e:
            print(f"XPath error: {e}")
            continue
    return []

# === UNLIKE FUNCTION ===
def unlike_visible_tweets():
    unliked_count = 0

    while True:
        unlike_buttons = find_unlike_buttons()
        if not unlike_buttons:
            print("All likes have been removed or no new likes found.")
            break

        for button in unlike_buttons:
            try:
                button.click()
                unliked_count += 1
                print(f"Like removed, total: {unliked_count}")
                time.sleep(1)  # Reduced wait time to 1 second for faster processing
            except Exception as e:
                print(f"Click error: {e}, Button: {button}")

        scroll_down()  # Scroll to load more likes

    print(f"Total likes removed: {unliked_count}")

# === EXECUTE ===
unlike_visible_tweets()

# === CLOSE THE BROWSER AFTER COMPLETION ===
driver.quit()
