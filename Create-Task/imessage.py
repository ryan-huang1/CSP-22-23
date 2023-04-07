import requests
import os

# Define the URL of the LoopMessage API endpoint
url = 'https://server.loopmessage.com/api/v1/message/send/'

# Define the headers for the request
headers = {
    'Authorization': os.environ.get('loop_auth'),
    'Loop-Secret-Key': os.environ.get('loop_secret'),
    'Content-Type': 'application/json'
}

RECIPIENT_PHONE_NUMBER = "13365824875"
MESSAGE_TEXT = "Hello, World!"
SENDER_NAME = "Ryan"

# Define the body parameters for the request
data = {
    'recipient': '+13365824875',
    'text': 'Hello, World!',
    'sender_name': 'ryan@gmail.com'
}

# Make the POST request to the LoopMessage API
response = requests.post(url, headers=headers, json=data)

# Print the response status code and JSON response
print(response.status_code)
print(response.json())