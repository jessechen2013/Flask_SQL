from flask import Flask, render_template, session, request
import random, time
app = Flask(__name__)
app.secret_key = 'youngOG'
@app.route('/')
def index():
	session['money'] = 0
	session['activity'] = []
	return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def money():
	randNum = 0
	building = ""
	if 'building' in request.form:
		print "building"
		if "farm" in request.form['building']:
			print "farm"
			randNum = random.randrange(10, 21)
			building = "farm"
			session['money'] += randNum
		elif "cave" in request.form['building']:
			building = "cave"
			randNum = random.randrange(5, 11)
			session['money'] += randNum
		elif "house" in request.form['building']:
			building = "house"
			randNum = random.randrange(2, 6)
			session['money'] += randNum
		else:
			building = "casino"
			randNum = random.randrange(-50, 51)
			session['money'] += randNum
		if(randNum>=0):
			session['activity'].append("Earned " + str(randNum) + " gold(s) from "+ building+ "!")
	return render_template("index.html")
app.run(debug=True)