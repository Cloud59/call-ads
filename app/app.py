from flask import Flask, request, render_template, g

from twilio.twiml import Response
from twilio.util import TwilioCapability

caller_id = '+441803506012'
default_client = 'anonymous'

app = Flask(__name__)


def build_twilio_token(client_name):

    # Find these values at twilio.com/user/account
    account_sid = ""
    auth_token = ""

    cap = TwilioCapability(account_sid, auth_token)

    app_sid = ''
    cap.allow_client_outgoing(app_sid)
    cap.allow_client_incoming(client_name)

    return cap.generate()


@app.route('/', methods=['GET', 'POST'])
def index():

    client_name = request.values.get('client', None) or default_client

    token = build_twilio_token(client_name)

    return render_template('index.html', token=token,
                           client_name=client_name)


@app.route('/control/', methods=['GET', 'POST'])
def controller():

    token = build_twilio_token('Admin')

    return render_template('control.html', token=token,
                           client_name='Admin')


@app.route('/voice/', methods=['GET', 'POST'])
def generate_voice_twiml():

    client_name = request.values.get('client', None) or default_client

    r = Response()

    with r.dial(callerId=caller_id) as r:
        r.client(default_client)

    return r.toxml()


if __name__ == '__main__':
    app.run(debug=True)
