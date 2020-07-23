from flask import Flask, render_template
from multiprocessing import Process

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

# this should be in the test package, somehow!
def create_test_app():
    app_process = Process(target=run_app)
    app_process.start()
    return app_process

if __name__ == "main":
    run_app()