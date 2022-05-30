# Write a python program that will replace a word with a given length by the provided word
# Example if I have a sentence:
# This is a brown fox
# Add more tests for this as an example below

sentence = "Beginners when start programming often get bored if they do not get a chance to " \
           "play with some interesting code."


def replace_words(text, length_to_replace, word):
    text_lst = text.strip(".,-!@#$%^&*()/?><:;{}[]|").split()
    text = text.rjust(len(text) + 1, " ")
    for i in text_lst:
        if len(i) == length_to_replace:
            text = text.replace(i.center(len(i)+2, " "), word.center(len(word)+2, " "))
    text = text.strip().capitalize()
    return text


print(replace_words(sentence, 3, "test"))
print(replace_words(sentence, 1, "the"))
print(replace_words(sentence, 9, "people"))
print(replace_words(sentence, 2, "test"))

assert replace_words(sentence, 3,
                     "test") == "Beginners when start programming often test bored if they do test test a chance " \
                                "to play with some interesting code."

assert replace_words(sentence, 1,
                     "the") == "Beginners when start programming often get bored if they do not get the chance to " \
                               "play with some interesting code."

assert replace_words(sentence, 9,
                     "people") == "People when start programming often get bored if they do not get a chance to " \
                                  "play with some interesting code."

assert replace_words(sentence, 2,
                     "test") == "Beginners when start programming often get bored test they test not get a chance test " \
                                "play with some interesting code."
