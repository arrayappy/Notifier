from twilio.rest import Client
import configparser
Config = configparser.ConfigParser()
Config.read("config.ini")
account_sid = Config.get('Twilio','accountSid') 
auth_token= Config.get('Twilio','authToken')
messaging_service_sid = Config.get('Twilio','messagingServiceSid')
NUMBERS = Config.get('Numbers', 'SMSMe').split(",")

def send_sms(msg):
    client = Client(account_sid, auth_token)
    for num in NUMBERS:
        message = client.messages \
            .create(
                body=msg,
                messaging_service_sid=messaging_service_sid,
                to=num
            )

        print(message.sid)

#send_sms("hai")