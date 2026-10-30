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

# name = ['benny', 'jaes']
# ages = [45, 34]
# cars = ['lambo', 'ferrari']
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

# fruits = ['banana', 'mango', 'apple', 'orange', 'grape']
# # fruits.sort() 
# # print(fruits.sort()) #genrally this returns None beause it only modifies the var 'fruits'
# print(fruits) # now this will return the sorted fruits that was atually modified

# # print(sorted(fruits)) #this is a method that only modifies the fruits in print but not the main var 'fruit'
# arrange = sorted(fruits) #this is another ethod to do 'sorted' method
# print(arrange) #now you see, a new sorted fruit is ccreate

# exercise
# delare an empty list
# empty_list = []
# # declare a list with or than 5 items
# item5 = ['cherry', '24', 'sales', 'accountant', 'dark']
# # find the lenght of your list
# print(len(item5)) # output =5
# #get the first item, middle and last item
# print(item5[0]) #cherry
# print(item5[2]) #sales
# last_item = len(item5) - 1
# print(item5[last_item]) #dark

# # Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
# mixed_data_type = ['harrold', 22, '170cm', 'single', 'nigeria']


# # Declare a list variable named it_companies and assign initial values
# #  Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Print the list using print()
# print(it_companies)
# # Print the number of companies in the list
# print(len(it_companies))
# # Print the first, middle and last company
# print([0])
# print([4])
# last_company = len(it_companies) -1
# print(last_company)
# Print the list after modifying one of the companies
# it_companies[2] = 'tecno'
# print(it_companies)
# # Add an IT company to it_companies
# it_companies.append('tesla')
# print(it_companies)
# Insert an IT company in the middle of the companies list
# it_companies.insert(3, 'dell')
# print(it_companies)
# # Change one of the it_companies names to uppercase (IBM excluded!)
# it_companies[3] = it_companies[3].upper() #we say the index 3 of it_companies = a modified index 3 
#                         #therefore it replaces index 3 with a new modified value of index 3 (DELL)
# print(it_companies)
# # Join the it_companies with a string '#;  '
# print('#; '.join(it_companies)) # Facebook#; Google#; Microsoft#; DELL#; Apple#; IBM#; Oracle#; Amazon

# # Check if a certain company exists in the it_companies list.
# isdellonthelist = 'DELL' in it_companies
# print(isdellonthelist) #True

# Sort the list using sort() method
# it_companies.sort()
# print(it_companies) #['Amazon', 'Apple', 'Facebook', 'Google', 'IBM', 'Microsoft', 'Oracle'] sorted a-z

# # Reverse the list in descending order using reverse() method
# it_companies.reverse()
# print(it_companies) # ['Oracle', 'Microsoft', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']

# Slice out the first 3 companies from the list
# firstslice = it_companies[3:]
# print(firstslice) # ['Google', 'Facebook', 'Apple', 'Amazon']

# # Slice out the last 3 companies from the list
# lastslice = it_companies[0:4]
# print(lastslice) # ['Facebook', 'Google', 'Microsoft', 'Apple']

# # Slice out the middle IT company or companies from the list
# print(it_companies[3:4]) #using the slice method to ouptut the center IT company 'apple'


# # Remove the first IT company from the list
# it_companies.remove('Facebook')
# print(it_companies) # ['Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# # Remove the middle IT company or companies from the list
# it_companies.remove('Apple')
# print(it_companies)

# Remove the last IT company from the list
# it_companies.remove('Amazon')
# print(it_companies) # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle']

# #Remove all IT companies from the list
# it_companies.clear()
# print(it_companies) # []

# del(it_companies)
# print(it_companies) # Expected output = error

# join the list
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# joinedlist = front_end + back_end
# print(joinedlist) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

# # After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack,
# #  then insert Python and SQL after Redux.
# full_stack = joinedlist.copy()
# print(full_stack) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
# full_stack.insert(5, 'Python')
# full_stack.insert(6, 'SQL')
# print(full_stack) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']


# The following is a list of 10 students ages:

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# # Sort the list and find the min and max age
# ages.sort() #sorts the list from smallest to largest
# minimum = ages[0] #first index since it is sorted a;ready
# maximum = ages [-1] #last index since it is sorted already
# # print(f"minimum: {minimum}") #19
# # print(f"maximum: {maximum}") #26

# # Add the min age and the max age again to the list
# ages.append(minimum)
# ages.append(maximum)
# print(ages) # [19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]

# # Find the median age (one middle item or two middle items divided by two)
# median_age = int((ages[5] + ages[6]) / 2)
# print(median_age) # 24

# # Find the average age (sum of all items divided by their number )
# average_age = sum(ages) / len(ages)
# print("Average age: ",average_age)

# # or we can do it manually and say
# total_age = 0
# total_count = 0
# for age in ages:
#     total_age += age
#     total_count += 1
# avg_age = total_age / total_count
# print(f"avg age = {avg_age}")

# # Find the range of the ages (max minus min)
# ranges = maximum - minimum
# print(f"range = {ranges}")

# # Compare the value of (min - average) and (max - average), use abs() method
# minav = minimum -average_age
# maxav = maximum - average_age
# print(abs(minav-maxav)) #-7 ---- abs(-7) = 7

# Find the middle country(ies) in the countries list
# countries = [
#   'Afghanistan',
#   'Albania',
#   'Algeria',
#   'Andorra',
#   'Angola',
#   'Antigua and Barbuda',
#   'Argentina',
#   'Armenia',
#   'Australia',
#   'Austria',
#   'Azerbaijan',
#   'Bahamas',
#   'Bahrain',
#   'Bangladesh',
#   'Barbados',
#   'Belarus',
#   'Belgium',
#   'Belize',
#   'Benin',
#   'Bhutan',
#   'Bolivia',
#   'Bosnia and Herzegovina',
#   'Botswana',
#   'Brazil',
#   'Brunei',
#   'Bulgaria',
#   'Burkina Faso',
#   'Burundi',
#   'Cabo Verde',
#   'Cambodia',
#   'Cameroon',
#   'Canada',
#   'Central African Republic',
#   'Chad',
#   'Chile',
#   'China',
#   'Colombia',
#   'Comoros',
#   'Congo, Democratic Republic of the',
#   'Congo, Republic of the',
#   'Costa Rica',
#   "Côte d'Ivoire",
#   'Croatia',
#   'Cuba',
#   'Cyprus',
#   'Czech Republic',
#   'Denmark',
#   'Djibouti',
#   'Dominica',
#   'Dominican Republic',
#   'East Timor (Timor-Leste)',
#   'Ecuador',
#   'Egypt',
#   'El Salvador',
#   'Equatorial Guinea',
#   'Eritrea',
#   'Estonia',
#   'Eswatini',
#   'Ethiopia',
#   'Fiji',
#   'Finland',
#   'France',
#   'Gabon',
#   'Gambia',
#   'Georgia',
#   'Germany',
#   'Ghana',
#   'Greece',
#   'Grenada',
#   'Guatemala',
#   'Guinea',
#   'Guinea-Bissau',
#   'Guyana',
#   'Haiti',
#   'Honduras',
#   'Hungary',
#   'Iceland',
#   'India',
#   'Indonesia',
#   'Iran',
#   'Iraq',
#   'Ireland',
#   'Israel',
#   'Italy',
#   'Jamaica',
#   'Japan',
#   'Jordan',
#   'Kazakhstan',
#   'Kenya',
#   'Kiribati',
#   'Korea, North',
#   'Korea, South',
#   'Kuwait',
#   'Kyrgyzstan',
#   'Laos',
#   'Latvia',
#   'Lebanon',
#   'Lesotho',
#   'Liberia',
#   'Libya',
#   'Liechtenstein',
#   'Lithuania',
#   'Luxembourg',
#   'Madagascar',
#   'Malawi',
#   'Malaysia',
#   'Maldives',
#   'Mali',
#   'Malta',
#   'Marshall Islands',
#   'Mauritania',
#   'Mauritius',
#   'Mexico',
#   'Micronesia',
#   'Moldova',
#   'Monaco',
#   'Mongolia',
#   'Montenegro',
#   'Morocco',
#   'Mozambique',
#   'Myanmar',
#   'Namibia',
#   'Nauru',
#   'Nepal',
#   'Netherlands',
#   'New Zealand',
#   'Nicaragua',
#   'Niger',
#   'Nigeria',
#   'North Macedonia',
#   'Norway',
#   'Oman',
#   'Pakistan',
#   'Palau',
#   'Palestine',
#   'Panama',
#   'Papua New Guinea',
#   'Paraguay',
#   'Peru',
#   'Philippines',
#   'Poland',
#   'Portugal',
#   'Qatar',
#   'Romania',
#   'Russia',
#   'Rwanda',
#   'Saint Kitts and Nevis',
#   'Saint Lucia',
#   'Saint Vincent and the Grenadines',
#   'Samoa',
#   'San Marino',
#   'Sao Tome and Principe',
#   'Saudi Arabia',
#   'Senegal',
#   'Serbia',
#   'Seychelles',
#   'Sierra Leone',
#   'Singapore',
#   'Slovakia',
#   'Slovenia',
#   'Solomon Islands',
#   'Somalia',
#   'South Africa',
#   'South Sudan',
#   'Spain',
#   'Sri Lanka',
#   'Sudan',
#   'Suriname',
#   'Sweden',
#   'Switzerland',
#   'Syria',
#   'Tajikistan',
#   'Tanzania',
#   'Thailand',
#   'Togo',
#   'Tonga',
#   'Trinidad and Tobago',
#   'Tunisia',
#   'Turkey',
#   'Turkmenistan',
#   'Tuvalu',
#   'Uganda',
#   'Ukraine',
#   'United Arab Emirates',
#   'United Kingdom',
#   'United States',
#   'Uruguay',
#   'Uzbekistan',
#   'Vanuatu',
#   'Vatican City',
#   'Venezuela',
#   'Vietnam',
#   'Yemen',
#   'Zambia',
#   'Zimbabwe'
# ] # Find the middle country(ies) in the countries list
# print(len(countries))
# halflist = len(countries) // 2
# print(halflist)
# print("middle country: ",countries[halflist]) #Lesotho [97] ----0-97

# # Divide the countries list into two equal lists if it is even if not one more country for the first half.
# print(countries[0:97])
# print(countries[97:195])

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
#  Unpack the first three countries and the rest as scandic countries.
country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country,second_country,third_country,*remainder_country = country
print("the first three is: ",first_country,second_country,third_country,'\n' "remainder: ",*remainder_country)