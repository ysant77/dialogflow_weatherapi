This repository is used with Google Dialogflow API. Google Dialogflow helps to capture
the intents and the dialogflow_weatherforecast is a simple flask application which 
responds to the User's question on google dialog flow and returns the response.

Currently the dialogflow bot is only trained on the sequence to ask what is weather of any city. Ex: What is the weather in Singapore?

Default answer to this is Weather in singapore is cloudy. The API give the actual response.

Steps to run:

1) Install the packages using commandL pip install -r requirements.txt
2) Run the flask application as: flask run --port 5000
3) Download and run ngrok locally and map it to port number 5000.
4) Go to dialogflow dashboard. Import the agent using weatheragent.zip file. Enable the fulfillments and insert the ngrok public url there.
5) Query using dialogflow in browser. The response should be from API.
