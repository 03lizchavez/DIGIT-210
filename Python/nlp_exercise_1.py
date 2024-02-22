import spacy
# Need line 8 the first time: Then comment it out after the first time you run it:
# nlp = spacy.cli.download("en_core_web_md")
nlp = spacy.load('en_core_web_md')

textfile = open('nlp_exercise_1', 'r', encoding='utf8')
words = textfile.read()
wordstrings = str(words)
print(wordstrings)
txtWords = nlp(wordstrings)
for token in txtWords:
    # if token.pos_ == "VERB":
    print(token.text, "!!!", token.pos_, "%$#", token.lemma_)