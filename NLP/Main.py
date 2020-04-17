# coding: utf-8
import os
from SimpleNLP import SimpleCorpusProcessor

if __name__ == "__main__":
    # corpus = {"a": '«عباس عراقچی» با تاکید بر اینکه فشار حداکثری آمریکا به اوج رسیده و «شرایط بسیار سختی» وجود دارد، خروج این شرکت‌ها را «همراهی» با آمریکا توصیف کرده است. عراقچی گفته است شرکت‌هایی که در این شرایط از ایران می‌روند، «بازاری را از دست داده‌اند که به آسانی نخواهند توانست دوباره به دست بیاورند».',
    #           'b': 'با پیروی از این حرکت چین، دولت‌های دیگر هم به تکنولوژی‌های مشابه برای مقابله با ویروس روی آورده‌اند. سنگاپور در ماه گذشته یک اپلیکیشن هوشمند برای پایش ارتباطات عرضه کرد که به مقامات اجازه می‌دهد قادر به شناسایی افرادی باشند که با مبتلایان به کووید-۱۹ در ارتباط بوده‌اند. دولت ژاپن هم یک اپلیکیشن مشابه در نظر دارد. مسکو نیز یک سیستم کدگذاری مبتنی بر کدهای QR معرفی کرده تا قادر به پایش حرکات و اعمال قرنطینه باشد.'
    #           }
    # obj = SimpleCorpusProcessor(corpus)
    # tmp = obj.TFIDF()
    # print(tmp.head(20))
    pwd = os.path.dirname(os.path.realpath(__file__))
    corpus_path = os.path.join(pwd, "corpus/")
    corpus = {}
    for root, dirs, files in os.walk(corpus_path):
        for file in files:
            if '.txt' in file:
                path = os.path.join(root, file)
                with open(path, 'r', encoding="utf8") as fp:
                    doc = fp.readlines()[0]
                key = file.replace('.txt', '')
                corpus[key] = doc

    corpus = SimpleCorpusProcessor(corpus, remove_marks=True)
    tf = corpus.TermFrequencies()
    tf.to_csv(pwd + '/TermFrequencies.csv', encoding='utf-8')

    df = corpus.DocumentFrequencies()
    df.to_csv(pwd + '/DocumentFreguencies.csv', encoding='utf-8')

    tfidf = corpus.TFIDF()
    df.to_csv(pwd + '/TFIDF.csv', encoding='utf-8')
