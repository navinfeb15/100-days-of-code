# Day-51


# InternetSpeedTwitterBot

InternetSpeedTwitterBot is a Python script that automates posting internet speed information to Twitter. The script uses Selenium and Speedtest libraries to measure internet speed and post the results as a tweet on Twitter.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Selenium library (`pip install selenium`)
- Speedtest library (`pip install speedtest-cli`)
- Chrome WebDriver (ensure it matches your installed Chrome browser version)

## Setup

1. Clone the repository or download the `InternetSpeedTwitterBot.py` script.

2. Install the required libraries if you haven't already:

   ```bash
   pip install selenium
   pip install speedtest-cli
   ```

3. Download the Chrome WebDriver from the official website:
   [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

   Make sure to select the WebDriver version compatible with your installed Chrome browser version.

4. Update the `InternetSpeedTwitterBot.py` script with your Twitter and Google account credentials:

   ```python
   # Your Twitter username and password
    TWITTER_EMAIL = "<YOUR_TWITTER_EMAIL>"
    TWITTER_PASSWORD = "<YOUR_TWITTER_PASSWORD>"
    TWITTER_USERNAME = "<YOUR_TWITTER_USERNAME>"
   ```

5. Set the correct path to the downloaded Chrome WebDriver in the `InternetSpeedTwitterBot.py` script:

   ```python
   service = Service(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe', chrome_options=chrome_options)
   ```

## Usage

To run the script, simply execute the `InternetSpeedTwitterBot.py` file:

```bash
python InternetSpeedTwitterBot.py
```

The script will log in to your Twitter account using your Google credentials, measure the internet speed using Speedtest, and post the results as a tweet on your Twitter timeline.

Note: The script may require additional verification steps if Twitter detects unusual login activity. You might need to manually verify your account by providing your phone number or additional details during the first run.

## Important Notes

- Make sure to keep your Chrome browser updated to the latest version to avoid compatibility issues with the Chrome WebDriver.

- Twitter may have usage limitations or restrictions for automated posting. Be cautious about using this script frequently to avoid potential restrictions on your Twitter account.

- The script is provided for educational purposes and personal use only. The author is not responsible for any misuse or violation of Twitter's terms of service.

## License

This project is licensed under Free [MIT License](LICENSE).
