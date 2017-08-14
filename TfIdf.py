# https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/gensim%20Quick%20Start.ipynb
from gensim import corpora, models
from collections import defaultdict
import logging
import math

logging.basicConfig(format='%(asctime)s: %(levelname)s : %(message)s', level=logging.INFO)


# corpus

def train_model(query_string):
    raw_corpus = []
    f = open("corpus_filter.txt", "r")
    lines = f.readlines()
    for line in lines:
        raw_corpus.append(line.strip('\n'))
    f.close()

    # Create a set of frequent words and add stopwords
    stoplist = set('for a an of the and to in test from this that'.split(' '))
    # Lowercase each document, split it by white space and filter resource stopwords
    texts = [[word for word in document.lower().split() if word not in stoplist]
             for document in raw_corpus]

    # Count word frequencies
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    # Only keep words that appear more than once
    processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
    dictionary = corpora.Dictionary(processed_corpus)
    bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
    # train the model
    tfidf = models.TfidfModel(bow_corpus)
    # transform the "system minors" string
    t = tfidf[dictionary.doc2bow(str(query_string).lower().split())]
    if (t == []):
        return 0
    else:
        count = 0
        sum = 0
        for item in t:
            # f.write("key: %d \r\n" %item[0])
            # f.write("freq: %.4f \r\n" %item[1])
            count += 1
            sum += item[1]
        res1 = sum / count
        res1 = math.sqrt(res1)
        return '%.2f' % res1
