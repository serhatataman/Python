# Let's combine two tasks: finding the most similar pair of lines and the tf-idf representation.
#
# Write a program that uses the tf-idf vectors to find the most similar pair of lines in a given data set.
# You can test your solution with the example text below. Note, however,
# that your solution will be tested on other data sets too,
# so make sure you don't make use of any special properties of the example data (like there being four lines of text).
#
# This exercise requires a bit more work than average
# but you should be able to benefit from what you have done in the previous exercises.

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def main(text):
    print(text)
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


main(text)
