from flask import Flask, render_template, request

app = Flask(__name__)

word_of_the_day = ""

@app.route("/")
def hello():
    return render_template("index.html", word_of_the_day=word_of_the_day)

@app.route("/", methods=["POST"])
def update_word():
    global word_of_the_day
    word_of_the_day = request.form["word-of-the-day"]
    return render_template("index.html", word_of_the_day=word_of_the_day)

def run_app():
    app.run(host="0.0.0.0")

if __name__ == "__main__":
    run_app()
