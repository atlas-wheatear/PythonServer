from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

count = 1

@app.route("/")
def hello():
    global count
    template = render_template("index.html", viewer_number=count)
    count += 1
    return template

def run_app():
    app.run(host="0.0.0.0")

def create_app():
    Thread(target="run_app").run()
    return app

if __name__ == "main":
    create_app()