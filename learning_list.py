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
cars = ['volkwagen','toyota','honda','jeep']
end_index = cars[-1] #jeep
next_index = cars[-2] #honda
print(end_index)
print(next_index)