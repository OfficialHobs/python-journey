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


