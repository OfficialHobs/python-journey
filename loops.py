# While loop--------------------------------------------------------------------------------------------
# We use the reserved word while to make a while loop. 
# It is used to execute a block of statements repeatedly until a given condition is satisfied. 
# When the condition becomes false, the lines of code after the loop will be continued to be executed.

# While loop
# syntax
# while condition:
    # code goes herehile Loop
# a = 0
# while a < 5: #while a is less than 5
#     print(a) # print a
#     a = a+1 # next, add a+1 then store it in a
# # print 0 1 2 3 4
#  ----when a = 5, a(5) is not greater than 5 therefore the loop ends 

# If we are interested to run block of code once the condition is no longer true, we can use else.
# a = 0
# while a < 5:
#     print(a)
#     a = a+1
# else:
#     print('loop ended')
#     print(a) # 5
# -----------------------------------------------------------------------------------------------------------
# Break and Continue
# Break: We use break when we like to get out of or stop the loop.

# digit = 0
# while digit < 4:
#     print(digit)
#     digit = digit + 1
#     if digit == 4:
#         break
#     #  0 1 2 3

# please it is not the same with else: rather, they work together
# E.g
# count = 0
# while count < 3:
#     password = input('Enter your password:')
#     count = count + 1 # look at the indentation, the count is still under the while loop just like the 'if'
#     if password == 'pass123': # quick check 
#         print('login successful')
#         break # if true, stop loop
# else:
#     print('locked! too many attempt')

# continue
# With the continue statement we can skip the current iteration, and continue with the next:

# count = 0
# while count < 5: # while  count  is less than 5,
#     if count == 3: #check -- if we have 3 as count, 
#         count += 1 # increment  ---count = 4
#         continue# and continue ----- i noticed is that of i comment out this line, it still gives same result
#     print(count) # 0 1 2 4 
#     count = count + 1      #    =5 from here loop ends 
#     #  final output = 0 1 2 4
