# to create a string, we ue {} or we say dict()
empty_string = {} # format of data will determine if its going to be a set or a dictionary
boys_class = {
    'Terry' : 'class A',
    'Paul' : 'class B',
    'Hero' : 'class C'
}
Biography = {
    'Name': 'Jay',
    'Age' : 40,
    'Country' : 'USA',
    'Is_married' : True,
    'Skills' : ['HTML', 'CSS', 'Java', 'Python'],
    # creating a dictionary in a dictionary == hahahaha
    'Children' : {
        '1st_born' : {
            'name' : 'quil',
            'age' : 15
        },
        '2nd_born' : {
            'name': 'Rufus',
            'age' : 12
        }
    }
}

# length of a dictionary
# print(len(Biography)) #6

# accessing a dictionary item
# We can access Dictionary items by referring to its key name. ie [''children]
# print(Biography['Children']) # {'1st_born': {'name': 'quil', 'age': 15}, '2nd_born': {'name': 'Rufus', 'age': '12'}}
# print(Biography['Children']['2nd_born']) # {'name': 'Rufus', 'age': '12'}
# print(Biography['Children']['2nd_born']['name']) # Rufus
# print(Biography['Skills'][2]) # Java

# Accessing an item by key name raises an error if the key does not exist. 
# To avoid this error first we have to check if a key exist or we can use the get method. 
# The get method returns None, which is a NoneType object data type, if the key does not exist.

# print(Biography.get('Children')) # {'1st_born': {'name': 'quil', 'age': 15}, '2nd_born': {'name': 'Rufus', 'age': '12'}}
# print(Biography.get('Networth')) # None
# print(Biography.get('Children'))

# # chained retrieval .get(), this is an advanced method i had to search up
# print(Biography.get('Children',{}).get('1st_born')) # chain .get
# print(Biography.get('Children',{}).get('1st_born',{}).get('name')) # quil
# print(Biography.get('Children',{}).get('1st_born',{}).get('age')) # 15

# adding an item to a dictionary
# dict1 = {'key1' : 'ppp', 'key2' : 'hhh', 'key3' : 'kkk', 'result' : ['first', 'second', 'third']}
# dict1['key4'] = 'rrr' # this add a new key to the list
# dict1['key5'].append('uuu') #error - why because it is updating 'key5' which has not been created yet
# dict1['result'].append('fourth') # success because it is updating result which has been created already
# print(dict1)

# # modifying a dictionary
# dict1['key1'] = 'lll'
# print(dict1) #{'key1': 'lll', 'key2': 'hhh', 'key3': 'kkk', 'result': ['first', 'second', 'third', 'fourth'], 'key4': 'rrr'}

# # checking keys or items in a dictionary
# print('key3'in dict1) #True
# print('key9' in dict1) #False

# removing key or items in a dictionary
# we use .pop() to remove a certain item .pop(item)
# Building = {'house1' : 'duplex', 'house2' : 'mansion', 'house3' : 'bungalow'}
# # Building.pop() # error, unlike list, using .pop() require you to pass an argument ('item')
# Building.pop('house2')
# print(Building)
# #  --- if you dont want ot pass an argument
# Building = {'house1' : 'duplex', 'house2' : 'mansion', 'house3' : 'bungalow'}
# Building.popitem() # removes the last item
# print(Building)
# # using del --- another way to remove an item in dictionary
# del Building['house1'] #deletes house1
# print(Building)

# # testing testing
# Building = {
#     'house1' : {
#         'type':'duplex', 
#         'address':'dart street'}, 
#     'house2' : 'mansion', 
#     'house3' : 'bungalow'}
# print(Building)
# # Building.popitem('house1',{}).popitem('type')
# del Building['house1']['type'] # output: as expected
# print(Building)

# changing dictionary to list
# we use .item()
# dictionary = {'animal1': 'panda', 'animal2':'rhino', 'animal3':'snake'}
# list_item = dictionary.items()
# print(list_item) # dict_items([('animal1', 'panda'), ('animal2', 'rhino'), ('animal3', 'snake')])

# # clearing a dictionary
# dictionary.clear() #none
# print(dictionary) #{}

# # Deleting a Dictionary
# dictionary = {'animal1': 'panda', 'animal2':'rhino', 'animal3':'snake'}
# del dictionary
# print(dictionary) # expected output = error- not defined

# copying a dictionary
# dictionary = {'animal1': 'panda', 'animal2':'rhino', 'animal3':'snake'}
# copy_dict = dictionary.copy()
# print(dictionary,copy_dict)
# print('is the same?:',dictionary == copy_dict) #True

# #  getting all keys in a dictionary ---- as a list 
# dictionary = {'animal1': 'panda', 'animal2':'rhino', 'animal3':'snake'}
# keys = dictionary.keys() # this gets the items name or keys
# print(keys) # dict_keys(['animal1', 'animal2', 'animal3'])

# Getting all Dictionary Values ----as a List
# dictionary = {'animal1': 'panda', 'animal2':'rhino', 'animal3':'snake'}
# values = dictionary.values()
# print(values) #dict_values(['panda', 'rhino', 'snake'])


# exercise

# Create an empty dictionary called dog
dog = dict()
# # Add name, color, breed, legs, age to the dog dictionary
# dog['name']=  'rufus'  
# dog['color'] =  'black' 
# dog['breed'] = 'pitbull'
# dog['legs'] = 4
# dog['age'] = 3
# print(dog)

# # or simply say---
# dog.update({'name': 'rufus', 'color': 'black', 'breed': 'pitbull', 'legs': 4, 'age': 3})
# print(dog)

# Create a student dictionary and add first_name, 
# last_name, gender, age, marital status, skills, 
# country, city and address as keys for the dictionary
student = {
    'first_name':'john', 
    'last_name': 'doe', 
    'gender':'male', 
    'age':23, 
    'marital status':'engaged', 
    'skills':['drawing', 'dancing', 'song writing'],
    'country': 'japan', 
    'city':'kyoto', 
    'address': 'kyoto, Japan'}
# Get the length of the student dictionary
# print(len(student))
# # Get the value of skills and check the data type, it should be a list
# value_skill = student['skills']
# print(value_skill) # ['drawing', 'dancing', 'song writing']
# print(type(value_skill)) # <class 'list'>
# # Modify the skills values by adding one or two skills
# student['skills'].append('HTML')
# student['skills'].append('CSS')
# print(student) # updated

# Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
del student['skills']
print(student)

# Delete one of the dictionaries
del student