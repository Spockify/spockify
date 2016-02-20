from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)

@app.route('')
def index():
    render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
