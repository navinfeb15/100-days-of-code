import smtplib
import time
import bs4
import requests

# Set the target price for the product
Target_price = 300

# Set the URL of the product on Amazon
PRODUCT_URL = "https://www.amazon.in/CZARTECH-Cover-OnePlus-Hybrid-Transparent/dp/B09CYMGGC1/"

# MAIL OF THE RECIEVER
TO_EMAIL = "<EMAIL OF RECIEVER>"

# Set the HTTP headers for the requests
HEADERS = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'    
}

# Get the current price of the product from Amazon
def get_price():
    # Make an HTTP request to the Amazon website
    response = requests.get(url=PRODUCT_URL, headers= HEADERS)
    # Parse the HTML content of the response using Beautiful Soup
    soup = bs4.BeautifulSoup(response.text,"lxml")
        
    global price, title
    price = None
    while price is None:
        try:
            # Extract the product price from the HTML content
            price = soup.find_all("span", class_="priceToPay")[0].find_all("span")[1].find_all("span")[1].getText()
            # Extract the product title from the HTML content
            title = soup.find_all("span", id="productTitle")[0].getText().strip()
        except IndexError:
            pass
        except Exception as e:
            print(e)
        
        # If the price is not found, wait for 3 seconds and try again
        if price is None:
            time.sleep(3)
            get_price()
    return [title,price]

# Send an email notification if the price drops below the target price
def send_mail():
    # Set the sender's email address and password
    my_email = "<YOUR MAIL>"
    password = "<YOUR GOOGLE APP PASSWORD>"
    # Set the recipient's email address
    to = "navinfeb15@gmail.com"
    # Set the email message
    message = f"Subject:Amazon Price Alert !\n\n{product_details[0]} is now Rs.{product_details[1]}\n{PRODUCT_URL}"

    # Send the email notification using the SMTP protocol
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to, msg=message)

# Get the current price of the product
product_details = get_price()
# Send an email notification if the price is lower than the target price
if float(product_details[1]) < Target_price:
    send_mail()