from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	session['target'] = random.randrange(0, 101)
	session['guess'] = -1
	return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
	session['guess'] = int(request.form['guess'])
	print "guess: ", session['guess']
	print "target: ", session['target']
	return render_template('index.html')

@app.route('/restart', methods=['POST'])
def restart():
	session['target'] = random.randrange(0, 101)
	session['guess'] = -1
	return render_template('index.html')
app.run(debug=True)






