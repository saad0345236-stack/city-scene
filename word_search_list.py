# Creating a list and searching for a word:
print("Enter any 3 things into the list by entering them below:")
words = []
entry_1 = input("1st Word: ")
words.append(entry_1)
entry_2 = input("2nd Word: ")
words.append(entry_2)
entry_3 = input("3rd Word: ")
words.append(entry_3)
print("Good job! If the thing is in the list we'll print 'True' otherwise we'll print 'False'. What's the word you want to search?")
search = input("Word: ")
print(search in words)