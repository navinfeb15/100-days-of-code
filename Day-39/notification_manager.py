from twilio.rest import Client


class NotificationManager:
    """This class is responsible for sending notifications via SMS using the Twilio API."""

    def __init__(self, deals, records):
        self.deals = deals
        self.records = records
        self.account_sid = "AC70c2d9568e8697cc25467fb084e74034"
        self.auth_token = "c4cbd5289497cec10430cd67f7ce799f"

    def send_alert(self):
        """Sends an SMS notification with the best flight deals."""
        message_content = f"only Rs.{self.deals[0]['flight_price']} to fly from Chennai-MAA to {self.records['to_city']}-{self.deals[0]['fly_to']} on {self.deals[0]['dep_date']}"
        # Send message to phone number
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=message_content,
            from_='+14849699513',  # Your Twilio phone number
            to='+917338961810'  # The recipient's phone number
        )