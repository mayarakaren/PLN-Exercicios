import nltk

texto = "Some say the world will end in fire, Some say in ice. From what I’ve tasted of desire I hold with those who favor fire."
wordnetLemmatizer = nltk.stem.WordNetLemmatizer()

stopword = nltk.corpus.stopwords.words('english')
palavras = nltk.word_tokenize(texto.lower())
resultado = []
lemas = []

for palavra in palavras: 
    if not (palavra in stopword):
        resultado.append(palavra)

for palavra in resultado:
    lemas.append((wordnetLemmatizer.lemmatize(palavra)))

print("Palavras Filtradas:", resultado)
print("Lemas:", lemas)
