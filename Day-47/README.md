# Day-47

# Amazon Price Tracker

This program tracks the price of a product on Amazon and sends an  email notification  if the price drops below a specified target price.

## Dependencies

-   `requests`: to make HTTP requests to the Amazon website
-   `smtplib`: to send  email notifications
-   `time`: to add a delay between price checks
-   `bs4`: to parse  HTML content  and extract information

## Usage

1.  Set the  `Target_price`  variable to the desired target price for the product.
2.  Set the  `PRODUCT_URL`  variable to the URL of the product on Amazon.
3.  Set the  `HEADERS`  variable to the desired  HTTP headers  for the requests.
4.  Set the  `my_email`  and  `password`  variables to the sender's email and password, respectively.
5.  Set the  `to`  variable to the recipient's email address.
6.  Run the program.

## Functions

### `get_price()`

This function makes an HTTP request to the  Amazon website, extracts the product title and price from the HTML content using  Beautiful Soup, and returns them as a list. If the price is not found, the function waits for 3 seconds and calls itself recursively.

### `send_mail()`

This function sends an email notification to the recipient's  email address  using the SMTP protocol. The email contains the product title,  current price, and  product URL.

## Example
```
Target_price = 300
PRODUCT_URL = "https://www.amazon.in/CZARTECH-Cover-OnePlus-Hybrid-Transparent/dp/B09CYMGGC1/"
HEADERS = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'    
}

product_details = get_price()
if float(product_details[1]) < Target_price:
    send_mail()

```

In this example, the program tracks the price of a  phone case  on Amazon and sends an email notification if the price drops below Rs. 300.

## Contributions

  

Contributions are welcome! If you find any bugs or have any suggestions for improvement, please feel free to create a pull request or open an issue.
## License

  

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).