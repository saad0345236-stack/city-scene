# Exercise:
name = input("Enter name: ")
if len(name) < 3:
    print("Name must be at least 3 character.")
elif len(name) > 20:
    print("Name can be a maximum of 20 characters.")
else:
    print("Name is valid.")
# Second Exercise:
weight = float(input("Weight: "))
asking = input("Lbs or Kg: ")
if asking.upper() == "LBS":
    kg = weight * 0.45
    print(f"You're {kg} kilos.")
elif asking.upper() == "KG":
    lbs = weight / 0.45
    print(f"You're {lbs} pounds.")
else:
    print("Invalid answer.")
# Practicing 'while' loops:
value = 1
while value <= 10:
    print('-' * value)
    value = value + 1
print("The end.")