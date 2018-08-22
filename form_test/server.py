from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
   print "Welcome to 5000/ local host"
   return render_template('index.html')
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
   name = request.form['name']
   email = request.form['email']
   # Here's the line that changed. We're rendering a template from a post route now.
   return render_template('success.html')

@app.route('/ninjas')
def go_page():
  return render_template('ninjas.html')

@app.route('/dojos/new')
def get_new():
	return render_template('dojos.html')

@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')
app.run(debug=True) # run our server

