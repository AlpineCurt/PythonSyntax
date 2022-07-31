def print_upper_words(list_of_words, letters):
    """prints a list of words in upper case that start with the specified letter"""
    for word in list_of_words:
        if word[0] in letters:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {"h", "y"})