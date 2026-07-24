# Practicing functions:
def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
numbers = [2, 4, 6, 8]
print(find_max(numbers))
def ship_product():
    print("Product shipped.")
ship_product()
def product_tax():
    print("Product taxed.")
product_tax()