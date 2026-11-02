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
# cars = ('toyota', 'honda', 'ferrari', 'BMW')
# # print(cars[-3]) #'honda'
# # print(cars[3]) # 'BMW'
# # print(cars[-1]) # 'BMW'

# # slicing a tuple
# # print(cars[0:2]) #toyata, honda 
# # honda_ferrari = cars[1:3] #honda, ferrari
# # print(honda_ferrari)

# # negative indexing
# print(cars[-4:-1])# skips BMW
# print(cars[-4:])# prints all the list
# print(cars[-4:-2]) #toyota,honda
# print(cars[-1:-3]) #returns () empty beacause default -> direction
# print(cars[-1:-3:-1])# (bmw,ferrari) direction is given. -1 means reverse the slice

# generally, tuple is immutable
# changing tuple to list
# subject = ('maths', 'english', 'physics', 'literature')
# list_subjects = list(subject) # ['maths', 'english', 'physics', 'literature']
# list_subjects[0] = 'science' # ['science', 'english', 'physics', 'literature']
# print(list_subjects)

# # change back to tuple
# tuple_subject = tuple(list_subjects)
# print(tuple_subject) # ('science', 'english', 'physics', 'literature')
# # tuple_subject[0] = 'math' # error
# # print(tuple_subject)

# # checking an item in a tuple
# furnitute = ('chair', 'table', 'shelves', 'windows')
# print('chair' in furnitute) #True
# print('AC' in furnitute) #False

# # joining tuples together
# items = ('cake', 'chicken', 'candle', 'cow')
# items2 = ('berry', 'bag', 'banner', 'bull')
# # a siple concatenation method woould work
# joined_items = items + items2
# print(joined_items)

# deleting a tuple
# its not possible to remove an item from the tuple but you can delete the whole thing
# lastexample = ('tuple', 'list')
# del lastexample
# # # or
# # del(lastexample)
# print(lastexample)# Error

# exerise
#  Create an empty tuple
music = ('afro','jazz', 'pop', 'soul', 'R&B')
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers= ('sally', 'Aaron', 'rowan', 'bobby', 'Nelson')
sisters = ('amber', 'maddie', 'peace', 'nel')
# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
# How many siblings do you have?
print(len(siblings))
# Modify the siblings tuple and add the name of your father and mother 
# and assign it to family_members
family_members = list(siblings)
last_member = len(family_members) - 1
family_members.append('harold')
family_members.append('tess')
print(family_members)