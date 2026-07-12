# Building a coutndown timer:
print("This is a countdown timer. Enter a number below!")
number = int(input("Enter number: "))
while number >= 1:
    print(number - 1)
    number -= 1
print("Counting is finished.")