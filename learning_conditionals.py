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

# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:

myAge = 22
yourAge = int(input('enter your age:'))
if myAge > yourAge:
    if myAge - yourAge == 1:
        print('i am older by a year')
    elif myAge - yourAge > 1:
        print(f'i am older by {myAge - yourAge} years')
elif myAge == yourAge:
    print('we are age mates')
else:
    print('your are older')