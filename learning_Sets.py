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

# # Names.pop() #removes a random item ---in the set and returns that item to you
# popout = Names.pop() #for example
# print(popout)
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
# We can join two sets using the union() or update() method or | symbol
# set1 = {'chain', 'rakash', 'jelly', 'fan'}
# set2 = {'karl', 'hello', 'burner', 'fan'} # i intentionally add fan to see if .union removes one of it
# # print(set1.union(set2)) # as suspected a U b gives unique items as combination and removes 1 'fan'
# # # we can also say
# # print(set1 | set2)

# # # adding a set to a set. same as union though but we use .update() like prev
# # print(set1.update(set2)) #this will give output : none because it is saying 
# #                          # 'do -action' to these, same as .remove

# # better solution
# updated = set1.update(set2) # add set2 inside set1
# print(set1) # we print set1 because we are update set1 actually

# ---------------------------------------------------------------------------------------------
#there some methods that return actual output like .pop(), .union(), .intersection
# there are some that doesnt return anything but only modifiy the set it self
# examples are .sort, .update, ..... 

# intersection of a set
# first = {'jerry', 'tom', 'bull', 'dog'}
# second = {'tom', 'dog', 'karen', 'cat'}
# # # #first.intersection(second) # this intersects the set and returns a value
# # # that value needs to be stored and it is what we are looking for...therefore
# intersect = first.intersection(second) # now we store that value in intersect
# print(intersect)
# intersect2 = second.intersection(first)
# print(intersect2)

# checking a subset of and superset of sets
# .isubset() and .issuperset() --- we expect an output. 
# it doesnt really modify a particular set but compares both set
# setA = {0,1,2,3,4,5}
# setB = {1,2,3}
# print(setA.issubset(setB)) # False
# print(setA.issuperset(setB)) # True
# print(setB.issubset(setA)) #True
# print(setB.issuperset(setA)) #False

# finding the difference between two set
# .difference() -- what this does is to check difference of set1 from set2 
# IT DOESNT REALLY FOLLOW THE SUBTRACTION LOGIC BUT difference between a from b
# so if set1  = 1,2,3 and set2 =3,4.... the difference of set1 from set2 is that set1 has 1,2
# .difference is only checking for the first set and comparing it to the second one 
# not the both at the same time. if not that would result to diff = 1,2,4
# set1 = {1,2,3,4,5,6}
# set2 = {3,4,5,7}
# print(set1.difference(set2)) # expected output: {1,2,6}
# print(set2.difference(set1)) # expected output: {7}

# python = {'p','y','t','h','o','n'}
# dragon = {'d','r','a','g','o','n'}
# print(python.difference(dragon)) # output: {p,y,t,h} --- understood?
# print(dragon.difference(python)) # output: {d,r,a,g} --hey both have {o,n} in common but dragon has d,r,a,g

# # Now to tackle this problem of simply returning one difference
# #  .symetrical_difference()
# # this would give us the combination ofthe diffrence A from B  +  B from A
# print(python.symmetric_difference(dragon)) #output: {p,y,t,h,d,r,a,g} as we probably would have wanted

# disjoint of two sets
# if two sets have entirely different items, we say they are disjoint of each other
# .isdisjoint()
set1 = {0,2,4,6,8}
set2 = {1,3,5,7,9}
set3 = {1,2,3,4,5}
print(set1.isdisjoint(set2)) # true
print(set2.isdisjoint(set3)) #false {1,3,5}
print(set3.isdisjoint(set1)) #false {2,4}