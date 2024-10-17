import nltk

texto = "O rato roeu a roupa do rei de Roma. O rei de Roma matou o rato."
palavras= nltk.word_tokenize(texto)
print(palavras)