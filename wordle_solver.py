# Made by Isaac Joffe

import sys    # for command line arguments
import os.path    # to check that file exists


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
            determines the number of times each letter occurs in the dataset
        set_values(frequencies):
            calculates the value of a word based on how common its letters are
        sort_by_value():
            sorts the list of words based on their value
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
        self.frequencies = {}

        # execute steps to build the serilaized data
        self.get_base_words(filename)
        self.count_letters()
        frequencies = self.count_frequencies()
        self.set_values(frequencies)
        self.sort_by_value()
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
            self.wordset.append({"word": word, "letters": {}, "value": 0})
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
            for letter in element["word"]:
                if letter not in element["letters"]:
                    element["letters"][letter] = 1
                else:
                    element["letters"][letter] += 1
        return

    def count_frequencies(self):
        """
        Counts how often each letter occurs in the entire dataset.

        Arguments:
            None, but operates on existing class attributes

        Returns:
            frequencies: dictionary
                holds the number of times each letter occurs in the dataset
        """

        frequencies = {}    # dictionary of each letters count
        for letter in range(26):
            frequencies[chr(ord("a") + letter)] = 0
        for element in self.wordset:
            # count every letter in every word to keep track fo frequency
            for letter in element["letters"]:
                frequencies[letter] += 1

        """
        # optional normalization of data
        total = len(self.wordset) * 5
        for letter in self.frequencies.keys():
            self.frequencies[letter] /= total
        """
        return frequencies

    def set_values(self, frequencies):
        """
        Sets the value of each word in terms of how often its letters occur.

        Arguments:
            frequencies: dictionary
                holds the number of times each letter occurs in the dataset

        Returns:
            None, but updates existing class attributes
        """

        for element in self.wordset:
            element["value"] = 0
            # compute value of each word based on how useful each distinct
            # letter inside it, double letters are not counted again
            for letter in element["letters"]:
                element["value"] += frequencies[letter]
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
            return word["value"]

        # sort dataset in descending order for easy access to first element
        self.wordset.sort(reverse=True, key=word_value_key)
        return


def wordle_solve(infilename):
    """
    Guesses the secret word according to input corresponding to the output of
    the game Wordle.

    Arguments:
        infilename: string
            the name of the file containing the data on all possible words

    Returns:
        None, but continually prints words to try until the word is found
    """

    valid_words = WordSet(infilename)
    all_words = WordSet(infilename)
    letters = {}    # dictionary of each letters count
    for letter in range(26):
        letters[chr(ord("a") + letter)] = False
    results = [0]    # initialize number of guesses
    # keep guessing as long as the set of valid words is not empty
    while(True):
        if not len(valid_words.wordset):
            print("There was an error in the program.")
            break    # invalid input led to no words being left, exit program

        print("Number of possible words:", len(valid_words.wordset))
        if len(valid_words.wordset) > len(all_words.wordset) / 500 + 1:
            test_word = all_words.wordset[0]["word"]
        else:
            test_word = valid_words.wordset[0]["word"]

        print("Now try:", test_word)    # tell user what to guess next
        result = input("Enter result: ")    # obtain response to the guess
        results[0] += 1    # one more guess has been entered
        results.append(result)    # make not of result of guess
        words_to_remove = []

        if result == "ggggg":
            print_results(results)    # print shareable results
            break    # code cracked, exit program

        # iterate through each letter of the guessed word
        for number in range(len(result)):
            if result[number] == "g":
                letters[test_word[number]] = True
                # words are only valid with that letter in that exact spot
                for index in range(len(valid_words.wordset)):
                    if valid_words.wordset[index]["word"][number] \
                        != test_word[number]:
                        words_to_remove.append(index)

            elif result[number] == "y":
                letters[test_word[number]] = True
                # words are only valid with that letter, but not in that spot
                for index in range(len(valid_words.wordset)):
                    if test_word[number] not in valid_words.wordset[index] \
                        ["letters"]:
                        words_to_remove.append(index)
                    if test_word[number] == valid_words.wordset[index] \
                        ["word"][number]:
                        words_to_remove.append(index)

            elif result[number] == "b":
                # words are only valid if they do not contain that letter, but
                # exception is for letters that reoccured in the guess
                for index in range(len(valid_words.wordset)):
                    if test_word[number] in valid_words.wordset[index] \
                        ["letters"] and test_word.count(test_word[number]) \
                        == 1:
                        words_to_remove.append(index)

        # put in descending order to avoid popping glitches
        words_to_remove.sort(reverse=True)
        # remove any and all words that are not possibly correct
        words_to_remove.insert(0, -1)    # so comparison remains valid
        for index in range(1, len(words_to_remove)):
            if words_to_remove[index] != words_to_remove[index - 1]:
                valid_words.wordset.pop(words_to_remove[index])

        frequencies = valid_words.count_frequencies()
        for letter in frequencies:
            if letters[letter]:
                frequencies[letter] = 0
        all_words.set_values(frequencies)
        all_words.sort_by_value()
    return


def print_results(results):
    """
    Prints the Wordle-style shareable result of the game instance.

    Arguments:
        results: list of integers and strings
            data about the result of the game to print

    Returns:
        None, but prints data to standard out
    """

    print()    # intentional blank line
    print("Share Results:")
    print("Wordle {}/6".format(results[0]))    # print number of tries
    print()    # intentional blank line
    for index in range(results[0]):
        for letter in results[index + 1]:
            if letter == "g":
                print("\U0001F7E9", end="")    # unicode for green square
            elif letter == "y":
                print("\U0001F7E8", end="")    # unicode for yellow square
            elif letter == "b":
                print("\U00002B1B", end="")    # unicode for black square
        print()    # move to next line
    return


def main():
    """
    Solves an instance of the Wordle game based on input data.

    Arguments:
        None, but reads the data of valid words from a specified file

    Returns:
        None, but calls the wordle solving function which continually prints
        words to try until the word is found
    """

    # check that file is specified
    if len(sys.argv) != 2:
        print("Error: no input file specified.",
            "Proper Usage: python3 wordle_solver.py <filename>")
        return

    # check that the specified file exists
    infilename = sys.argv[1]
    if not os.path.exists(infilename):
        print("Error: input file specified does not exist.",
            "Proper Usage: python3 wordle_solver.py <filename>")
        return

    wordle_solve(infilename)    # solve particular instance of the game
    return


if __name__ == "__main__":
    main()
