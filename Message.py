from twilio.rest import Client

# Twilio credentials
account_sid = 'AC9bd8b3073158ac220cbd30d3ee1408a1'
auth_token = '[AuthToken]'
twilio_phone_number = '+254703297902'
messaging_service_sid = 'your_messaging_service_sid_with_no_reply'

# Recipient's phone number
recipient_phone_number = '+254703297902'

# Message content
message_body = 'Hello! Please com with the Christian Union book on sunday.'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send SMS notification
message = client.messages.create(
    body=message_body,
    messaging_service_sid=messaging_service_sid,
    to=recipient_phone_number
)

print("SMS notification sent successfully!")