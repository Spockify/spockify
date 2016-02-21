from flask import Flask, render_template, request, session, redirect, url_for
import trygmail

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/getmsgs")
def getmsgs():
    return trygmail.getGmailMessages("pat.lempert@gmail.com")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "adashljdoiqdm"
    app.run('0.0.0.0',port=8000)
