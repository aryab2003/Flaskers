from flask import Flask, render_template, request
from model import spell_check
import enchant

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", result="")


@app.route("/check", methods=["POST"])
def check_spelling():
    text = request.form["text"]
    misspelled_words = spell_check(text)
    corrected_words = []
    for word in misspelled_words:
        suggestions = enchant.Dict("en_US").suggest(word)
        corrected_word = suggestions[0] if suggestions else "No suggestion found"
        corrected_words.append(corrected_word)
    result = (
        f"Misspelled words: {', '.join(misspelled_words)} and "
        f"Corrected words: {', '.join(corrected_words)}"
        if misspelled_words
        else "No misspelled words found"
    )
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
