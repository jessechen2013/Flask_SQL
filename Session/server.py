from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
	session['count'] = 1
 	return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
	if 'Add 2' in request.form:
		session['count'] += 2
	elif 'Reset' in request.form:
		session['count'] = 1
	return render_template('index.html')
app.run(debug=True)
