import nltk
import spacy

# Carregar o modelo do spaCy para português
nlp = spacy.load("pt_core_news_sm")

# Frase de exemplo
texto = "O rato roeu a roupa do rei de Roma. O rei de Roma matou o rato."

# Carregar as stopwords em português
stopword = nltk.corpus.stopwords.words('portuguese')

# Tokenizar o texto usando NLTK
palavras = nltk.word_tokenize(texto.lower())

# Inicializar listas de resultados e lemas
resultado = []
lemas = []

# Filtrar palavras que não estão nas stopwords
for palavra in palavras: 
    if not (palavra in stopword):
        resultado.append(palavra)

# Agora usar o spaCy para lematizar as palavras filtradas
doc = nlp(" ".join(resultado))  # Converta o resultado de volta para texto para usar no spaCy

for token in doc:
    lemas.append(token.lemma_)  # Armazena o lema de cada token

# Exibir os resultados
print("Palavras filtradas:", resultado)
print("Lematização:", lemas)
