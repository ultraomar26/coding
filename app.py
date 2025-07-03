# filepath: c:\Users\omar\Desktop\coding\app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # ممكن تضيف شرط تحقق هنا
        return f"Logged in as: {email}"
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # هنا تحفظه أو تطبعه
        return f"Signed up as: {username}"
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)
