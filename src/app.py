from flask import Flask, render_template

app = Flask(__name__)

count = 1

@app.route("/")
def hello():
    global count
    template = render_template("index.html", viewer_number=count)
    count += 1
    return template

if __name__ == "__main__":
    app.run(host='0.0.0.0')
