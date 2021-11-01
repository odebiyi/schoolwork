import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.translate.ribes_score import position_of_ngram
from nltk.stem import WordNetLemmatizer

with open (r'C:\Users\Ayodeji.odebiyi.GLOBALACCELEREX\Desktop\LECTURES\TEXT ANALYTICS\LECT 2\xLect2.Progs\assignmentb.txt') as c:
    text_two = c.readlines()
    print(text_two)

tokens =nltk.word_tokenize(text_two)
print(tokens)







sent = tokens
sent_tokenized = sent.split(" ")
lemmatizer = WordNetLemmatizer()
words = [lemmatizer.lemmatize(word) for word in sent_tokenized]
print(words)





