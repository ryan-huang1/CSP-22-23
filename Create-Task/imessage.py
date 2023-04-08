import requests
import os

def send_loop_message(recipient_phone_number, message_text, sender_name):
    # Define the URL of the LoopMessage API endpoint
    url = 'https://server.loopmessage.com/api/v1/message/send/'

    # Define the headers for the request
    headers = {
        'Authorization': os.environ.get('loop_auth'),
        'Loop-Secret-Key': os.environ.get('loop_secret'),
        'Content-Type': 'application/json'
    }

    # Define the body parameters for the request
    data = {
        'recipient': recipient_phone_number,
        'text': message_text,
        'sender_name': sender_name
    }

    # Make the POST request to the LoopMessage API
    response = requests.post(url, headers=headers, json=data)

    # Print the response status code and JSON response
    print(response.status_code)
    print(response.json())

# Example usage
RECIPIENT_PHONE_NUMBER = "+13365824875"
MESSAGE_TEXT = "Hello, World!"
SENDER_NAME = "Ryan"

send_loop_message(RECIPIENT_PHONE_NUMBER, MESSAGE_TEXT, SENDER_NAME)
