from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import sqlite3

app = Flask(__name__)
CORS(app)

DB_FILE = "database.db"
# Initialize SQLite Database (if it doesn't already exist)
def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE accounts (employee_id INTEGER, name TEXT, email TEXT, password TEXT, admin BOOL)")
        conn.commit()
        conn.close()

init_db()

app.route("/log-in")
def log_in():
    # Check email & password against the database
    
    # if they match & the account is an admin, redirect to the admin page
    # if they match & the account is a teacher, redirect to the teacher page
    # if they don't match or the email isn't found, stay on log-in page and create a toast pop-up


if __name__ == '__main__':
    app.run(debug=True)