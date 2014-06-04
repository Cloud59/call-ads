# Twilio Click-To-Call

This example project demonstrates how to set up a click-to-call service
for adverts in a web application.

This example project use the Twilio Client Javascript library to place phone
calls to a call center, over the web, with additional information about which advert has been
clicked. This additional information is passed along with the Twilio call request, and using [Pusher][2], is
delivered to the call center in real-time as the call is placed.

The application is built in Python, but there are plenty of [examples][1] for setting
up Twilio in other languages.

# Setup

If you want to download this code to see how it works, follow these steps:

1. Download the entire project off Github
2. Navigate to the call-ads folder in terminal
3. Install the requirements with ```pip install -r requirements.txt```
4. Start the server using Python: ```python app/app.py```
5. Navigate to localhost:5000 to view the website running


[1]: https://www.twilio.com/docs/quickstart
[2]: https://pusher.com
