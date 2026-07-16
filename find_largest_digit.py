# Letting a user make a list and finding the largest number within it:
print("Enter any 4 single to triple digit numbers below to make a list:")
user_list = []
first = int(input("1st digit: "))
user_list.append(first)
second = int(input("2nd digit: "))
user_list.append(second)
third = int(input("3rd digit: "))
user_list.append(third)
fourth = int(input("4th digit: "))
user_list.append(fourth)
print(f"Good job, here's your list {user_list}")
question = input("Should we find the largest number? ").lower()
if question == "yes":
    print("Okay.")
    largest = user_list[0]
    for digit in user_list:
        if digit > largest:
            largest = digit
    print(f"The largest number is {largest}.")
elif question == "no":
    print("Okay, have a nice day!")
else:
    print("Invalid answer.")