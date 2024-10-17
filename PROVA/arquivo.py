# BLOCO 1 - Importação das bibliotecas e leitura do arquivo
import nltk
import pandas as pd

# Importar o arquivo CSV
path = r'C:\\Users\\mayar\\Downloads\\6Semestre\\PLN\\exercicios\\PROVA\\base-wepink.csv'
data = pd.read_csv(path, delimiter=',')

# BLOCO 2 - Tokenização e conversão para minúsculas (lowercasing)
# Crio uma lista para armazenar os comentários tokenizados
tokenized_comments = []
# Itero sobre cada comentário e converto para minúsculas
for comments in data['Comments']:
    tokenized_comments.append(nltk.word_tokenize(comments.lower()))

# BLOCO 3 - Remoção de stopwords
# Definir as stopwords em português
stopwords = nltk.corpus.stopwords.words('portuguese')
# Crio uma lista para armazenar os comentários sem stopwords
tokenized_comments_without_stopwords = []
for comments in tokenized_comments:
    comments_without_stopwords = [comment for comment in comments if comment not in stopwords]
    tokenized_comments_without_stopwords.append(comments_without_stopwords)

# BLOCO 4 - POS tagging
# Crio uma lista para armazenar os comentários com POS tagging
pos_tagged_comments = []
for comments in tokenized_comments_without_stopwords:
    pos_tagged_comments.append(nltk.pos_tag(comments))

# BLOCO 5 - Lematização
# Crio uma variável para o lematizador
word_net_lemmatizer = nltk.stem.WordNetLemmatizer()
# Crio uma lista para armazenar os comentários lematizados
lemmatized_comments = []
for comments in pos_tagged_comments:
    lemmatized_comment = [word_net_lemmatizer.lemmatize(word) for word, tag in comments]
    lemmatized_comments.append(lemmatized_comment)

# BLOCO 6 - Radicalização (Stemming)
# Crio uma variável para o stemmer
snowball_stemmer = nltk.SnowballStemmer('portuguese')
# Crio uma lista para armazenar os radicais
radicals = []
for comments in lemmatized_comments:
    radicals_by_comment = [snowball_stemmer.stem(word) for word in comments]
    radicals.append(radicals_by_comment)

# Exibir o resultado final
print(radicals)