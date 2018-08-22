from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    print request.form['first_name']
    print "Hi"
    print request.form['last_name']
    print request.form['occupation']
    # add a friend to the database!
    return redirect('/')
app.run(debug=True)
