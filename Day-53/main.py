from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


class SfRentalResearch:
    def __init__(self):
        # Google Form link for submitting the rental information
        self.GOOGLE_FORM_LINK = "https://forms.gle/Rk5uhoZStSYMWtbi6"
        # Zillow link for searching rental properties in San Francisco
        self.SF_RENTAL_LINK = r"https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
        self.is_site_available = False

        self.property_links = []
        self.property_price = []
        self.property_address = []

        # Configure Chrome options for WebDriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")
        chrome_options.add_argument("--headless")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.service = Service(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe', chrome_options=chrome_options)
        
    def get_rental(self):
        # Check if the Zillow site is available for scraping
        while self.is_site_available == False:
            self.driver = webdriver.Chrome(service=self.service)
            self.actions = ActionChains(self.driver)

            # Open Google Images to bypass the CAPTCHA
            self.driver.get("https://images.google.com/")
            time.sleep(2)
            
            # Open the Zillow rental listings page for San Francisco
            self.driver.get(self.SF_RENTAL_LINK)
            time.sleep(5)

            # Check if the CAPTCHA page is displayed
            if not self.driver.find_elements(By.CSS_SELECTOR,'div.px-captcha-message'):
                self.is_site_available = True 
            else:
                self.driver.quit()

        # Scroll to the end of the page to load all rental listings
        last_property = self.driver.find_elements(By.CSS_SELECTOR,'.ListItem-c11n-8-84-3__sc-10e22w8-0.StyledListCardWrapper-srp__sc-wts.0-1')
        self.driver.execute_script("arguments[0].scrollIntoView();", last_property[-1])
        time.sleep(5)

        # Get the HTML content of the page
        html = self.driver.page_source
        self.driver.quit()

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Find all the rental property listings
        listings = soup.find_all("div", class_="ListItem-c11n-8-84-3__sc-10e22w8-0 StyledListCardWrapper-srp__sc-wts.ekg0m9h0")
        
        # Extract the property details from each listing
        for listing in listings:
            link = listing.find("a", class_="list-card-link list-card-link-top-margin list-card-img")['href']
            price = listing.find("div", class_="list-card-price").text
            address = listing.find("address", class_="list-card-addr").text

            self.property_links.append(link)
            self.property_price.append(price)
            self.property_address.append(address)

    def submit_rental_info(self):
        # Open the Google Form for submitting rental information
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.GOOGLE_FORM_LINK)
        time.sleep(2)

        # Fill in the rental information in the Google Form
        for i in range(len(self.property_links)):
            link_field = self.driver.find_element(By.CSS_SELECTOR, 'input[name="entry.1234567890"]')
            price_field = self.driver.find_element(By.CSS_SELECTOR, 'input[name="entry.0987654321"]')
            address_field = self.driver.find_element(By.CSS_SELECTOR, 'input[name="entry.2468135790"]')

            link_field.send_keys(self.property_links[i])
            price_field.send_keys(self.property_price[i])
            address_field.send_keys(self.property_address[i])

            submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button[jsname="M2UYVd"]')
            submit_button.click()
            time.sleep(2)

        self.driver.quit()


# Create an instance of the SfRentalResearch class
research = SfRentalResearch()

# Get the rental information from Zillow
research.get_rental()

# Submit the rental information to Google Form
research.submit_rental_info()