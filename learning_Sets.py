# creating an empty set
# newset = set()
# # creating a set with initial items {curly braces is used} -----for [list] for (tuple)
# fruits = {'mango', 'cherry', 'orange', 'apple'}
# finding the length of a set - same as list
# print(len(fruits))
# # accessing an item in set - same also
# print("Is cherry in fruits:", 'cherry' in fruits) #True
# addign an item to the list
# fruits.add('grape')
# print(fruits)
# # adding multiple items to a set
# # we use .update([]) ---update takes a list arguement [] ---since we are adding multiple items
# fruits.update(['pineapple', 'berry', 'banana'])
# print(fruits)

# removing an item from the list
# we can use .remove() provided we have the item as arguement
Names = {'Aaron', 'Hero', 'Tyler', 'Mark', 'Jacob', 'King'}
# Names.remove('Tyler') # if 'Tyler' was not found, it would raisean error
# Names.discard('garry') # .disard() ---this doesnt return error, 
# # it only cares about deleteing the item ---whether it is found or not
# print(Names)
# Names.pop() #removes a random item ---in the set
# print(Names)

# if you want to know the exact item .pop() removed--
# delted_item = Names.pop()
# print(Names) #output the remainder of the set
# print(delted_item) #output the deleted item


# testing testing
# ret = Names.remove('Hero') #None is the ouput here because .remove is only a method that 
#                            # takes an arguement 'hero' to remove it.
#                            # it work is basically just an operation but .pop colleccts that data
# print(ret)

# clearing items in a set
# cars = {'tesla', 'toyota', 'bmw', 'honda'}
# # cars.clear()
# # print(cars) # set()

# # deleting the whole set itself
# del cars
# print(cars) #expected output = not defined or error basically

# converting a list to a set
# listm = ['ferro', 'dark', 'horizontal', 'slim', 'gold']
# listm = set(listm)
# print(listm) #expected output {set items}

# joining sets
