# Made by Isaac Joffe

import sys    # for command line arguments
import os.path    # to check that file exists
import pickle    # to serialize data


class WordSet():
    """
    A class to hold the set of all valid Wordle words.

    Attributes:
        wordset: list of dictionaries
            contains all valid Wordle words along with data on what letters
            the word conatins and how useful the word is

    Methods:
        get_base_words(filename):
            reads a text file containing all valid words separated by spaces
        count_letters():
            counts the number of letters that occur in each word
        count_frequencies():
            calculates the value of a word based on how common its letters are
        sort_by_value():
            sorts the list of words based on their value
        pickle(filename):
            serializes the list of words and their data
    """

    def __init__(self, filename):
        """
        Fully creates and serializes all data based on an input file.

        Arguments:
            filename: string
                name of the text file to read words from

        Returns:
            None, but creates a serialized version of the word data
        """

        self.wordset = []

        # execute steps to build the serilaized data
        self.get_base_words(filename)
        self.count_letters()
        self.count_frequencies()
        self.sort_by_value()
        self.pickle(filename)
        return

    def get_base_words(self, filename):
        """
        Reads in all possible words into memory.

        Arguments:
            filename: string
                name of the text file to read words from

        Returns:
            None, but creates a basic skeleton of the data structure
        """

        with open(filename) as infile:
            words = infile.read().split()    # words are separated by spaces
        for word in words:
            # create base attributes of each word
            self.wordset.append({'word': word, 'letters': {}, 'value': 0})
        return

    def count_letters(self):
        """
        Counts which letters occur in each word and how often the occur.

        Arguments:
            None, but operates on existing class attributes

        Returns:
            None, but updates existing class attributes
        """

        for element in self.wordset:
            # count each letter in each word and store in the words dictionary
            for letter in element['word']:
                if letter not in element['letters']:
                    element['letters'][letter] = 1
                else:
                    element['letters'][letter] += 1
        return

    def count_frequencies(self):
        """
        Counts how often each letter occurs in the entire dataset.

        Arguments:
            None, but operates on existing class attributes

        Returns:
            None, but updates existing class attributes
        """

        frequencies = {}    # dictionary of each letters count
        for element in self.wordset:
            # count every letter in every word to keep track fo frequency
            for letter in element['letters']:
                if letter not in frequencies:
                    frequencies[letter] = 1
                else:
                    frequencies[letter] += 1

        """
        # optional normalization of data
        total = len(self.wordset) * 5
        for letter in self.frequencies.keys():
            self.frequencies[letter] /= total
        """

        for element in self.wordset:
            # compute value of each word based on how useful each distinct
            # letter inside it, double letters are not counted again
            for letter in element['letters']:
                element['value'] += frequencies[letter]
        return

    def sort_by_value(self):
        """
        Sorts the entire dataset based on how valuable each word is.

        Arguments:
            None, but operates on existing class attributes

        Returns:
            None, but updates existing class attributes
        """

        # define sorting function so words can be sorted by their value
        def word_value_key(word):
            # returns the value of a particular word in the set
            return word['value']

        # sort dataset in descending order for easy access to first element
        self.wordset.sort(reverse=True, key=word_value_key)
        return

    def pickle(self, filename):
        """
        Serializes all word data into a file for other programs to use.

        Arguments:
            filename: string
                name of the text file to write to with extension

        Returns:
            None, but creates a serialized version of the data in a file
        """

        outfilename = filename + ".pkl"    # add suffix to original name
        with open(outfilename, 'wb') as outfile:
            pickle.dump(self.wordset, outfile)
        return


def main():
    """
    Processes and stores information about a set of possible input words.

    Arguments:
        None, but reads the set of valid words from a specified file

    Returns:
        None, but creates another file containing the information of the words
    """

    # check that file is specified
    if len(sys.argv) != 2:
        print("Error: no input file specified.",
            "Proper Usage: <python3 word_processor.py <filename>>")
        return

    # check that the specified file exists
    infilename = sys.argv[1]
    if not os.path.exists(infilename):
        print("Error: input file specified does not exist.",
            "Proper Usage: <python3 word_processor.py <filename>>")
        return

    WordSet(infilename)    # call object to create and serialize data
    return


if __name__ == "__main__":
    main()
