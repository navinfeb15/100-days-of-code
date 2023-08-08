
# San Francisco Rental Research

This Python script scrapes rental property listings from Zillow for San Francisco and submits the rental information to a Google Form.

## Prerequisites

- Python 3.x
- `pip` package manager
- Selenium library (`pip install selenium`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- ChromeDriver - WebDriver for Chrome (Download and installation instructions: https://chromedriver.chromium.org/home)

## Setup

1. Clone the repository or download the script file (`sf_rental_research.py`).

2. Install the required Python libraries by running the following command in your terminal or command prompt:

   ```
   pip install selenium beautifulsoup4
   ```

3. Download ChromeDriver and extract the executable file to a suitable location on your computer.

4. Update the `executable_path` variable in the script (`sf_rental_research.py`) to the path where you placed the ChromeDriver executable:

   ```python
   self.service = Service(executable_path='C:/path/to/chromedriver.exe', chrome_options=chrome_options)
   ```

5. Configure other script variables if needed:
   - `GOOGLE_FORM_LINK`: Google Form link for submitting the rental information.
   - `SF_RENTAL_LINK`: Zillow link for searching rental properties in San Francisco.

## Usage

1. Open a terminal or command prompt and navigate to the directory where the `sf_rental_research.py` script is located.

2. Run the script using the following command:

   ```
   python sf_rental_research.py
   ```

3. The script will open a Chrome browser (in headless mode) and scrape rental property listings from Zillow for San Francisco.

4. Once the scraping is complete, the script will submit the rental information to the specified Google Form.

## Notes

- The script uses Selenium and ChromeDriver to automate the web scraping process. It also utilizes BeautifulSoup for HTML parsing.

- The script handles the CAPTCHA verification by temporarily opening Google Images before accessing Zillow. This helps bypass the CAPTCHA page.

- The script scrolls to the end of the Zillow page to load all rental listings before scraping.

- Ensure that you have a stable internet connection during the execution of the script.

- The rental information, including property links, prices, and addresses, will be submitted to the specified Google Form.

Feel free to customize the script or modify it according to your specific requirements.

If you have any questions or encounter any issues, please don't hesitate to reach out.

Happy rental research!

## License

This project is licensed under Free [MIT License](LICENSE).