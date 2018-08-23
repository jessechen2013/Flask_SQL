from flask import Flask, render_template, session, request, redirect, url_for, flash
import re
import md5
from mysqlconnection import MySQLConnector



app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app, 'mydb')


@app.route('/')
def index():
    return render_template('log.html')


@app.route('/log')
def log():
    return render_template('success.html')

@app.route('/register')
def register():
  return render_template('reg.html')

@app.route('/reg', methods=['POST'])
def reg():
    hashed_password = md5.new(request.form['password']).hexdigest()
    query = \
        'INSERT INTO Users (email, firstname, lastname, password) VALUES (:email, :firstname, :lastname, :password)'
    data = {
        'email': request.form['email'],
        'firstname': request.form['firstname'],
        'lastname': request.form['lastname'],
        'password': hashed_password,
        }
    mysql.query_db(query, data)
    return render_template('success.html')

@app.route('/check', methods=['POST'])
def check():
    hashed_password = md5.new(request.form['password']).hexdigest()
    email = request.form['email']
    user_query = "SELECT * FROM Users WHERE users.email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)
    if len(user) != 0:
      encrypted_password = md5.new(password).hexdigest()
      if user[0]['password'] == encrypted_password:
        return redirect('/success')
      else:# invalid password!
        flash("Invalid password")
        return redirect('/')
    else:# invalid email!
      flash("Invalid email")
      return redirect('/')

app.run(debug=True)
