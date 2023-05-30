# Day-35
# README

# Stock Trading  Notification System

This is a  Python script  that sends notifications to a phone number when the percentage change in the  stock price  of a particular company is greater than or equal to 5%. The script uses the  Alpha Vantage API  to get the  stock price data  and the  News API  to get the latest  news articles  related to the company.

## Prerequisites

Before running the script, you must have the following:

-   Python 3.6 or later installed on your system
-   A free Alpha  Vantage API  key
-   A free News API key
-   A free  Twilio account
-   A phone number that can receive SMS messages

## Installation

1.  Clone the repository from  GitHub  using the following command:
  
	```
	git clone https://github.com/navinfeb15/100-days-of-code.git
	```
    
2.  Change into the project directory:
       ```
    cd stock-trading-notification
	   ```
    
3.  Install the required libraries using pip:
    
    ```
    pip install -r requirements.txt
    ```
    
    
    
4.  Sign up for an  [Alpha Vantage API key](https://www.alphavantage.co/support/#api-key)  and a  [News API key](https://newsapi.org/register).
    
5.  Create a  [Twilio account](https://www.twilio.com/try-twilio)  if you don't already have one. You will need to verify your  phone number  during the registration process.
    
6.  Obtain your  Twilio account SID  and  authentication token  from the  [Twilio console](https://www.twilio.com/console).
    
7.  Update the following placeholders in the  `main.py`  file with your own  API key, authentication token, and phone numbers:
    
    -   `STOCK_API_KEY`: Replace with your  Alpha  Vantage API key.
    -   `NEWS_API_KEY`: Replace with your  News API key.
    -   `account_sid`: Replace with your Twilio account SID.
    -   `auth_token`: Replace with your  Twilio authentication  token.
    -   `from_`: Replace with your  Twilio phone  number.
    -   `to`: Replace with the recipient's phone number.

## Usage

To run the script, execute the following command from the  project directory:

```
python main.py
```

The script will fetch the stock price data for the company specified in the  `STOCK`  variable from the  Alpha Vantage  API. It will then calculate the  percentage change  in the stock price between the last two days and determine if it is greater than or equal to 1%.

If the percentage change is greater than or equal to 1%, the script will fetch the top 3 news articles related to the company from the News API. It will then send a notification to the phone number specified in the  `to`  variable using the  Twilio API.

The notification will include the following information:

-   The percentage change in the stock price and whether it has gone up or down
-   The headline of the  news article
-   A brief summary of the news article

## Contributing

Contributions are welcome! If you find a bug or have a  feature request, please open an issue or a pull request.
## License

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT).