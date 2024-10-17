import nltk

textos = ["O rato roeu a roupa do rei de Roma.", "A situação faz o sapo pular.", "Se fosse na minha empresa...", "Já dizia o Datena é brincadeira.", "Faz o L!"]

respostas = []

for texto in textos:
    respostas.append(nltk.word_tokenize(texto))

print(respostas)