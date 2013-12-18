from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

tokenizer = RegexpTokenizer(r'\w+')
link = open('BreneBrown_2010X-480p.eng.srt','r').read()

lmtzr = WordNetLemmatizer()
link = set(tokenizer.tokenize(link))
normalize = []
for word in link:
    normalize += lmtzr.lemmatize(word)
print link
#

