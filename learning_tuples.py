# creating a tuple
# we cannot modify a tuple; add, remove, patch..
tpl = ()
# or we use the tuple constuctor
tpl = tuple()

# checking tuple length
fruits = ('apple', 'mango', 'orange', 'berry')
lenght = len(fruits)
print(f"lenght of fruits: {lenght}")

# accessing a tuple 
first_fruits = fruits[0]
end_fruits = len(fruits) -1
lastfruits = fruits[end_fruits]
print('first fruits: ', first_fruits)
print('last fruits: {}' .format(lastfruits))