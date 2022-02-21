# Made by Isaac Joffe

import sys
import os.path
import pickle


def depickle(filename):
    """
    """

    with open(filename, 'rb') as infile:
        words = pickle.load(infile)
    return words


def wordle_solve(words):
    """
    """

    results = [0]
    while(len(words)):
        test_word = words[0]['word']
        print("Number of possible words:", len(words))
        print("Now try:", test_word)
        result = input("Enter result: ")
        results[0] += 1
        results.append(result)
        words_to_remove = []

        if result == "ggggg":
            print_results(results)
            break

        for number in range(len(result)):
            if result[number] == "g":
                for index in range(len(words)):
                    if words[index]['word'][number] != test_word[number]:
                        words_to_remove.append(index)

            elif result[number] == "y":
                for index in range(len(words)):
                    if test_word[number] not in words[index]['letters']:
                        words_to_remove.append(index)
                    if test_word[number] == words[index]['word'][number]:
                        words_to_remove.append(index)

            elif result[number] == "b":
                for index in range(len(words)):
                    if test_word[number] in words[index]['letters'] \
                        and test_word.count(test_word[number]) == 1:
                        words_to_remove.append(index)

        words_to_remove.sort(reverse=True)
        words_to_remove.insert(0, -1)
        for index in range(1, len(words_to_remove)):
            if words_to_remove[index] != words_to_remove[index - 1]:
                words.pop(words_to_remove[index])
    return


def print_results(results):
    """
    """

    print()
    print("Wordle XXX {}/6".format(results[0]))
    print()
    for index in range(results[0]):
        print(results[index + 1])
    return


def main():
    if len(sys.argv) != 2:
        print("Error: no input file specified.",
            "Proper Usage: <python3 wordle_solver.py <filename>>")
        return

    infilename = sys.argv[1]
    if not os.path.exists(infilename):
        print("Error: input file specified does not exist.",
            "Proper Usage: <python3 wordle_solver.py <filename>>")
        return

    words = depickle(infilename)
    wordle_solve(words)
    return


if __name__ == "__main__":
    main()
