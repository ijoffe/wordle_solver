# Made by Isaac Joffe

import sys    # for command line arguments
import os.path    # to check that file exists
import time


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


def wordle_solve(word, infilename):
    """
    Guesses the secret word according to input corresponding to the output of
    the game Wordle.

    Arguments:
        word: string
            the word that is being solved
        infilename1: string
            the name of the file containing the data on all possible words

    Returns:
        number: integer
            the number of guesses the solver took to solve the word
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

        if len(valid_words.wordset) > len(all_words.wordset) / 1000 + 1:
            test_word = all_words.wordset[0]["word"]
        else:
            test_word = valid_words.wordset[0]["word"]
            valid_words.wordset.pop(0)

        result = wordle(word, test_word)    # obtain response to the guess
        results[0] += 1    # one more guess has been entered
        results.append(result)    # make note of result of guess
        words_to_remove = []

        if result == "ggggg":
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
        if len(results) > 7:
            break

    number = len(results) - 1
    return number


def wordle(word, guess):
    """
    Gives the colour-based response to an word-guess pair, exactly how Wordle
    itself would.

    Arguments:
        word: string
            secret word trying to be cracked
        guess: string
            word being guessed by the wordle solver

    Returns:
        result: string
            string of colours to be interpreted by the solver
    """

    result = ""
    for index in range(len(guess)):
        if guess[index] == word[index]:
            result += "g"
        elif guess[index] not in word:
            result += "b"
        else:
            if guess.count(guess[index]) > word.count(guess[index]):
                result += "b"
            else:
                result += "y"
    return result


def test(infilename1, infilename2):
    """
    Guesses the secret word according to input corresponding to the output of
    the game Wordle.

    Arguments:
        infilename1: string
            the name of the file containing all possible words
        infilename2: string
            the name of the file containing all words ton test on

    Returns:
        None, but tests the solver against all possible instances
    """

    results = [0, 0, 0, 0, 0, 0, 0]
    with open(infilename1) as infile:
        test_words = infile.read().split()
    total = 0
    number = 0
    wrong_words = []
    start = time.time()
    for word in test_words:
        number += 1
        print("Algorithm solving instance {} of {}".format(number, len(test_words)))
        result = wordle_solve(word, infilename2)
        if result == 7:
            wrong_words.append(word)
            results[6] += 1
        results[result - 1] += 1
        total += result
    end = time.time()
    # print(results)
    correct = 0
    for number in range(len(results)):
        # print("Algorithm took {} tries {} times".format(number + 1, results[number]))
        if number < 6:
            correct += results[number]
    # print("Algorithm solved {} percent of cases".format(correct/len(test_words)*100))
    # print("Algorithm took an average of {} tries".format(total/len(test_words)))
    # print("Algorithm most often took {} tries".format(results.index(max(results)) + 1))
    # print("Algorithm took an average time of {} seconds".format((end-start)/len(test_words)))
    # print("Algorithm could not solve the following words:", ", ".join(wrong_words))

    print("SOLVED {:.1f}% OF CASES".format(correct/len(test_words)*100))
    print("TOOK AN AVERAGE OF {:.1f} ATTEMPTS".format(total/len(test_words)))
    print("TOOK AN AVERAGE TIME OF {:.2f} SECONDS".format((end-start)/len(test_words)))
    print("COULD NOT SOLVE THE FOLLOWING: {}".format(", ".join(wrong_words)))
    print("HISTOGRAM:")
    for index in range(len(results)):
        print("{}: {}".format(index + 1, "X"*int(results[index]/max(results)*20)))
    return


def main():
    """
    Solves an instance of the Wordle game based on input data.

    Arguments:
        None, but reads the data of valid and test words from specified files

    Returns:
        None, but calls the wordle solving function which continually prints
        words to try until the word is found
    """

    # check that files are specified
    if len(sys.argv) != 3:
        print("Error: no input file specified.",
            "Proper Usage: python3 wordle_solver.py <filename> <filename>")
        return

    # check that the specified file exists
    infilename1 = sys.argv[1]
    infilename2 = sys.argv[2]
    if not os.path.exists(infilename1) or not os.path.exists(infilename2):
        print("Error: input file specified does not exist.",
            "Proper Usage: python3 wordle_solver.py <filename> <filename>")
        return

    test(infilename1, infilename2)    # solve all instances of the game
    return


if __name__ == "__main__":
    main()
