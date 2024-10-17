import nltk 

texto = "O rato roeu a roupa do rei de Roma"
palavras = nltk.word_tokenize(texto.lower())

stopwords = nltk.corpus.stopwords.words('portuguese')

resultados = []

for palavra in palavras:
    if not (palavra in stopwords):
        resultados.append(palavra)

print(resultados)

categorias = nltk.pos_tag(palavras)
poss_tagging = nltk.ne_chunk(categorias)
print(poss_tagging)