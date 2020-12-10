original_string = input("Enter original string: ")
word_to_change = input("Enter word to change: ")
new_word = input("Enter new word: ")
number_of_changes = int(input("Number of changes: "))


def fake_string(original_string, word_to_change, new_word, number_of_changes):
    return original_string.replace(word_to_change, new_word, number_of_changes)


print(fake_string(original_string, word_to_change, new_word, number_of_changes))
