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
            'age' : '12'
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

print(Biography.get('Children')) # {'1st_born': {'name': 'quil', 'age': 15}, '2nd_born': {'name': 'Rufus', 'age': '12'}}
print(Biography.get('Networth')) # None
print(Biography.get('Children''1st_born'))