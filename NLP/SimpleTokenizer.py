# coding: utf-8
import stringprep
import string
import re


class SimpleTokenizer():
    istr = "input string"
    marks = [';', '.', '!', ':', '،', '«',
             '»', '(', ')', '#', '$', '^', '*', '-']

    def __init__(self, istr):
        self.istr = istr.strip()

    def _marks_replace(self, marks=marks, remove_marks=False, **kwargs):
        result = self.istr
        for mark in marks:
            if remove_marks:
                result = result.replace(mark, " ")
                # remove marks
            else:
                # put space behind and after marks in context for splitting
                result = result.replace(mark, " {} ".format(mark))
        # remove semi-whitespace from context
        result = result.replace(u'\u200c', '')
        # remove extra whitespaces(more than 1)
        result = re.sub(' +', ' ', result)
        # remove white spcae from begin and end of context
        result = result.strip()
        self.istr = result

    def tokenize(self, *args, **kwargs):
        self._marks_replace(**kwargs)
        result = self.istr.split(" ")
        return result


if __name__ == "__main__":
    istr = "«عباس عراقچی» با تاکید بر اینکه فشار حداکثری آمریکا به اوج رسیده و «شرایط بسیار سختی» وجود دارد، خروج این شرکت‌ها را «همراهی» با آمریکا توصیف کرده است. عراقچی گفته است شرکت‌هایی که در این شرایط از ایران می‌روند، «بازاری را از دست داده‌اند که به آسانی نخواهند توانست دوباره به دست بیاورند»."

    tkn = SimpleTokenizer(istr)

    print(tkn.tokenize(remove_marks=False))
