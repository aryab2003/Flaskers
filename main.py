from flask import Flask, render_template, request
from model import spell_check

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", result="")


@app.route("/check", methods=["POST"])
def check_spelling():
    text = request.form["text"]
    misspelled_words = spell_check(text)
    result = (
        f"Misspelled words: {', '.join(misspelled_words)}"
        if misspelled_words
        else "No misspelled words found"
    )
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
