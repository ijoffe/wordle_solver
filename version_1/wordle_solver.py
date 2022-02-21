# Made by Isaac Joffe


def main():
    """
    Guesses the secret word according to input corresponding to the output of
    the game Wordle.

    Arguments:
        None, but reads the set of valid words from a file called
        "base_words.txt"

    Returns:
        None, but continuallyr prints words to try until the word is found

    """

    # store file containing words as a list of strings of each word
    with open("base_words.txt") as file:
        words = (file.read()).split()

    test_word = "ouija"    # arbitrary but useful first guess of word
    while(True):
        print("Try word", test_word)    # tell user what to guess next
        result = input("Enter Result: ")    # obtain response to the guess
        words_to_remove = []
        if result == "ggggg":
            break    # code cracked, exit program

        # iterate through each letter of the guessed word
        for number in range(len(result)):
            if result[number] == "g":
                # words are only valid with that letter in that exact spot
                for word in words:
                    if word[number] != test_word[number]:
                        words_to_remove.append(word)

            elif result[number] == "y":
                # words are only valid with that letter, but not in that spot
                for word in words:
                    if test_word[number] not in word:
                        words_to_remove.append(word)
                    if test_word[number] == word[number]:
                        words_to_remove.append(word)

            elif result[number] == "b":
                # words are only valid if they do not contain that letter
                for word in words:
                    if test_word[number] in word:
                        words_to_remove.append(word)

        # remove any and all words that are not possibly correct
        for word in words_to_remove:
            if word in words:
                words.remove(word)
        test_word = words[0]    # set next guess from remaining possible words
    return


if __name__ == "__main__":
    main()
