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
print(len(Biography)) #6