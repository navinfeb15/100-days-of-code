import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class InstaFollower:
    def __init__(self):
        # Replace with your Instagram login credentials and target page
        self.INSTAGRAM_EMAIL = "<YOUR_TWITTER_EMAIL>"
        self.INSTAGRAM_PASSWORD = "<YOUR_TWITTER_PASSWORD>"
        self.TARGET_PAGE =  "<YOUR_TARGET_PAGE>"
        self.URL = "https://www.instagram.com"

        # Set Chrome options to disable notifications and initialize WebDriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        service = Service(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe', chrome_options=chrome_options)
        self.driver = webdriver.Chrome(service=service)
        self.actions = ActionChains(self.driver)

    def login(self):
        # Open Instagram login page and wait for the page to load
        self.driver.get(self.URL)
        time.sleep(8)

        # Find the username and password input fields and enter login credentials
        username = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(self.INSTAGRAM_EMAIL)

        password = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(self.INSTAGRAM_PASSWORD)

        # Find and click the login button
        login_button = self.driver.find_element(By.CLASS_NAME,'_acan._acap._acas._aj1-')
        login_button.click()

        time.sleep(5)
    
    def find_followers(self):
        # Construct the URL for the target page and navigate to it
        target_url = f"{self.URL}/{self.TARGET_PAGE}"
        self.driver.get(target_url)

        time.sleep(6)

        # Find and click the followers button on the target page
        followers = self.driver.find_element(By.CLASS_NAME,'x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._alvs._a6hd')
        followers.click()

        time.sleep(5)

        # Find all the follow buttons for the followers and store them in a list
        self.accounts_follow_button = self.driver.find_elements(By.CLASS_NAME,'_acan._acap._acas._aj1-')[1:]
        
    def follow(self):
        # Iterate through each follow button and click it
        for account in self.accounts_follow_button:
            self.actions.move_to_element(account).perform()
            account.click()
            time.sleep(1)
        
bot = InstaFollower()

# Call the methods to execute the bot actions
bot.login()
bot.find_followers()
bot.follow()
