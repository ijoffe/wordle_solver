# Made by Isaac Joffe

with open("base_words.txt") as file:
    words = (file.read()).split()

test_word = "tears"
while(True):
    print("Try word", test_word)
    result = input("Enter Result: ")
    words_to_remove = []
    if result == "ggggg":
        break
    for number in range(len(result)):
        if result[number] == "g":
            for word in words:
                if word[number] != test_word[number]:
                    words_to_remove.append(word)
        elif result[number] == "y":
            for word in words:
                if test_word[number] not in word:
                    words_to_remove.append(word)
                if test_word[number] == word[number]:
                    words_to_remove.append(word)
        elif result[number] == "b":
            for word in words:
                if test_word[number] in word:
                    words_to_remove.append(word)
    for word in words_to_remove:
        if word in words:
            words.remove(word)
    test_word = words[0]
