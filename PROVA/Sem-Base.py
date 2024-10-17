#1 Passo: Importações 
import nltk
import nltk.stem.wordnet
import pandas as pd

texto = ['Produtividade é a capacidade de realizar tarefas de forma eficiente, maximizando os resultados com o menor esforço e tempo possível. Para alcançar altos níveis de produtividade, é essencial a organização, definição clara de metas, e foco nas prioridades. Técnicas como a gestão do tempo, uso de ferramentas digitais e pausas estratégicas podem otimizar o desempenho, reduzindo distrações e elevando a qualidade do trabalho executado.']

#2 Passo: Tokenização
tokenizacao = []
for comentarios in texto:
    tokenizacao.append(nltk.word_tokenize(comentarios.lower()))

#3 Passo: Remoção das Stopwords
stopwords = nltk.corpus.stopwords.words('portuguese')
sem_stopwords = []
for comentarios in tokenizacao:
    comentario_sem_stopwords = [comentario for comentario in comentarios if comentario not in stopwords]
    sem_stopwords.append(comentario_sem_stopwords)

#Passo 4: Pos Taggin
tags = []
for comentarios in sem_stopwords:
    tags.append(nltk.pos_tag(comentarios))

#Passo 5: Lematização
lematizacao = nltk.stem.WordNetLemmatizer()
lemas = []
for comentarios in tags:
    comentarios_lematizados = [lematizacao.lemmatize(word) for word, tag in comentarios]
    lemas.append(comentarios_lematizados)

#Passo 6: Radicalização
stemmer = nltk.SnowballStemmer('portuguese')
radicais = []
for comentarios in lemas:
    comentarios_radicalizados = [stemmer.stem(word) for word in comentarios]
    radicais.append(comentarios_radicalizados)

print(radicais)
