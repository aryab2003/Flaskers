import enchant


def spell_check(text):
    d = enchant.Dict("en_US")
    words = text.split()
    misspelled_words = [word for word in words if not d.check(word)]
    return misspelled_words
