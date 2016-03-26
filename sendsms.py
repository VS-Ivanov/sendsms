import flask
from flask import render_template, request, url_for
import sms

app = flask.Flask('__name__')

# @app.route('/')
@app.route('/index', methods=['POST','GET'])
@app.route('/send', methods=['POST','GET'], endpoint='send')
@app.route('/about',endpoint='about')

def index():

	if request.method == 'GET':

		if request.args.get('mes') == 'sms_inbox':
			mes = sms.get_sms_inbox()
		elif request.args.get('mes') == 'sms_outbox':
			mes = sms.get_sms_outbox()
		elif request.arg.get('mes') == 'ussd_inbox':
			mes = sms.get_ussd_inbox()
		elif request.arg.get('mes') == 'ussd_outbox':
			mes = sms.get_ussd_outbox()
		else:
			mes = sms.get_sms_inbox()
	else:
		mes = sms.get_sms_inbox()

	return render_template("sendsms.html",title='Send sms',messages=mes)

def send():
	return 'Send message...'

def about():
	return 'About this application...'

app.run(debug=True)