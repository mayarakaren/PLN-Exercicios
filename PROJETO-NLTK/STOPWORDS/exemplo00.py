import nltk

texto = "O rato roeu a roupa do rei de Roma. O rei de Roma matou o rato."
stopwords = ["O", "o", "A", "a", "E", "e", "de", "do", "para", "na"]

palavras = nltk.word_tokenize(texto)
resultado = []

for palavra in palavras: 
    if not (palavra in stopwords):
        resultado.append(palavra)

print(resultado)