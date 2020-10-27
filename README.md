# Snippets Voicemail Transcription
This snippet will show you how to implement transcribing a recorded voicemail message.
## About Voicemail Transcription
Easily create a quick transcription service that will email the contents of the voice mail.
## Getting Started
You will need a machine with Python installed, the SignalWire SDK, a provisioned SignalWire phone number, and optionally Docker if you decide to run it in a container.

For this demo we will be using Python, but more languages may become available.
- [x] Python
- [x] SignalWire SDK
- [x] SignalWire Phone Number
- [x] Docker (Optional)
----
## Running Voicemail Transcription - How It Works
We are going to build off of our Simple IVR Menu, and add ring groups

## Methods and Endpoints
```
Endpoint: /voice_entry
Methods: GET OR POST
Handles incoming voice requests
```
```
Endpoint: /transcribe_webhook
Methods: GET OR POST
Processes the transcription actions, i.e Sending Email.
```
```
Endpoint: /recording_webhook
Methods: GET OR POST
Provided for informational purposes, if you would like to see the recording status information.
```
```
Endpoint: /hangup
Methods: GET OR POST
Handles voice hangup.
```

## Setup Your Enviroment File

1. Copy from 'example.env' and fill in your values
2. Save new file called '.env'

Your file should look something like this
```
## This is the full name of your SignalWire Space. e.g.: example.signalwire.com
MAILGUN_DOMAIN=
MAILGUN_API_TOKEN=
EMAIL_FROM=
EMAIL_TO=
EMAIL_SUBJECT=Voicemail Transcription

```

## Build and Run on Docker
Lets get started!
1. Use our pre-built image from Docker Hub 
```
For Python:
docker pull signalwire/snippets-voicemail-transcription:latest
```
(or build your own image)

1. Build your image
```
docker build -t snippets-voicemail-transcription .
```
2. Run your image
```
docker run --publish 5000:5000 --env-file .env snippets-voicemail-transcription
```
3. The application will run on port 5000

## Build and Run Natively
For Python
```
1. Replace environment variables
2. From command line run, python3 app.py
```

----
# More Documentation
You can find more documentation on LaML, Relay, and all Signalwire APIs at:
- [SignalWire Python SDK](https://github.com/signalwire/signalwire-python)
- [SignalWire API Docs](https://docs.signalwire.com)
- [SignalWire Github](https://gituhb.com/signalwire)
- [Docker - Getting Started](https://docs.docker.com/get-started/)
- [Python - Gettings Started](https://docs.python.org/3/using/index.html)

# Support
If you have any issues or want to engage further about this Signal, please [open an issue on this repo](../../issues) or join our fantastic [Slack community](https://signalwire.community) and chat with others in the SignalWire community!

If you need assistance or support with your SignalWire services please file a support ticket from your Dashboard. 

