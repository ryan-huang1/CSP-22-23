from flask import json
from flask import request
from flask import Flask
import message_helper

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'empty page'

@app.route('/message_recive', methods=['POST'])
def message_handeler():
    if request.headers['Content-Type'] == 'application/json':
        print("message recived")
        payload = request.json
        
        if internal_check(payload):
            internal_drafter(payload)

        else:
            external_drafter(payload)

        return 'JSON message: ' + json.dumps(request.json)
    
def internal_check(payload):
    if payload['msisdn'] == "13365824875":
        return True
    else:
        return False
    
def internal_drafter(payload):
    print("internal message drafted")
    
def external_drafter(payload):
    print("message drafted")

if __name__ == '__main__':
    app.run(host='localhost', port=4999, debug=True)