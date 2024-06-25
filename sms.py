import os
import africastalking
from dotenv import load_dotenv

load_dotenv()


class SMSNotifier:
    def __init__(self) -> None:
        # Load the required credentials from environment variables
        self.username = os.getenv("AFRICAS_TALKING_USERNAME")
        self.api_key = os.getenv("AFRICAS_TALKING_API_KEY")

        # Initialize the AfricasTalking SDK
        africastalking.initialize(self.username, self.api_key)

        # Create an instance of the SMS service
        self.sms_service = africastalking.SMS

    def send_sms(
        self, recipient_number: str, owner_name: str, amount_due: int, plate_number: str
    ):
        # Set the recipient number in international format
        recipients = [recipient_number]

        # Compose the SMS message
        message = f"Dear {owner_name}, your vehicle with plate number {plate_number} has an outstanding balance of Tshs {amount_due}/=. Please make payment. \n #NikumbusheDeni"

        try:
            # Send the SMS
            response = self.sms_service.send(message, recipients)
            print(response)

        except Exception as e:
            print(f"An error occurred while sending the SMS: {e}")
