from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """returns the word welcome"""
    return "welcome"


@app.route('/welcome/home')
def welcome_home():
    """return the words 'welcome home'"""
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    """return the words 'welcome back'"""
    return "welcome back"