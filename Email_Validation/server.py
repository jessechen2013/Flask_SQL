from flask import Flask, render_template, session, request, redirect, url_for,flash
import re, md5
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,10}')
app = Flask(__name__)
app.secret_key = 'youngOG'
mysql = MySQLConnector(app,'mydb')

@app.route('/')
def index():
    return render_template("log.html")


@app.route('/check', methods=['POST'])
def validate():
    email = request.form['email']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    password = request.form['password']
    password_confirm = request.form['password_confirm']

    if len(email) < 1 or len(firstname) < 1 or len(lastname) < 1 or len(password) < 1 or len(password_confirm) < 1:
        flash("All fields are required and must not be blank")
        return redirect('/')
        # just pass a string to the flash function
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address")
        return redirect('/')
    elif any(char.isdigit() for char in firstname + lastname):
        flash("Names must not contain any numbers")
        return redirect('/')
    elif not PASS_REGEX.match(password):
        flash("Password must be longer than 8 and shorter than 10 characters; with at least one number and uppercase letter")
        return redirect('/')
    elif password != password_confirm:
        flash("Please make sure password confirmation is same as the password")
        return redirect('/')
    elif len(firstname) < 3 or len(lastname) < 3:
        flash("Names must contain more than 2 characters")
        return redirect('/')
    hashed_password = md5.new(password).hexdigest()
    insert_query = "INSERT INTO Users (email, firstname, lastname, password) VALUES (:email, :firstname, :lastname, :password)"
    query_data = { 'email': email, 'firstname': firstname, 'lastname': lastname, 'password': password }
    mysql.query_db(insert_query, query_data)
    return render_template('success.html', email=email, firstname = firstname, lastname = lastname)

@app.route('/log', methods=['POST'])
def log():
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    query = "SELECT * FROM Users"
    # Run query with inserted data.
    users = mysql.query_db(query)
    for user in users:
        if user['email'] == email and user['password'] == password:
            return render_template('success.html', email=email, firstname = user['firstname'], lastname = user['lastname'])
    flash ("Invlad email or password")
    return redirect('/log')

@app.route('/reg')
def reg():
    return render_template('reg.html')
app.run(debug=True)