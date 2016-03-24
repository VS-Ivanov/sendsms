import flask
from flask import render_template

app = flask.Flask('__name__')

@app.route('/')
@app.route('/index')

def index():
	user = {'nickname':'VS.Ivanov'}
	return render_template("sendsms.html",title='Sens sms',user = user)

app.run()