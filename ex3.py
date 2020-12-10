some_string = input("Enter some string: ")


def long_word(some_string):
    any_string = some_string.split()
    check_word = 0
    for i in any_string:
        if len(i) > check_word:
            check_word = len(i)
            word = i
    return word


print("Longest word is: " + long_word(some_string))
