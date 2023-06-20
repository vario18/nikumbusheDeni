import os
import re
import africastalking
from dotenv import load_dotenv

load_dotenv()


class SendSMS():

    def __init__(self) -> None:
        self.username = os.getenv('AFRICAS_TALKING_USERNAME')
        self.api_key = os.getenv('AFRICAS_TALKING_API_KEY')

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        self.sms = africastalking.SMS

    def send(self, number: str, owner: str, amount: int, plate: str):
        # Set the numbers in international format
        recipients = [number]

        # Set your message
        message = f"Ndugu  {owner}, Gari lako namba: {plate}. Linadaiwa Tshs {amount}/=. Tafadhali lipia. \n #NikumbusheDeni"

        # Set your shortCode or senderId
        # sender = "AFRICASTKNG"

        try:
            response = self.sms.send(message, recipients)
            print(response)

        except Exception as e:
            print(f'we have a problem: {e}')
