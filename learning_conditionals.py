# In python and other programming languages the key word if is used to check 
# if a condition is true and to execute the block code. 
# Remember the indentation after the colon.

# truly = 100
# if truly > 56:
#     print('yes it is true')

# # If condition is true the first block will be executed, if not the else condition will run.
# if truly > 200:
#     print('yes it is truly')
# else:
#     print('no it is not') # no it is not

# multiple conditions
# We use elif when we have multiple conditions.
# names = 'Jesse'
# if names == 'Jordan':
#     print('jesse = jordan')
# elif names == 'Jane':
#     print('jesse = jane')
# else:
#     print('they are not the same')

# Short Hand
# please study the syntax properly
# code = 'hello world'
# result1            condition                result2
# print('true') if code == 'world hello'else print('inverse')

# Nested Conditions
# a = 10
# if a // 2 == 1: # if the first condition is false, it will skip the nested 'if' and go to the 'elif'
#     if a % 2 == 0:
#         print('a is 10') #but if the 1st 'if' is true and this is true--
#     else:
#         print('a is odd number') # if the 1st 'if' is true and the 2nd is false--
# elif a == 15:
#     print('no = 15') #unless this is true, iteration moves to 'else'
# else:
#     print('not defined') #output


# if condition with logical operator
# We can avoid writing nested condition by using logical operator and.
# b = 20
# if b > 12 and 12 < b:
#     print('true condition')
# -----------------------------------
# another example
# a = 10
# if a // 2 == 1 and  a % 2 == 0:
#         print('a is 10') 
# elif a // 2 == 5 and a % 2 == 1:
#     print('a is odd number') # if the 1st 'if' is true and the 2nd is false--
# elif a == 10:
#     print('no = 10') #unless this is true, iteration moves to 'else'
# else:
#     print('not defined') #output

# If and Or Logical Operators
# d = 10
# if d == 5 or d % 2 == 0:
#     print('d is even or 10') # expected output
# else:
#     print('d is odd or 11')
# ------------------------------------------------------------------------------------------------
# Exercise
# Get user input using input(“Enter your age: ”).  
# If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years. Output:


# age = int(input("Enter your age: "))
# if age >= 18:
#     print('You are old enough to drive.')
# else:
#     required = 18 - age
#     # print('wait till you are: ', required)
#     print(f'wait till you are {18 - age}')
# ------------------------------------------------------------------------------------
# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:

# myAge = 22
# yourAge = int(input('enter your age:'))
# if myAge > yourAge:
#     if myAge - yourAge == 1:
#         print('i am older by a year')
#     elif myAge - yourAge > 1:
#         print(f'i am older by {myAge - yourAge} years')
# elif myAge == yourAge:
#     print('we are age mates')
# else:
#     print('your are older')
# -----------------------------------------------------------------------------------
# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, 
# else a is equal to b. Output:

# a = int(input('enter 1st number:'))
# b = int(input('enter 2nd number:'))

# if a > b:
#     print(f'{a} is greater than {b}')
# elif b > a:
#     print(f'{b} is greater than {a}')
# else:
#     print(f'{a} is equal to {b}')
# -----------------------------------------------------------------------------------------------------

# Write a code which gives grade to students according to theirs scores:
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# Score = int(input('Enter your score: '))

# if Score >= 90 and Score <= 100:
#     print('Grade: A')
# elif Score >= 80 and Score <= 89:
#     print('Grade: B')
# elif Score >= 70 and Score <= 79:
#     print('Grade: C')
# elif Score >= 60 and Score <= 69:
#     print('Grade: D')
# elif Score >= 0 and Score <= 59:
#     print('Grade: F')
# else:
#     print('invalid Score!')
# ------------------------------------------------------------------------------------------

# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

# Month = input('Enter a month: ').strip().capitalize() # this strips any space and 
# #                                           always capitalize the first alphabet the use wrote
# #                                      so if the user type all in small letter, 
# #                                      the first letter will automatically be changed 
# #                                      to caps so as to match the format in our list 

# if Month in ['September', 'October', 'November']:
#     print('the season is Autumn')
# elif Month in ['December', 'January', 'February']:
#     print('the season is winter')
# elif Month in ['March', 'April', 'May']:
#     print('the season is spring')
# elif Month in ['June', 'July', 'August']:
#     print('the season is Summer')
# else:
#     print('invalid month!')
# -------------------------------------------------------------------------------------------------


# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
# fruits = ['banana', 'orange', 'mango', 'lemon']
# print('available fruites are:',' '.join(fruits))
# new_fruit = input('Enter a new fruit: ').strip().lower() #strip and lower all case, to match existing list 
# if new_fruit in fruits:
#     print('That fruit already exist in the list!')
# else:
#     fruits.append(new_fruit)
#     print('Fruit successfully added!')
#     print(' '.join(fruits))
# ------------------------------------------------------------------------------------------------------

#  Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  If a person skills has only JavaScript and React, print('He is a front end developer'), 
# -if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# -if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# -
# else print('unknown title') - for more accurate results more conditions can be nested!
#  If the person is married and if he lives in Finland, print the information in the following format:
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }

# if 'skills' in person:
#     print(person['skills'][2])
# ---------------------------------
# if 'skills' in person:
#     if 'Python' in ['skills']:
#         print('true')
#     else:
#         print('false')
# -----------------------------------
# person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#         }
#     }

# if 'JavaScript' and 'React' in person['skills']:
#     print('He is a front end developer')
# ------------------------------------------------

# person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#         }
#     }
# if 'Node'and'Python'and 'MongoDB' in person['skills']:
#     print('He is a backend developer')

# ----------------------------------------------

# person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['React', 'Node', 'MongoDB'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#         }
#     }
# if 'React'and 'Node'and 'MongoDB' in person['skills']:
#     print('He is a fullstack developer')

# ---------------------------------------------------------
#  Asabeneh Yetayeh lives in Finland. He is married.
if person['is_married'] == True and person['country'] == 'Finland':
    print(person['first_name'], person['last_name'], "lives in", person['country'], '.', 'He is married.')