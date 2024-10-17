import nltk
print(nltk.corpus.gutenberg.fileids())

import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Hello, world!")
print([(token.text, token.pos_) for token in doc])