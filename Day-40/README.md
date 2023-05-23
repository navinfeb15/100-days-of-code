
# Flight Deals  Finder


## New Functionality

A new functionality has been added to this script. The functionality is designed to get users'  email addresses, store them in the  Google Sheet, and then email them price changes in flight tickets. This feature can be useful for users who want to be notified of price changes in real-time and take advantage of the best deals.

To use this feature, follow these steps:

1.  Add a new column to the Google Sheet named "Email".
    
2.  Enter the email addresses of users who want to receive notifications in the "Email" column.
    
3.  Update the  `config.json`  file with your  Gmail address  and password.
    
4.  Run the script with the following command:
    ```
    python main.py --email
    ```
    

The script will search for the cheapest flights to each city in the Google Sheet and compare the prices to the threshold value. If the price is below the threshold, the script will send an  email notification  to all email addresses listed in the "Email" column.

Note: This feature requires authentication with your  Gmail  account. Please ensure that you have enabled "Less secure app access" in your  Gmail account  settings.

---


This script searches for the cheapest flights to cities in a  Google Sheet  and sends notifications when the price drops below a certain threshold.

## Getting Started

### Prerequisites

-   Python 3.x
-   Google API  credentials
-   Twilio  API credentials (if using SMS notifications)

### Installation

1.  Clone this repository to your local machine.
    
2.  Install the required Python packages:
    
    
    ```
    pip install -r requirements.txt
    ```
    
3.  Obtain  Google API credentials  and save the  `credentials.json`  file to the  project directory.
    
4.  Create a  `.env`  file in the project directory and add your  Twilio API credentials  (if using  SMS notifications):
    
    Copy
    
    ```
    TWILIO_ACCOUNT_SID=your_account_sid
    TWILIO_AUTH_TOKEN=your_auth_token
    TWILIO_FROM_NUMBER=your_twilio_phone_number
    ```
    
5.  Create a  `config.json`  file in the project directory and add the following information:
    
    ```
    {
        "google_sheet_id": "your_sheet_id",
        "google_sheet_name": "Sheet1",
        "gmail_user": "your_gmail_address",
        "gmail_password": "your_gmail_password",
        "threshold": 10000
    }
    ```

## Usage

1.  Run the script with the following command:
    
    ```
    python main.py
    ```
  
2.  The script will search for the cheapest flights to each city in the Google Sheet and compare the prices to the  threshold value.
    
3.  If the price is below the threshold, the script will send an email or  SMS notification  (depending on your configuration).
    

## Contributing

Contributions are welcome! Please create a  pull request  with your changes.
## License

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT).