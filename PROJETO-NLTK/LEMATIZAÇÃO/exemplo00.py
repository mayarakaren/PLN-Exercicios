import nltk

wordnetLemmatizer = nltk.stem.WordNetLemmatizer()

word1 = wordnetLemmatizer.lemmatize("alunos")
word2 = wordnetLemmatizer.lemmatize("corpora")
word3 = wordnetLemmatizer.lemmatize("girls")
word4 = wordnetLemmatizer.lemmatize("better", pos="a")
print(word1, word2, word3, word4)