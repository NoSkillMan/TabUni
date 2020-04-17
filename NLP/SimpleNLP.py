# coding= utf-8
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from SimpleTokenizer import SimpleTokenizer


class SimpleCorpusProcessor:
    corpus = 'Corpus'
    wt = 'Word Types'
    tf = 'Term Frequencies'
    df = 'Document Frequencies'
    tf_idf = 'Type Frequencies / Document Frequencies'

    def __init__(self, corpus,*args,**kwargs):
        self.corpus = corpus
        self._CorpusProcess(*args,**kwargs)

    def _CorpusProcess(self,*args,**kwargs):
        self.wt = set()
        self.tf = dict()
        self.df = dict()
        self.tf_idf = dict()
        for doc in self.corpus.keys():
            tmp_doc = {}
            self.tf[doc] = tmp_doc
            self.tf_idf[doc] = {}
            text = self.corpus.get(doc)
            obj = SimpleTokenizer(text)
            tokenized_text = obj.tokenize(*args,**kwargs)
            for word in tokenized_text:
                if tmp_doc.get(word):
                    tmp_doc[word] += 1
                else:
                    self.wt.add(word)
                    tmp_doc[word] = 1
                    if self.df.get(word):
                        self.df[word] += 1
                    else:
                        self.df[word] = 1
        for word in self.wt:
            for doc in self.tf.keys():
                if self.tf[doc].get(word):
                    tmp_tfidf = self.tf[doc][word] / self.df[word]
                    self.tf_idf[doc][word] = tmp_tfidf
                else:
                    self.tf_idf[doc][word] = 0.0

    def TermFrequencies(self):
        # dataframe = pd.DataFrame(data=self.tf, columns=self.tf.keys(),index=self.wt.keys())
        dataframe = pd.DataFrame(data=self.tf)
        dataframe.fillna(value=0.0, inplace=True)
        return dataframe

    def DocumentFrequencies(self):
        dataframe = pd.DataFrame().from_dict(self.df, orient="index")
        dataframe.fillna(value=0, inplace=True)
        return dataframe
        # return self.df

    def TFIDF(self):
        dataframe = pd.DataFrame(data=self.tf_idf)
        return dataframe

if __name__ == "__main__":
    corpus = {"a": '«عباس عراقچی» با تاکید بر اینکه فشار حداکثری آمریکا به اوج رسیده و «شرایط بسیار سختی» وجود دارد، خروج این شرکت‌ها را «همراهی» با آمریکا توصیف کرده است. عراقچی گفته است شرکت‌هایی که در این شرایط از ایران می‌روند، «بازاری را از دست داده‌اند که به آسانی نخواهند توانست دوباره به دست بیاورند».',
              'b': 'با پیروی از این حرکت چین، دولت‌های دیگر هم به تکنولوژی‌های مشابه برای مقابله با ویروس روی آورده‌اند. سنگاپور در ماه گذشته یک اپلیکیشن هوشمند برای پایش ارتباطات عرضه کرد که به مقامات اجازه می‌دهد قادر به شناسایی افرادی باشند که با مبتلایان به کووید-۱۹ در ارتباط بوده‌اند. دولت ژاپن هم یک اپلیکیشن مشابه در نظر دارد. مسکو نیز یک سیستم کدگذاری مبتنی بر کدهای QR معرفی کرده تا قادر به پایش حرکات و اعمال قرنطینه باشد.'
              }
    obj = SimpleCorpusProcessor(corpus)
    tmp = obj.TFIDF()
    print(tmp.head(20))
