from flask import Flask, request, render_template, g

from twilio.util import TwilioCapability

from pusher import Pusher

# Twilio number and default client name
caller_id = 'PHONE_NUMBER'
default_client = 'anonymous'

# Pusher credentials found at https://app.pusher.com/
p_app_id='PUSHER_APP_ID'
p_key='PUSHER_KEY'
p_secret='PUSHER_SECRET'

app = Flask(__name__)


def build_twilio_token(client_name):

    # Find these values at twilio.com/user/account
    account_sid = "TWILIO_ACCOUNT_SID"
    auth_token = "TWILIO_AUTH_TOKEN"

    cap = TwilioCapability(account_sid, auth_token)

    app_sid = ''
    cap.allow_client_outgoing(app_sid)
    cap.allow_client_incoming(client_name)

    return cap.generate()


@app.route('/', methods=['GET', 'POST'])
def index():

    client_name = request.values.get('client', None) or default_client

    token = build_twilio_token(client_name)

    return render_template(
        'index.html',
        token=token,
        client_name=client_name
    )


@app.route('/control/', methods=['GET', 'POST'])
def controller():

    token = build_twilio_token('Admin')

    return render_template(
        'control.html',
        token=token,
        client_name='Admin',
        pusher_key=p_key
    )


@app.route('/voice/', methods=['GET', 'POST'])
def generate_voice_twiml():

    item = request.values.get('item', None)
    name = request.values.get('name', None)

    p = Pusher(p_app_id, p_key, p_secret)

    p['twilio_call_center'].trigger(
        'new_caller',
            {
                'item': item,
                'name': name
            }
        )

    return '<Response><Dial><Client>Admin</Client></Dial></Response>'

if __name__ == '__main__':
    app.run(debug=True)
