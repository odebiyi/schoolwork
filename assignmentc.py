import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
 
with open(r'C:\Users\Ayodeji.odebiyi.GLOBALACCELEREX\Desktop\LECTURES\TEXT ANALYTICS\LECT 2\xLect2.Progs\assignmentb.txt')as f:
    contents = f.readlines()
    print(contents)

tokens =nltk.word_tokenize(contents)
print(tokens)
lemmatizer = WordNetLemmatizer()

#sentence= 'I’m just a young lady who is currently studying for her master’s degrees at Ireland largest campus UCD. The past one month has been a game-changer for me as it has opened doors of opportunities that I never thought existed. It might not be easy but I’m hopeful for the best learning experience at UCD.  '
 
# Define function to lemmatize each word with its POS tag
 
# POS_TAGGER_FUNCTION : TYPE 1
def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:         
        return None
pos_tagged = nltk.pos_tag(nltk.word_tokenize(contents)) 
 
print(pos_tagged)

wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
print(wordnet_tagged)

lemmatized_sentence = []
for word, tag in wordnet_tagged:
    if tag is None:
        # if there is no available tag, append the token as is
        lemmatized_sentence.append(word)
    else:       
        # else use the tag to lemmatize the token
        lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
lemmatized_sentence = " ".join(lemmatized_sentence)
 
print(lemmatized_sentence)