#test list

# empty_list = []
# print(len(empty_list))

# #full list
# fruits = ['orange','apple','lime','watermelon']
# print('number of fruits:',len(fruits)) # we use ',' to add the other items to print
# print('fruits:',fruits)
# print(' '.join(fruits)) # output = orange appple  lie wateremlon ====i learned this previously

#list can have multiple data types 
profile = ['habib', 'oluwa', str({'age':30, "score":100}), str(True)]
print(profile)
print(len(profile))
print(' '.join(profile))
# here is what i noticed: we cannot .join data type that is not string in python
# we have to convert them to str by saying str(original syntax data type) like above
# this will then convert the data to string first the join can now execute.
# therefore .join only supports strings.