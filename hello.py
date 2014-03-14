from flask import Flask, request, render_template
from telapi import rest


app = Flask(__name__)

@app.route('/')
def hello():
	user = { 'name': 'Yedid' }
	return render_template('test_template.html', title = 'Home', user = user)

@app.route('/sms')
def sms():
	sms_body = request.args.get('Body', None)
	return sms_body


	

if __name__ == '__main__':
	app.run()