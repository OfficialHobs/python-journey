# find the largest number in the list
# O of n complexity
numbers = [12, 7, 45, 23, 18]

largest = numbers[0]
lowest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    elif number < lowest:
        lowest = number

print("Largest:", largest)

print("Lowest:", lowest)
