import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


# INTRODUCTION TO NLP


text = "On Wednesday, the Association for Computing Machinery, the world's largest society of " \
       "computing professionals, announced that Hinton, LeCun and Bengio had won this year's Turing Award " \
       "for their work on neural networks. The Turing Award, which was introduced in 1966, is often called " \
       "the Nobel Prize of computing, and it includes a $1 million prize, which the three scientists will share."

# import sentence tokenizer
print("\nImporting sentence tokenizer: " + str(nltk.download('punkt')))


# Sentence Tokenizer - Breaks the paragraph into sentences and returns a list of sentences
sent_tk = sent_tokenize(text)
print("\nSentence Tokenizing the text: ", sent_tk)

# Word Tokenizer - Breaks the sentence into words and returns a list of words
word_tk = word_tokenize(text)
print("\nWord Tokenizing the text: ", word_tk)


# CLEANING TEXTUAL DATA
# Removing stop words

# import stopwords
print("\nImporting stopwords: " + str(nltk.download('stopwords')))

sw = set(stopwords.words('english'))
print("\nStop words in English language: ", sw)

# Removing stop words from the text
filtered_words = [word for word in word_tk if word not in sw]

print("\nThe text after removing stop words: ", filtered_words)


# Implement STEMMING
port_stem = PorterStemmer()

stemmed_words = []

# For each item in our filtered words list, we apply the Porter Stemmer algorithm
# and append the result to our stemmed_words list
for w in filtered_words:
    stemmed_words.append(port_stem.stem(w))

print("\nFiltered Words: ", filtered_words)
print("\nStemmed Rods: ", stemmed_words)




