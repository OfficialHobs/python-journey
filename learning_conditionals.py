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
# another example
a = 10
if a // 2 == 1 and  a % 2 == 0:
        print('a is 10') 
elif a // 2 == 5 and a % 2 == 1:
    print('a is odd number') # if the 1st 'if' is true and the 2nd is false--
elif a == 10:
    print('no = 10') #unless this is true, iteration moves to 'else'
else:
    print('not defined') #output