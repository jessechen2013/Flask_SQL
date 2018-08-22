from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "youngOG"
# our index route will handle rendering our form
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def page():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	if len(language) < 1 or len(location) < 1 or len(name) < 1:
		flash("Language, Location and Name filed have to be filled!")
	if len(comment) > 120:
		flash("comment has a word-limit of 120, please be concise!")
	return render_template('result.html', name = name, location = location, language = language, comment = comment)

@app.route('/reload', methods=['POST'])
def reload():
	return render_template('index.html')
app.run(debug=True) # run our server