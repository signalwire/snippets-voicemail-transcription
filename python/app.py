import os
import requests
import pprint

from signalwire.voice_response import VoiceResponse, Say, Gather, Record
from flask import Flask,request

app = Flask(__name__)

# Entry point for incoming calls, prompts to leave a voice mail for processing.
@app.route('/voice_entry', methods=['GET', 'POST'])
def voice_entry():
    response = VoiceResponse()
    response.say("Please leave a message at the beep. Press the pound key when finished.")
    response.record(finishOnKey="#", maxLength="1", action="/hangup", transcribe="true", transcribeCallback="/transcribe_webhook", recordingStatusCallback="/recording_webhook")
    # return response
    return str(response)

# The webhook that is called when a transcription is received, this will process the transcription actions.
@app.route('/transcribe_webhook', methods=['GET','POST'])
def transcribe_webhook():

    pprint.pprint(request.values)

    # Recording Information
    recording_duration = request.values.get("RecordingDuration")
    recording_url = request.values.get("RecordingUrl")
    
    # Send Email
    send_email(request.values.get('TranscriptionText'))
    return "200"

# The webhook that is called on recording updates
@app.route('/recording_webhook', methods=['GET','POST'])
def recording_webhook():
    # For information only, and to show what is returned.
    pprint.pprint(request.values)

    return "200"

# Terminates the call
@app.route('/hangup', methods=['GET','POST'])
def hangup():
    response = VoiceResponse()
    response.say('Thank you! Good Bye!')
    response.hangup()
    return str(response)

# Sends the email provided using mailgun
def send_email(body):
    return requests.post(
        "https://api.mailgun.net/v3/" + os.environ['MAILGUN_DOMAIN'] + "/messages",
        auth=("api", os.environ['MAILGUN_API_TOKEN']),
        data={"from": os.environ['EMAIL_FROM'],
              "to": [os.environ['EMAIL_TO']],
              "subject": os.environ['EMAIL_SUBJECT'],
              "text": body })
              
# Default Route
@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
