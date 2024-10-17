import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

texto = "Some say the world will end in fire, Some say in ice. From what I’ve tasted of desire I hold with those who favor fire."
wordnetLemmatizer = nltk.stem.WordNetLemmatizer()

stopword = nltk.corpus.stopwords.words('english')
palavras = nltk.word_tokenize(texto.lower())
resultado = []
lemas = []

# Filtrar stopwords
for palavra in palavras: 
    if not (palavra in stopword):
        resultado.append(palavra)

# Etiquetagem de partes do discurso (POS tagging)
pos_tagged = nltk.pos_tag(resultado)

# Função para mapear a tag do NLTK para o formato do WordNet
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif tag.startswith('R'):
        return nltk.corpus.wordnet.ADV
    else:
        return None

# Lematização considerando a tag POS
for palavra, tag in pos_tagged:
    pos = get_wordnet_pos(tag) or nltk.corpus.wordnet.NOUN 
    lemas.append(wordnetLemmatizer.lemmatize(palavra, pos))

print("Palavras Filtradas:", resultado)
print("Lemas:", lemas)
