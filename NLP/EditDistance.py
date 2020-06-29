import numpy as np
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Distance():

    words: list

    @staticmethod
    def iterative_levenshtein(s: str, t: str, costs: tuple = (1, 1, 1), case_sensetive: bool = False, *args, **kwargs) -> int:
        """ 
            iterative_levenshtein(s, t) -> ldist
            ldist is the Levenshtein distance between the strings 
            s and t.
            For all i and j, dist[i,j] will contain the Levenshtein 
            distance between the first i characters of s and the 
            first j characters of t

            costs: a tuple with three integers (d, i, s)
                where d defines the costs for a deletion
                        i defines the costs for an insertion and
                        s defines the costs for a substitution
            case_sensetive: a boolean thats differ between 
                lower case and upper case
        """
        s = s.lower()
        t = t.lower()

        rows = len(s)+1
        cols = len(t)+1
        deletes, inserts, substitutes = costs
        dist = np.zeros((rows, cols), dtype=np.int)

        # source prefixes can be transformed into empty strings
        # by deletions:
        for row in range(1, rows):
            dist[row][0] = row * deletes

        # target prefixes can be created from an empty source string
        # by inserting the characters
        for col in range(1, cols):
            dist[0][col] = col * inserts

        for col in range(1, cols):
            for row in range(1, rows):
                if s[row-1] == t[col-1]:
                    cost = 0
                else:
                    cost = substitutes
                dist[row][col] = min(dist[row-1][col] + deletes,  # deletion
                                     dist[row][col-1] + inserts,  # insertion
                                     dist[row-1][col-1] + cost)   # substitution

        return dist[row][col]

    def corpus_distance(self, my_word: str, max_distance: int = 2, *args, **kwargs) -> dict:
        result = defaultdict(list)
        for word in self.words:
            edit_distance = self.iterative_levenshtein(
                my_word, word, *args, **kwargs)
            if edit_distance <= max_distance:
                result[edit_distance].append(word)
        return result


if __name__ == "__main__":
    # print(Distance.iterative_levenshtein('av', 'ab'))
    with open('EditDistanceWords.txt', 'r', encoding='utf-8') as fp:
        words = fp.readlines()
    corpus = [word.replace('\n', '') for word in words]
    myobj = Distance(corpus)
    input_word = input('کلمه مورد نظر برای محاسبه فاصله ویرایشی را وارد کنید: ')
    result = myobj.corpus_distance(str(input_word))
    for key in sorted(result.keys()):
        output = f'فاصله ویرایشی {key} : {result[key]}'
        print(output)



