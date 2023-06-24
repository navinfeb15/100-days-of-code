# Day-49

# Tinder Auto Liker

This Python script uses Selenium to automatically like Tinder profiles by emulating user actions. It can log in to Tinder using Facebook authentication and start liking profiles until the like limit is reached.

## Requirements

- Python 3
- Selenium WebDriver for Chrome (ChromeDriver)
- Chrome browser

## Installation

1. Clone the repository or download the code.

2. Install the required packages using pip:

```bash
pip install selenium
```

3. Download the ChromeDriver executable and place it in the `C:\Program Files\Chrome Driver\` directory. Make sure it matches your Chrome browser version. ChromeDriver can be downloaded from: https://sites.google.com/a/chromium.org/chromedriver/downloads

4. Replace the Facebook login credentials in the script with your own Facebook email and password:

```python
# Replace these with your Facebook login credentials
fb_username.send_keys("your_facebook_email")
fb_pswd.send_keys("your_facebook_password")
```

## Usage

1. Run the script using the following command:

```bash
python tinder_auto_liker.py
```

2. The script will open the specified Tinder link and log in using your Facebook credentials. It will then start liking profiles automatically until the like limit is reached or an error occurs.

3. The script will handle popups for cookies, location access, notifications, and homescreen access automatically if they appear during the execution.

4. If the script encounters any errors or runs out of likes, it will print an error message and terminate the program.

## Notes

- Make sure you have a stable internet connection while running the script.

- The script will control the browser and interact with Tinder on your behalf. Use it responsibly and only in compliance with Tinder's terms of service.

- The provided XPaths are based on the current structure of the Tinder website as of the last update. If the structure of the Tinder website changes in the future, you might need to update the XPaths accordingly.

- If you encounter issues related to ChromeDriver or Chrome browser version, consider updating the ChromeDriver or using a compatible version.

- The script is intended for educational purposes only and comes with no warranty. Use it at your own risk.

## License

This project is licensed under the [MIT License](LICENSE).