import nltk

languages = nltk.SnowballStemmer.languages
snowballStemmer = nltk.SnowballStemmer('portuguese')

word1 = "Computador"
word2 = "Menino"
word3 = "Venda"

print(snowballStemmer.stem(word1))
print(snowballStemmer.stem(word2))
print(snowballStemmer.stem(word3))
