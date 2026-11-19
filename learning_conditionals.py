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
Score = int(input('Enter your score: '))

if Score >= 90 and Score <= 100:
    print('Grade: A')
elif Score >= 80 and Score <= 89:
    print('Grade: B')
elif Score >= 70 and Score <= 79:
    print('Grade: C')
elif Score >= 60 and Score <= 69:
    print('Grade: D')
elif Score >= 0 and Score <= 59:
    print('Grade: F')
else:
    print('invalid Score!')