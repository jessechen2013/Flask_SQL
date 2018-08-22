from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'youngOG'
mysql = MySQLConnector(app,'mydb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
@app.route('/')
def index():                       # run query with query_db()
    return render_template('index.html')

@app.route('/validation', methods=['POST'])
def validate():
    email = request.form['email']
    if not(EMAIL_REGEX.match(email)):
        flash("Invalid Email")
        print "not right"
        return redirect('/')
    else:
        print "right"
        flash('Valid Email!')
        # Write query as a string. Notice how we have multiple values
        # we want to insert into our query.
        query = "INSERT INTO Emails (email, created_at) VALUES (:email, NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
            'email': email
        }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        query = "SELECT * FROM Emails"                           # define your query
        emails = mysql.query_db(query) 
        return render_template('success.html', all_emails=emails)
app.run(debug=True)
