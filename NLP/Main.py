# coding: utf-8
import os
import pandas as pd
from SimpleNLP import SimpleCorpusProcessor

if __name__ == "__main__":
    pwd = os.path.dirname(os.path.realpath(__file__))
    corpus_path = os.path.join(pwd, "corpus/")
    corpus = {}
    for root, dirs, files in os.walk(corpus_path):
        for file in files:
            if '.txt' in file:
                path = os.path.join(root, file)
                with open(path, 'r', encoding="utf8") as fp:
                    doc = fp.read().replace('\n',' ')
                key = file.replace('.txt', '')
                corpus[key] = doc

    corpus = SimpleCorpusProcessor(corpus, remove_marks=True)
    tf = corpus.TermFrequencies()
    tf.to_csv(pwd + '/TermFrequencies.csv', encoding='utf-8')

    df = corpus.DocumentFrequencies()
    df.to_csv(pwd + '/DocumentFreguencies.csv', encoding='utf-8')

    tfidf = corpus.TFIDF()
    df.to_csv(pwd + '/TFIDF.csv', encoding='utf-8')
