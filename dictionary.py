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
dict1 = {'key1' : 'ppp', 'key2' : 'hhh', 'key3' : 'kkk', 'result' : ['first', 'second', 'third']}
# dict1['key4'] = 'rrr'
# # dict1['key5'].append('uuu') #error
# dict1['result'].append('fourth')
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

# testing testing
Building = {
    'house1' : {
        'type':'duplex', 
        'address':'dart street'}, 
    'house2' : 'mansion', 
    'house3' : 'bungalow'}
print(Building)
# Building.popitem('house1',{}).popitem('type')
del Building['house1']['type']
print(Building)