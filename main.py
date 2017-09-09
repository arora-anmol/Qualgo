from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'qualgo123'
app.config['MYSQL_DATABASE_DB'] = 'qualgo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

conn = mysql.connect()
cursor = conn.cursor()


@app.route('/search')
def main():
    cursor.execute("SELECT * from companies")
    data = cursor.fetchone()

    return render_template('main.html', data=data)
