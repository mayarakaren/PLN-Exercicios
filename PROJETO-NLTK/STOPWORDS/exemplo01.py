import nltk

texto = "O rato roeu a roupa do rei de Roma. O rei de Roma matou o rato."
stopword = nltk.corpus.stopwords.words('portuguese')
palavras = nltk.word_tokenize(texto.lower())
resultado = []

for palavra in palavras: 
    if not (palavra in stopword):
        resultado.append(palavra)

print(resultado)