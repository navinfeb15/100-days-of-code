from twilio.rest import Client
from data_manager import DataManager
import smtplib


class NotificationManager:
    """This class is responsible for sending notifications via SMS using the Twilio API."""

    def __init__(self, deals, records):
        self.deals = deals
        self.records = records
        self.account_sid = "AC70c2d9568e8697cc25467fb084e74034"
        self.auth_token = "<AUTH TOKEN>"

    def send_alert(self):
        """Sends an SMS notification with the best flight deals."""
        self.message_content = f"only Rs.{self.deals[0]['flight_price']} to fly from Chennai-MAA to {self.records['to_city']}-{self.deals[0]['fly_to']} on {self.deals[0]['dep_date']}"
        self.has_stopover = self.deals[1].get("has_stopover")
        self.stopover = self.deals[1].get("stopover_city")
        if self.stopover:
            self.message_content += f"\nFlight has 1 stop over, {self.stopover} City"

        # Send message to phone number
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=message_content,
            from_='+14849699513',  # Your Twilio phone number
            to='+917338961810'  # The recipient's phone number
        )
        print(self.message_content)

    def send_mail(self):
        self.message_content = f"only Rs.{self.deals[0]['flight_price']} to fly from Chennai-MAA to {self.records['to_city']}-{self.deals[0]['fly_to']} on {self.deals[0]['dep_date']}"
        self.has_stopover = self.deals[1].get("has_stopover")
        self.stopover = self.deals[1].get("stopover_city")
        if self.stopover:
            self.message_content += f"\nFlight has 1 stop over, {self.stopover} City"
        self.message_content += "\n{self.deals[0]['deal_link']}"

        data_manager = DataManager()
        users = data_manager.get_user_mail()

        for to_address in users:
            if to_address:
                my_email = "navinfeb15@gmail.com"
                password = "<MAIL APP PASSWORD>"
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=self.message_content)
                    connection.close()