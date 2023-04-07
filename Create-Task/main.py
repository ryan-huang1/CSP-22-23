from flask import json
from flask import request
from flask import Flask
import message_helper

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'hello world!'

@app.route('/message_recive', methods=['POST'])
def message_handeler():
    print('JSON message: ' + json.dumps(request.json)) 
    if request.headers['Content-Type'] == 'application/json':
        print("message recived")
        payload = request.json
        
        # Extract and print the 'text' value from the JSON payload
        text_value = payload['text']
        print('Text from JSON message:', text_value)
        
        if internal_check(payload):
            internal_drafter(payload)

        else:
            external_drafter(payload)

        return 'JSON message: ' + json.dumps(request.json)

def internal_check(payload):
    # Check if the recipient's phone number matches the expected value
    if payload['recipient'] == '+13365824875':
        return True
    else:
        return False

def internal_drafter(payload):
    print("internal message drafted")

def external_drafter(payload):
    print("message drafted")

# TO EXPOSE THE FLASK APP TO THE INTERNET, USE THE FOLLOWING COMMAND:
# ngrok http 4999
if __name__ == '__main__':
    app.run(host='localhost', port=4999, debug=True)