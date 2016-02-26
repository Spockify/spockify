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

@app.route("/showgraph")
def showgraph():
    return render_template("showgraph.html")

@app.route("/getmsgs")
def getmsgs():
    email = session["input_email"]
    return trygmail.getGmailMessages(email)

@app.route("/input",methods=["GET","POST"])
def input():
    if request.method=="GET":
        return render_template("input.html")
    else:
        session["input_email"] = request.form['input_email']
        return redirect(url_for("getmsgs"))


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "adashljdoiqdm"
    app.run('0.0.0.0',port=8000)
