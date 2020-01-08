def is_palindrom(word):
    return word == word[::-1]


def is_anagram(word_1, word_2):
    return sorted(word_1) == sorted(word_2)


if __name__ == '__main__':
    word_1 = input("Please give the first word: ")
    word_1 = word_1.lower()
    word_2 = input("Please give the second word: ")
    word_2 = word_2.lower()

    for word in [word_1, word_2]:
        if is_palindrom(word):
            print('Word "{}" is palindrom.'.format(word))
        else:
            print('Word "{}" is not palindrom.'.format(word))

    if is_anagram(word_1, word_2):
        print('Words "{}" and "{}" are anagram.'.format(word_1, word_2))
    else:
        print('Words "{}" and "{}" are not anagram.'.format(word_1, word_2))
