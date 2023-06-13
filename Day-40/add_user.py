import requests


class addUser:
    def __init__(self):
        self.url_endpoint = "https://api.sheety.co/081557a0ce02affee27d6b05aee415b0/flightDeals/users"
        TOKEN = "a;wlrkjf3wq[app;'';rkfq[p'akfr[p"
        self.SHEETY_HEADERS = {"Authorization": f"Bearer {TOKEN}"}
        
        firstname = input("Welcome to the Flight Club.\nwe find the best flight deals and email you.\nWhat is your first name?\n")
        lastname = input("What is your last name?\n")
        
        email_match = False
        while not email_match:
            check_email_1 = input("what is your email?\n")
            check_email_2 = input("Enter your email again.\n")
            if check_email_1 == check_email_2:
                email_match = True
            else:
                print("email do not match. Try again !")

        self.sheety_params = {
            "user": 
                {
                "firstName": firstname,
                "lastName": lastname,
                "email": check_email_1 
            }
        }
            
        resp = requests.post(url=self.url_endpoint, json = self.sheety_params, headers = self.SHEETY_HEADERS)
        print(resp.text)

        