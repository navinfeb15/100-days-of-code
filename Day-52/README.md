# Day-52


# Instagram Follower Bot

This Python script automates the process of logging into Instagram, navigating to a target page, and following its followers.

## Prerequisites

- Python 3.x
- `pip` package manager
- Selenium library (`pip install selenium`)
- ChromeDriver - WebDriver for Chrome (Download and installation instructions: https://chromedriver.chromium.org/home)

## Setup

1. Clone the repository or download the script file (`insta_follower.py`).

2. Install the required Python library by running the following command in your terminal or command prompt:

   ```
   pip install selenium
   ```

3. Download ChromeDriver and extract the executable file to a suitable location on your computer.

4. Update the `INSTAGRAM_EMAIL`, `INSTAGRAM_PASSWORD`, and `TARGET_PAGE` variables in the script (`insta_follower.py`) with your Instagram login credentials and the target page you want to follow the followers of:

   ```python
   self.INSTAGRAM_EMAIL = "<YOUR_INSTAGRAM_EMAIL>"
   self.INSTAGRAM_PASSWORD = "<YOUR_INSTAGRAM_PASSWORD>"
   self.TARGET_PAGE = "<YOUR_TARGET_PAGE>"
   ```

5. Update the `executable_path` variable in the script (`insta_follower.py`) to the path where you placed the ChromeDriver executable:

   ```python
   service = Service(executable_path='C:/path/to/chromedriver.exe', chrome_options=chrome_options)
   ```

## Usage

1. Open a terminal or command prompt and navigate to the directory where the `insta_follower.py` script is located.

2. Run the script using the following command:

   ```
   python insta_follower.py
   ```

3. The script will open a Chrome browser and automate the following actions:
   - Log into Instagram using the provided login credentials.
   - Navigate to the target page specified in the `TARGET_PAGE` variable.
   - Follow the followers of the target page.

4. The script includes appropriate delays (`time.sleep`) to ensure that the necessary elements are loaded before interacting with them.

## Notes

- The script uses Selenium and ChromeDriver to automate the web browsing actions.

- It sets Chrome options to disable notifications and uses a specific user agent for the browser.

- Ensure that you have a stable internet connection during the execution of the script.

- The script finds and clicks the followers button on the target page and then iterates through each follower's follow button to follow them.

- Customize the script by modifying the login credentials, target page, or any other relevant elements according to your requirements.

- Be cautious when using automation scripts on social media platforms to comply with their terms of service and avoid any violations.

If you have any questions or encounter any issues, please don't hesitate to reach out.

Happy Instagram automation!

## License

This project is licensed under Free [MIT License](LICENSE).