# Day-50

# LinkedIn Job Application Automation

## Overview

This Python script automates the job application process on LinkedIn. It logs in to your LinkedIn account using your Google credentials, searches for job opportunities related to specific technologies (e.g., Python, Django, Git, HTML, CSS) in Chennai, Tamil Nadu, India, and automatically applies to the jobs that match the criteria.

## Requirements

- Python 3.x
- Selenium library
- ChromeDriver

## Installation

1. Make sure you have Python 3.x installed on your system. If you don't have it, you can download it from the official website: https://www.python.org/downloads/

2. Install the Selenium library using pip:

```bash
pip install selenium
```

3. Download the ChromeDriver executable from the official website that matches your Chrome browser version and operating system: https://sites.google.com/a/chromium.org/chromedriver/downloads

4. Extract the downloaded ChromeDriver executable (chromedriver.exe) and place it in the `C:\Program Files\Chrome Driver\` directory.

## Configuration

Before running the script, you need to set up your LinkedIn and Google account credentials:

```python
LINKEDIN_USERNAME = "<YOUR_LINKED_IN_USERNAME>"
LINKEDIN_PASSWORD = "<YOUR_LINKED_IN_PASSWORD>"
```

## Usage

1. Open the Python script in a text editor or IDE of your choice.

2. Configure the `GOOGLE_USERNAME` and `GOOGLE_PASSWORD` variables with your LinkedIn account's Google credentials.

3. Optionally, you can update the `known_tech` list with additional technologies to search for specific job opportunities.

4. Run the script:

```bash
python linkedin_job_automation.py
```

5. The script will open a Chrome browser and navigate to the LinkedIn job search page for the specified location and technologies.

6. It will log in to your LinkedIn account using the provided Google credentials.

7. The script will start automatically applying to the relevant job opportunities based on the specified criteria. It will go through the job listings, click on the job, and proceed with the application process if the "Apply" button is available.

8. If the script encounters any issues during the application process, it will log the error and continue with the next job listing.

## Important Note

- Please use this script responsibly and only for personal use. Automating large-scale job applications or violating LinkedIn's terms of service may result in account suspension or other consequences.

---

Please remember that using automation scripts on websites like LinkedIn might violate their terms of service. It's essential to be cautious and use automation responsibly. Always ensure you comply with the website's policies and do not engage in any activities that may lead to adverse consequences for your account or actions.

## License

This project is licensed under Free [MIT License](LICENSE).