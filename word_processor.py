# Made by Isaac Joffe

import sys
import os.path
import pickle


class WordSet():
    """
    A class to hold the set of all valid Wordle words.

    Attributes
    ----------

    Methods
    -------
    """

    def __init__(self, filename):
        """
        """

        self.wordset = []

        self.get_base_words(filename)
        self.count_letters()
        self.count_frequencies()
        self.sort_by_value()
        self.pickle(filename)
        return

    def get_base_words(self, filename):
        """
        """

        with open(filename) as infile:
            words = infile.read().split()
        for word in words:
            self.wordset.append({'word': word, 'letters': {}, 'value': 0})
        return

    def count_letters(self):
        """
        """

        for element in self.wordset:
            for letter in element['word']:
                if letter not in element['letters']:
                    element['letters'][letter] = 1
                else:
                    element['letters'][letter] += 1
        return

    def count_frequencies(self):
        """
        """

        frequencies = {}
        for element in self.wordset:
            for letter in element['letters']:
                if letter not in frequencies:
                    frequencies[letter] = 1
                else:
                    frequencies[letter] += 1

        """
        total = len(self.wordset) * 5
        for letter in self.frequencies.keys():
            self.frequencies[letter] /= total
        """

        for element in self.wordset:
            for letter in element['letters']:
                element['value'] += frequencies[letter]
        return

    def sort_by_value(self):
        """
        """

        def word_value_key(word):
            return word['value']

        self.wordset.sort(reverse=True, key=word_value_key)
        return

    def pickle(self, filename):
        """
        """

        outfilename = filename + ".pkl"
        with open(outfilename, 'wb') as outfile:
            pickle.dump(self.wordset, outfile)
        return


def main():
    """
    """

    if len(sys.argv) != 2:
        print("Error: no input file specified.",
            "Proper Usage: <python3 word_processor.py <filename>>")
        return

    infilename = sys.argv[1]
    if not os.path.exists(infilename):
        print("Error: input file specified does not exist.",
            "Proper Usage: <python3 word_processor.py <filename>>")
        return

    WordSet(infilename)
    return


if __name__ == "__main__":
    main()
