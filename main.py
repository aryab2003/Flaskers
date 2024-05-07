from flask import Flask, render_template, request
from model import spell_check, grammar_check, correct_sentence

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html", misspelled_result="", grammar_result=[], corrected_sentence=""
    )


@app.route("/check", methods=["POST"])
def check_text():
    text = request.form["text"]
    misspelled_words = spell_check(text)
    grammar_errors = grammar_check(text)
    corrected_text = correct_sentence(text)

    misspelled_result = (
        f"Misspelled words: {', '.join(misspelled_words)}"
        if misspelled_words
        else "No misspelled words found"
    )

    return render_template(
        "index.html",
        misspelled_result=misspelled_result,
        grammar_result=grammar_errors,
        corrected_sentence=corrected_text,
    )


if __name__ == "__main__":
    app.run(debug=True)
