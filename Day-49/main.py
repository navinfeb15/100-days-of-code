from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Your Facebook username and password
FB_USERNAME = "<YOUR FB USERNAME>"
FB_PASSWORD = "<YOUR FB PASSWORD>"

# Set Chrome options to disable notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize the Chrome WebDriver
service = Service(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe', chrome_options=chrome_options)
driver = webdriver.Chrome(service=service)

# URLs
one_link = "https://tinder.onelink.me/9K8a/3d4abb81"
url = "https://tinder.com/"

# Open the first URL
driver.get(one_link)
time.sleep(7)

# Get the handle of the first window
window_before = driver.window_handles[0]

# Locate and click the Facebook login button
login_fb_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div'))
)
login_fb_button.click()
time.sleep(2)

# Switch to the new Facebook login window
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

# Enter Facebook login credentials and click login
fb_username = driver.find_element(By.XPATH, '//*[@id="email"]')
fb_pswd = driver.find_element(By.XPATH, '//*[@id="pass"]')
fb_username.send_keys(FB_USERNAME)
fb_pswd.send_keys(FB_PASSWORD)
log_in = driver.find_element(By.NAME, 'login')
log_in.click()

# Switch back to the Tinder window
driver.switch_to.window(driver.window_handles[0])

# Set a flag to keep track of likes
like_empty = False

# Loop for liking profiles until likes are exhausted
while not like_empty:
    # Handle cookie accept popup if present
    cookie_accept = driver.find_elements(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
    if cookie_accept:
        cookie_accept[0].click()
    
    time.sleep(5)

    # Handle location allow popup if present
    location_allow = driver.find_elements(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
    if location_allow:
        location_allow[0].click()
    time.sleep(2)

    # Handle notification deny popup if present
    notification_deny = driver.find_elements(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
    if notification_deny:
        notification_deny[0].click()
    time.sleep(2)

    # Handle homescreen deny popup if present
    homescreen_deny = driver.find_elements(By.XPATH, '//*[@id="t223514671"]/main/div/div[2]/button[2]/div[2]/div[2]')
    if homescreen_deny:
        homescreen_deny[0].click()
    time.sleep(2)

    try:
        # Like the profile using Arrow Right key
        like = ActionChains(driver).send_keys(Keys.ARROW_RIGHT)
        like.perform()
        
        # Check for like limit popup
        likelimit_deny = driver.find_elements(By.XPATH, '//*[@id="t223514671"]/main/div/div[2]/button/svg')
        if likelimit_deny:
            like_empty = True
    except Exception as error:
        print("Ran out of likes\n", error)
        driver.quit()
