# Let's combine two tasks: finding the most similar pair of lines and the tf-idf representation.
#
# Write a program that uses the tf-idf vectors to find the most similar pair of lines in a given data set.
# You can test your solution with the example text below. Note, however,
# that your solution will be tested on other data sets too,
# so make sure you don't make use of any special properties of the example data (like there being four lines of text).
#
# This exercise requires a bit more work than average
# but you should be able to benefit from what you have done in the previous exercises.
import math
import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def main(text):
    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # get a list of unique words that appear
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # (Term Frequency) tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequency of the word 'he' in the first
        # document
        tf[word] = [doc.count(word) / len(doc) for doc in docs]

        # (Inverse Document Frequency) df: number of documents containing word
        df[word] = sum([word in doc for doc in docs]) / N

    # loop through documents to calculate the tf-idf values
    tfidf = np.zeros((len(docs), len(vocabulary)))
    for doc_index, doc in enumerate(docs):
        for word_index, word in enumerate(vocabulary):
            # ADD THE CORRECT FORMULA HERE. Remember to use the base 10 logarithm: math.log(x, 10)

            value = tf[word][doc_index] * math.log((1 / df[word]), 10)
            tfidf[doc_index][word_index] = value

    print(find_nearest_pair(tfidf))
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal
    # despite casing) can be done with
    # docs = [line.lower().split() for line in text.split('\n')]

    # 2. go over each unique word and calculate its term frequency, and its document frequency

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and
    # calculate its TF-IDF representation, which will be a vector

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.


def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)
    new_data = all_pairs(data)
    for i in range(len(new_data)):
        for j in range(len(new_data[i])):
            if i == j:
                new_data[i][j] = np.Inf

    return np.unravel_index(np.argmin(new_data), dist.shape)


def distance(row1, row2):
    result = 0
    for i in range(len(row1)):
        result = result + abs(row1[i]-row2[i])
    return result


def all_pairs(data):
    return [[distance(sent1, sent2) for sent1 in data] for sent2 in data]


main(text)
