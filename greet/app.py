from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    "Return 'welcome' upon page load"
    return "welcome"

@app.route("/welcome/home")
def welcome_home():
    "Return 'welcome home' upon page load"
    return "welcome home"

@app.route("/welcome/back")
def welcome_back():
    "Return 'welcome back' upon page load"
    return "welcome back"