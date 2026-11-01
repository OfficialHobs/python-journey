# creating a tuple
# we cannot modify a tuple; add, remove, patch..
# tpl = ()
# # or we use the tuple constuctor
# tpl = tuple()

# # checking tuple length
# fruits = ('apple', 'mango', 'orange', 'berry')
# lenght = len(fruits)
# print(f"lenght of fruits: {lenght}")

# # accessing a tuple 
# first_fruits = fruits[0]
# end_fruits = len(fruits) -1
# lastfruits = fruits[end_fruits]
# print('first fruits: ', first_fruits)
# print('last fruits: {}' .format(lastfruits))

# negative indexing
        # -4        -3        -2        -1
cars = ('toyota', 'honda', 'ferrari', 'BMW')
# print(cars[-3]) #'honda'
# print(cars[3]) # 'BMW'
# print(cars[-1]) # 'BMW'

# slicing a tuple
# print(cars[0:2]) #toyata, honda 
# honda_ferrari = cars[1:3] #honda, ferrari
# print(honda_ferrari)

# negative indexing
print(cars[-4:-1])# skips BMW
print(cars[-4:])# prints all the list
print(cars[-4:-2]) #toyota,honda
print(cars[-1:-3]) #returns () empty beacause default -> direction
print(cars[-1:-3:-1])# (bmw,ferrari) direction is given. -1 means reverse the slice