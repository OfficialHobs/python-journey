#test list

# empty_list = []
# print(len(empty_list))

# #full list
# fruits = ['orange','apple','lime','watermelon']
# print('number of fruits:',len(fruits)) # we use ',' to add the other items to print
# print('fruits:',fruits)
# print(' '.join(fruits)) # output = orange appple  lie wateremlon ====i learned this previously

#list can have multiple data types 
# profile = ['habib', 'oluwa', str({'age':30, "score":100}), str(True)]
# print(profile)
# print(len(profile))
# print(' '.join(profile))
# here is what i noticed: we cannot .join data type that is not string in python
# we have to convert them to str by saying str(original syntax data type) like above
# this will then convert the data to string first the join can now execute.
# therefore .join only supports strings.

#accessing a list by index
# color = ['blue','red','yellow']
# print(color[0]) #blue
# last_index = len(color) -1 #len color = 3 -1 = 2.. so since last_index is 2, therefore..
# print(color[last_index]) #we are simply saying that [2] = [last_index] = yellow

# accessing a list item by negative index
# cars = ['volkwagen','toyota','honda','jeep']
# end_index = cars[-1] #jeep
# next_index = cars[-2] #honda
# print(end_index)
# print(next_index)

# upacking a list
# names = ['fola','berry','dami','kami','klaus']
# firstnm,secondnm,thirdnm,*remaindernm = names #that *remaindernm means store the rest of the LIST to this
# print(firstnm)#fola
# print(secondnm)#berry
# print(thirdnm) #dami
# print(remaindernm)# ['kami', 'klaus']

# numbers = [1,2,3,4,5,6,7,8,9,10]
# first,second,*remainder,last = numbers
# print(first) #1
# print(second) #2
# print(remainder) #[3,4,5,6,7,8,9] --- it stops at 9 because there is an extra var name(last) that follows
# print(last) #10

# string slicing
# alpa = ['a','b','c','d','e']
# # slice1 = alpa[0:] # ['a','b','c','d','e'] ---start from index 0 and dont stop to slice
# # slice2 = alpa[0:3] # ['a','b','c'] ----start from 0 and slice at index 3
# # slice3 = alpa[2:4] # ['c','d'] ---start from 2 =c and end 4=e but we cut at 'e' so output =d
# # slice4 = alpa[1:4:2] # ['b','d'] --start form b skip c to d , skip e to nothing

#  #                        -5  -4   -3   -2   -1
# # negslice = alpa[-5:] # ['a', b', 'c', 'd', 'e'] 
# negslice2 = alpa[-5:-1] # ['a', 'b', 'c', 'd']
# negslice3 = alpa[-1:-5:-1] #['e', 'd', 'c', 'b'] - but no 'a' - beause that is the stop same as positive cutting
# # print(slice1)
# # print(slice2)
# # print(slice3)
# # print(slice4)
# # print(negslice)
# print(negslice2)
# print(negslice3)
# print(alpa[-5:-1:1]) # -1 index('e') is the last element so it's not going to be output
# print(alpa[::-1]) #['e', 'd', 'c', 'b', 'a']


# modifying or updating a list
# boys = ['dele', 'harold', 'sam', 'kim']
# print(boys)
# boys[3] = 'jeff'
# print(boys)
# boys[-3] = 'ronny'
# print(boys)
# # changing the very last boy name assuming we dont know the index number
# lastboy = len(boys) -1
# boys[lastboy] = 'ben'
# print(boys)

# checking an item in a list
# girls = ['dera', 'iris', 'vera', 'tess', 'candice']
# print("tess" in girls)
# print('balli' in girls)
# # we can also store it inside a variable
# istrue = 'vera' in girls
# print(istrue)

# adding items to a list
# cities = ['tokyo', 'lagos', 'madrid', 'fulham', 'stuggart']
# print(cities)
# print('lille' in cities) #False ---- testing
# cities.append('lille')
# print(cities)
# print('lille' in cities) #True ---- testing

# inserting items to a list
# syntax
# lst = ['item1', 'item2']
# lst.insert(index, item)
# phone = ['iphone', 'samsung', 'google', 'tecno']
# phone.insert(2,'itel') # so insert takes two values - (index, item)
# print(phone)

# removing an item from a list

# item7 = ['food', 'cloth', 'bags', 'drinks']
# item7.remove('food') 
# print(item7)
# # let us add it back
# item7.insert(0,'food')
# print(item7)

# removing an item with pop
# pop removes indexes
# it may or may not take in arguement 
# item2 = ['car', 'plane', 'train']
# item2.pop() #removes the item on the last index
# print(item2)
# item2.append('train') #removes item 'train'
# print(item2)
# item2.pop(0) #remove item on the indexx 0 == 'car'
# print(item2)

# removing using del
# animals = ['dog', 'cat', 'goat', 'pig']
# del animals[0] #spot that it uses [] to take arguments
# print(animals) #dog is deleted --['cat', 'goat', 'pig']- 

# # lets add more to the list the delete again
# animals.append('cow') #['cat', 'goat', 'pig', 'cow']
# animals.append('hen') #['cat', 'goat', 'pig', 'cow', 'hen']
# print(animals)

# del animals[1:3]
# print(animals) #['cat', 'cow', 'hen']

# del animals #deletes the who list
# print(animals) #this should give error, because the list has been delete and does not exist

# clear-- we do not delete the list but erase the item in the list
# list1=[1,2,3,4]
# list1.clear()
# print(list1) #output == []. so no error

# copying a list
# game = [1,2,3,4,5]
# nwgame = game
# print(nwgame)

# play = ['ludo', 'chess', 'cards', 3]
# nwplay = play.copy()
# print(nwplay)

# joining a list
# we can joing by concatenating list + list

name = ['benny', 'jaes']
ages = [45, 34]
cars = ['lambo', 'ferrari']
# joinlist = name + ages + cars
# print(joinlist)

#  or we should use the method extend
# name.extend(ages)
# name.extend(cars)
# print(name)

# counting the nuber of times an item appear on the list
# print(name.count('benny')) #1

# # finding the index of an item
# print(name.index('jaes')) #1

# # reversing a list
# print(cars.reverse()) #['ferrari', 'lambo']

# sorting the list
# new = [1,3,4,2,5,6,8,7]
# # new.sort()
# # print(new) #ew has now been sorted and will reamin that way
# newso = new.sort()
# print(newso) # returns NONE
# # new.sort(reverse=True)
# # print(new)

# # using sorted - sorted sorts not does not modify the original list nw like sort does
# new2 = [2,4,6,7,5,3,1]
# print(sorted(new2)) # sorted list is outputed
# print(new2) #original unsorted list is iutputed
# print(sorted(new2,reverse=True)) #reerse the sorted list

fruits = ['banana', 'mango', 'apple', 'orange', 'grape']
# fruits.sort() 
# print(fruits.sort()) #genrally this returns None beause it only modifies the var 'fruits'
print(fruits) # now this will return the sorted fruits that was atually modified

# print(sorted(fruits)) #this is a method that only modifies the fruits in print but not the main var 'fruit'
arrange = sorted(fruits) #this is another ethod to do 'sorted' method
print(arrange) #now you see, a new sorted fruit is ccreate