import nltk
from nltk import pos_tag
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer 

with open(r'C:\Users\Ayodeji.odebiyi.GLOBALACCELEREX\Desktop\LECTURES\TEXT ANALYTICS\LECT 2\xLect2.Progs\assignment.txt', encoding='cp437')as f:
    contents = f.read()
    print(contents)

tokens =nltk.word_tokenize(contents)
print(tokens)

words =[w.lower() for w in tokens]
print(words)

print(nltk.pos_tag(tokens))

stemmer=PorterStemmer()
print(stemmer.stem("I’m just a young lady who is currently studying for her master’s degrees at Ireland largest campus UCD. The past one month has been a game-changer for me as it has opened doors of opportunities that I never thought existed. It might not be easy but I’m hopeful for the best learning experience at UCD."))
