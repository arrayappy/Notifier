from twilio.rest import Client

from config_loader import config_loader
listObj=config_loader()

account_sid = listObj[1]['accountSid']
auth_token = listObj[1]['authToken']
messaging_service_sid = listObj[1]['messagingServiceSid']
NUMBERS = [listObj[1]['twilio_phone_number1'], listObj[1]['twilio_phone_number2']]
def send_sms(msg):
    client = Client(account_sid, auth_token)
    for num in NUMBERS:
        message = client.messages \
            .create(
                body=msg,
                messaging_service_sid=messaging_service_sid,
                to=num
            )