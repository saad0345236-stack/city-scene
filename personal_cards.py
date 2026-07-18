# Creating 2 cards and allowing user to pick one of them:
name = input("Enter your name below for personal greeting card: ")
def greeting(name):
    print(f"Hi {name}! It's nice to meet you. This is your personal greeting card. Welcome aboard and we hope you have a good time.")
def goodbye(name):
    print(f"Goodbye {name}! I hope you had fun and it was really nice meeting you. Have a nice day!")
choice = input("Would you like a greeting card or a goodbye card? ").lower()
if choice == "greeting card" or choice == "greeting":
    greeting(name)
elif choice == "goodbye card" or choice == "goodbye":
    goodbye(name)
else:
    print("Sorry, that's an invalid answer.")