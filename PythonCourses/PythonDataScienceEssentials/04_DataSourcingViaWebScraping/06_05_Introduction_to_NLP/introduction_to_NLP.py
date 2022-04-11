import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# INTRODUCTION TO NLP


text = "On Wednesday, the Association for Computing Machinery, the world's largest society of " \
       "computing professionals, announced that Hinton, LeCun and Bengio had won this year's Turing Award " \
       "for their work on neural networks. The Turing Award, which was introduced in 1966, is often called " \
       "the Nobel Prize of computing, and it includes a $1 million prize, which the three scientists will share."

# import sentence tokenizer (this doesn't work)
print("\nImporting sentence tokenizer: " + str(nltk.download('punkt')))


# Sentence Tokenizer - Breaks the paragraph into sentences and returns a list of sentences
sent_tk = sent_tokenize(text)
print("\nSentence Tokenizing the text: ", sent_tk)

# Word Tokenizer - Breaks the sentence into words and returns a list of words
word_tk = word_tokenize(text)
print("\nWord Tokenizing the text: ", word_tk)

