from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/ninja')
def index():
  return render_template("index.html")

@app.route('/ninja/<ninja>')
def show_ninja(ninja):
	if ninja == "blue":
		ninja = "leonardo"
	elif ninja == "orange":
		ninja = "michelangelo"
	elif ninja == "red":
		ninja = "raphael"
	elif ninja == "purple":
		ninja = "donatello"
	else:
		ninja = "notapril"
	ninja += ".jpg"
	return render_template("ninja.html", ninja=ninja)
app.run(debug=True)