

from twilio.rest import Client
auth_token = 'auth-token'
account_sid = 'account-sid'
client = Client(account_sid, auth_token)

def send_sms(number, message):
    message = client.messages.create(
    from_='+12513151891',
    body=message,
    to='+91'+number
    )

    print(message.sid)