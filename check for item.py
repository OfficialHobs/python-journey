# Create a list of fruits
fruits = ["apple", "banana", "orange", "mango"]

# Asking for the user to enter a fruit
item = input("Enter a fruit: ")

# Chek if the fruit is in the list and then pring it
if item in fruits:
    print(item, "is on the list.")
else:
    print(item, "is not in the list.")