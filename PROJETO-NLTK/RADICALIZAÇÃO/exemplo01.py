import nltk

texto = "O rato roeu a roupa do rei de Roma. O rei de Roma matou o rato."

languages = nltk.SnowballStemmer.languages
snowballStemmer = nltk.SnowballStemmer('portuguese')

stopword = nltk.corpus.stopwords.words('portuguese')
palavras = nltk.word_tokenize(texto.lower())
resultado = []
radicais = []

for palavra in palavras: 
    if not (palavra in stopword):
        resultado.append(palavra)

for res in resultado:
    radicais.append(snowballStemmer.stem(res))


print(resultado)
print(radicais)
