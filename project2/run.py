from flask import Flask,render_template,request,session,jsonify
import os
from models.fact_model import Message
from models.base_model import DBSingelton
from datetime import datetime

app = Flask(__name__)

@app.before_first_request
def initialize_tables():
	connect_db()
	if not Message.table_exists():
		Message.create_table()
	disconnect_db()

@app.before_request
def connect_db():
	DBSingelton.getInstance().connect()

@app.teardown_request
def disconnect_db(err=None):
	DBSingelton.getInstance().close()


@app.route('/')
def name():
	query = Message.select().dicts()
	return render_template('index.html',query=query)

@app.route('/message', methods=['POST','GET'])
def message():	
	if request.method == 'POST':
		session['is_submitted'] = True
		name = request.form.get('name_sth')
		message = request.form.get('message')
		title = request.form.get('title')
		email = request.form.get('mail')
		new_message = Message.create(name=name, message=message, email=email, title=title)
		return render_template('index.html')
	
	

@app.route('/strategy')
def strategy():
	return render_template("politics.html")

app.secret_key= b'\xf0\x80\xd5\x8aZ\xf4\xa7f\x8b\x0f]\xbf,\xa8"\xa5\xc8&\x03\'\x98\x8d\x15\x16'

