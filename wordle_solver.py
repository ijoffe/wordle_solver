# Made by Isaac Joffe

import sys    # for command line arguments
import os.path    # to check that file exists
import pickle    # to serialize data


def depickle(filename):
    """
    Reads serialized data on the set of words into memory.

    Arguments:
        filename: string
            name of the pickled file to read from

    Returns:
        None, but reads the data into a vraible
    """

    with open(filename, 'rb') as infile:
        words = pickle.load(infile)
    return words


def wordle_solve(words):
    """
    Guesses the secret word according to input corresponding to the output of
    the game Wordle.

    Arguments:
        words: list of dictionaries
            contains all valid Wordle words along with data on what letters
            the word conatins and how useful the word is

    Returns:
        None, but continually prints words to try until the word is found
    """

    results = [0]    # initialize number of guesses
    # keep guessing as long as the set of valid words is not empty
    while(len(words)):
        test_word = words[0]['word']    # pick most valuable valid word
        print("Number of possible words:", len(words))
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
                # words are only valid with that letter in that exact spot
                for index in range(len(words)):
                    if words[index]['word'][number] != test_word[number]:
                        words_to_remove.append(index)

            elif result[number] == "y":
                # words are only valid with that letter, but not in that spot
                for index in range(len(words)):
                    if test_word[number] not in words[index]['letters']:
                        words_to_remove.append(index)
                    if test_word[number] == words[index]['word'][number]:
                        words_to_remove.append(index)

            elif result[number] == "b":
                # words are only valid if they do not contain that letter, but
                # exception is for letters that reoccured in the guess
                for index in range(len(words)):
                    if test_word[number] in words[index]['letters'] \
                        and test_word.count(test_word[number]) == 1:
                        words_to_remove.append(index)

        # put in descending order to avoid popping glitches
        words_to_remove.sort(reverse=True)
        # remove any and all words that are not possibly correct
        words_to_remove.insert(0, -1)    # so comparison remains valid
        for index in range(1, len(words_to_remove)):
            if words_to_remove[index] != words_to_remove[index - 1]:
                words.pop(words_to_remove[index])
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
    print("Wordle XXX {}/6".format(results[0]))    # print number of tries
    print()    # intentional blank line
    for index in range(results[0]):
        print(results[index + 1])    # print result of each guess
    return


def main():
    """
    Solves an instance of the Wordle game based on input data.

    Arguments:
        None, but reads the data of valid words from a specified file

    Returns:
        None, but continually prints words to try until the word is found
    """

    # check that file is specified
    if len(sys.argv) != 2:
        print("Error: no input file specified.",
            "Proper Usage: <python3 wordle_solver.py <filename>>")
        return

    # check that the specified file exists
    infilename = sys.argv[1]
    if not os.path.exists(infilename):
        print("Error: input file specified does not exist.",
            "Proper Usage: <python3 wordle_solver.py <filename>>")
        return

    words = depickle(infilename)    # read data on set of possible words
    wordle_solve(words)    # solve particular instance of the game
    return


if __name__ == "__main__":
    main()
