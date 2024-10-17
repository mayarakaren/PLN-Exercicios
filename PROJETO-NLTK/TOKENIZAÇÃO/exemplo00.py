import nltk

texto = "O rato roeu a roupa do rei de Roma. O rei de Roma matou o rato."
sentencas = nltk.sent_tokenize(texto)
print(sentencas)