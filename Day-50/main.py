from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

# Your LinkedIn username and password
LINKEDIN_USERNAME = "<YOUR_LINKED_IN_USERNAME>"
LINKEDIN_PASSWORD = "<YOUR_LINKED_IN_PASSWORD>"
known_tech = ["python", "django", "git", 'html', "css"]
SEARCH_JOB = True

URL = r"https://www.linkedin.com/jobs/search/?currentJobId=3669963950&f_LF=f_AL&geoId=114467055&keywords=python&location=Chennai%2C%20Tamil%20Nadu%2C%20India&refresh=true"

# Set Chrome options to disable notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize the Chrome WebDriver
service = Service(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe', chrome_options=chrome_options)
driver = webdriver.Chrome(service=service)

driver.get(URL)
driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()

# Login to LinkedIn
username_textbox = driver.find_element(By.XPATH, '//*[@id="username"]')
password_textbox = driver.find_element(By.XPATH, '//*[@id="password"]')

username_textbox.send_keys(LINKEDIN_USERNAME)
password_textbox.send_keys(LINKEDIN_PASSWORD)

login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
login_button.click()

# Wait for login to complete (You may use WebDriverWait here)
time.sleep(3)

while SEARCH_JOB:
    jobs_list = driver.find_element(By.CLASS_NAME, 'scaffold-layout__list-container').find_elements(By.CSS_SELECTOR, 'li.ember-view.jobs-search-results__list-item')

    for job in jobs_list:
        job.click()
        time.sleep(3)

        title = job.find_element(By.CSS_SELECTOR, 'div.artdeco-entity-lockup__title').text
        apply_job_button = driver.find_elements(By.CSS_SELECTOR, 'div.jobs-apply-button--top-card')

        if apply_job_button:
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, 'div.jobs-apply-button--top-card').click()

            # Proceed with the job application process
            mobile_next_button = driver.find_element(By.CLASS_NAME, 'artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
            mobile_next_button.click()

            resume_next_button = driver.find_element(By.CLASS_NAME, 'artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
            resume_next_button.click()

            # Check for additional questions (if any) and fill out the form
            try:
                before_notice = driver.find_elements(By.ID, 'text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3634680894-93217843-multipleChoice')
                if before_notice:
                    before_notice[1].select_by_index(2)

                # Filtering job preferences (You may need to update these XPATHs)
                work_exp = driver.find_elements(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3669963950-93872021-numeric"]')
                if work_exp:
                    work_exp[0].send_keys('2')

                git_exp = driver.find_elements(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3669963950-93872013-numeric"]')
                if git_exp:
                    git_exp[0].send_keys('2')

                django_exp = driver.find_elements(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3669963950-93872005-numeric"]')
                if django_exp:
                    django_exp[0].send_keys('1')

                location_option = driver.find_elements(By.XPATH, '//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3669963950-93871997-multipleChoice"]')
                if location_option:
                    location_option.select_by_index(1)

                review_button = driver.find_elements(By.XPATH, '//*[@id="ember606"]')
                if review_button:
                    review_button.click()

                unfollow_company = find_element(By.ID, 'follow-company-checkbox')
                unfollow_company.click()

                submit_app = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')
                submit_app.click()

                submit_close = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/button')
                submit_close.click()

                # Print success message if applied successfully
                job_name = driver.find_element(By.XPATH, r'//*[@id="ember688"]/h3')
                print(f"Applied to {job_name.text}")
            except Exception as e:
                # Handle any exceptions or errors during the application process
                # If there is a popup with an error message, close it and continue
                if driver.find_elements(By.CSS_SELECTOR, 'h3.jpac-modal-header'):
                    driver.find_element(By.CSS_SELECTOR, 'h3.artdeco-modal__dismiss.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--2').click()
                    continue
                else:
                    print("NOT APPLIED: ", title)

                # If an error occurs during the application process, continue with the next job
                cancel_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/button/li-icon')
                cancel_button.click()
                time.sleep(1)
                discard_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/button[1]/span')
                discard_button.click()
                continue

    # Move to the next page if available, otherwise exit the loop
    next_page = driver.find_elements(By.XPATH, "//li[contains(@class, 'artdeco-pagination__indicator artdeco-pagination__indicator--number active selected')]/following-sibling::li")
    if next_page:
        next_page[0].click()
    else:
        SEARCH_JOB = False