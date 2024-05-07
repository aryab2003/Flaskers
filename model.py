import enchant
from language_tool_python import LanguageTool


def spell_check(text):
    d = enchant.Dict("en_US")
    words = text.split()
    misspelled_words = [word for word in words if not d.check(word)]
    return misspelled_words


def grammar_check(text):
    tool = LanguageTool("en-US")
    matches = tool.check(text)
    return matches


def correct_sentence(text):
    tool = LanguageTool("en-US")
    corrected_text = tool.correct(text)
    return corrected_text
