# Day-35
# README
# Rain Alert

Rain Alert  is a  Python script  that sends an  SMS  message via  Twilio  to alert you if it's going to rain in the next 12 hours in a specified location. It uses the  OpenWeatherMap API  to retrieve weather data.

## Getting Started

### Prerequisites

Before you can use this script, you will need:

-   A  Twilio account  with a  verified phone  number
-   An  OpenWeatherMap  API key

### Installation

1.  Clone the repository:
    
    Copy
    
    ```
    git clone https://github.com/your-username/rain-alert.git
    ```
    
    
    ```
    
2.  Install the required Python packages:

    
    ```
    pip install -r requirements.txt
    ```
     
3.  Set the following environment variables:
    
    -   `TW_AUTH_TOKEN`: Your  Twilio auth  token
    -   `OWM_API_KEY`: Your OpenWeatherMap API key
    
    You can set these  environment variables  in your shell or by creating a  `.env`  file in the project directory and storing the values there:
    
    Copy
    
    ```
    TW_AUTH_TOKEN=your-twilio-auth-token
    OWM_API_KEY=your-openweathermap-api-key
    ```
    
    ```
    

### Usage

To run the script, simply execute the  `rain_alert.py`  file:


```
python rain_alert.py

```

If it's going to rain in the next 12 hours in the specified location, you will receive an  SMS message  from Twilio.

### Customization

You can customize the location by modifying the  `lat`  and  `lon`  parameters in the  `parameters`  dictionary in  `rain_alert.py`. You can also customize the message that is sent by modifying the  `body`  parameter in the  `client.messages.create()`  method.


## License

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT).