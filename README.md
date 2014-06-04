# Twilio Click-To-Call

This example project demonstrates how to set up a click-to-call service
for adverts in a web application.

This example project use the Twilio Client Javascript library to place phone
calls to a call center, over the web, with additional information about which advert has been
clicked. This additional information is passed along with the Twilio call request, and using [Pusher][2], is
delivered to the call center in real-time as the call is placed.

The application is built in Python, but there are plenty of [examples][1] for setting
up Twilio in other languages.


[1]: https://www.twilio.com/docs/quickstart
[2]: https://pusher.com
