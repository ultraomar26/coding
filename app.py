# filepath: c:\Users\omar\Desktop\coding\app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/sginup')
def signup():
    return render_template('sginup.html')

if __name__ == '__main__':
    app.run(debug=True)