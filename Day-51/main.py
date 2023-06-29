from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
import speedtest

class InternetSpeedTwitterBot:
    def __init__(self):
        # Twitter login credentials
        self.TWITTER_EMAIL = "<YOUR_TWITTER_EMAIL>"
        self.TWITTER_PASSWORD = "<YOUR_TWITTER_PASSWORD>"
        self.TWITTER_USERNAME = "<YOUR_TWITTER_USERNAME>"

        # URL for Twitter login page
        self.URL = "https://twitter.com/i/flow/login"

        # Set Chrome options to disable notifications and initialize WebDriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        service = Service(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe', chrome_options=chrome_options)
        self.driver = webdriver.Chrome(service=service)

    def get_internet_speed(self):
        # Get the internet speed using Speedtest
        st = speedtest.Speedtest()
        st.get_best_server()
        download = round(st.download()/1000/1000, 1)
        upload = round(st.upload()/1000/1000, 1)
        result = f"{download}down/{upload}up"
        message = f"Hey internet provider, why is my internet speed {result}, when I pay for 300down/300up?"
        return message

    def post_to_twitter(self):
        # Open the Twitter login page
        self.driver.get(self.URL)
        time.sleep(5)

        # Find the username input field and enter the Google username
        username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'r-30o5oe')))
        username.send_keys(self.TWITTER_EMAIL)
        time.sleep(5)

        # Find the next button and click to proceed to the password input page
        username_next = self.driver.find_element(By.CLASS_NAME, 'css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu')
        username_next.click()
        time.sleep(2)

        # Check if there is a verification step and handle it
        verification = self.driver.find_elements(By.XPATH, "//span[text()='There was unusual login activity on your account. To help keep your account safe, please enter your phone number or username to verify it’s you.']")
        if verification:
            self.driver.find_element(By.CSS_SELECTOR, 'input.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu').send_keys(self.TWITTER_USERNAME)
            self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
        time.sleep(2)

        # Find the password input field and enter the Google password
        password = self.driver.find_element(By.CSS_SELECTOR, 'input.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu')
        password.send_keys(self.TWITTER_PASSWORD)
        time.sleep(2)

        # Find the password next button and click to log in
        password_next = self.driver.find_element(By.CLASS_NAME, 'css-1dbjc4n.r-pw2am6')
        password_next.click()
        time.sleep(10)

        # Check if there is a security boost prompt and handle it
        if self.driver.find_elements(By.XPATH, "//span[text()='Boost your account security']"):
            self.driver.find_element(By.CLASS_NAME, 'css-901oao.r-1awozwy.r-6koalj.r-18u37iz.r-16y2uox.r-37j5jr.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0').click()

        # Find the tweet input field and post the message with internet speed
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')))
        msg = self.get_internet_speed()
        element.send_keys(msg)

        # Find the tweet button and click to post the tweet
        self.driver.find_element(By.CLASS_NAME, 'css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr').click()


# Create an instance of the Twitter bot and post the tweet
start_bot = InternetSpeedTwitterBot()
start_bot.post_to_twitter()
