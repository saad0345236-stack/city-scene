# Printing the letter "E":
numbers = [5, 2, 5, 2, 5]
for x_count in numbers:
    result = ''
    for item in range(x_count):
        result += 'x'
    print(result)
# Simplifying the code above to print 'L':
numbers_list = [2, 2, 2, 2, 5]
for x_count in numbers_list:
    print('x' * x_count)
# Finding the largest number from a list:
the_list = [6, 8, 9, 2, 10]
biggest = the_list[0]
for number in the_list:
    if number > biggest:
        biggest = number
print(biggest)
# Practing list methods:
list_2 = [7, 8, 5, 6, 7]
list_2.append(100)
list_2.insert(3, 60)
list_2.remove(7)
list_2.pop()
print(list_2.index(60))
print(list_2)
list_3 = [7, 6, 6]
list_3.clear()
print(list_3)
list_4 = [6, 6, 5, 6]
print(6 in list_4)
print(list_4.count(6))
list_5 = [3, 5, 4, 8]
list_5.sort()
list_5.reverse()
print(list_5)
list_6 = [5, 6, 7]
list_6.append(8)
list_7 = list_6.copy()
list_6.pop()
print(list_7)
print(list_6)