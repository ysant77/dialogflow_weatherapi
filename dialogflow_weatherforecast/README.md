Intent name should be getWeatherInfo and the parameter name for singapore should be geo-country.

Example queries:

What does the weather look like in Singapore
Weather in Singapore

Response is: 

The weather of Singapore is broken clouds

		
Steps to run:

1) Run ngrok using the command: ngrok http <<port_no>>
2) Run flask application using the command: flask run --port <<port_no>>

Note: above two ports must match

3) Paste the public https link of ngrock in fulfillment of google cloud dialog and Save.

4) The query should now be answered by the locally hosted flask api
