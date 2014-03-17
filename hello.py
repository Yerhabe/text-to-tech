from flask import Flask
from flask import request
from flask import render_template
from telapi import rest
import os
import psycopg2
import urlparse
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy

# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ["DATABASE_URL"])

# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

@app.route('/')
def hello():
	user = { 'name': 'Yedid' }
	return render_template('test_template.html', title = 'Home', user = user)

@app.route('/test/<name>')
def name(name):
	return "Hi Mr. {name}".format(name=name)

@app.route('/sms', methods = ['GET'])
def sms():
	sms_body = request.args.get('Body', None)
	from_number = request.args.get('To', None)
	to_number = request.args.get('From', None)
	time_stamp = datetime.now()


	
	# account_sid = 'ACec889084f5a483fc17fd4115b4be2b5e' 
	# auth_token = '86b901cc0c16475694d03c8e8bc9523b'
	# client = rest.Client(account_sid, auth_token)
	# account = client.accounts[client.account_sid]
 
	# from_number = request.args.get('To', None)
	# to_number = request.args.get('From', None)
	# body = "body: " + sms_body 
 
	# account.sms_messages.create(from_number = from_number, to_number = to_number, body = body)
 
	return "SMS Received"




if __name__ == '__main__':
	app.run()