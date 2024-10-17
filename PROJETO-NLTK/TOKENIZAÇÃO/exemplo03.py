import nltk

tweet = "Quando a educação não é libertadora, o sonho do oprimido é se tornar o opressor. ;) #FelizDiaDosProfessores #EducaçãoLibertadora @PauloFreireOficial XD"

twitterTokenizer = nltk.TweetTokenizer()
tweets = twitterTokenizer.tokenize(tweet)
print(tweets)
