# name = input ('enter your name: ')
# print("your name is " , name, len(name))

# # print (input('enter your name:'))
# #  this one executes "input" first which allows you to enter name,
# #  then "print" which prints out your "input" 

# print (min (20,40,50))


# person_info = {
#                 'name' : 'habib',
#                 'city' : 'lagos',
#                 'age' : 20
#               }
# print (person_info['name'])
# person_info['name'] = 'tom' //changing the "name" item from habib to tom
# print(person_info['name']) // calling that item "name" from the variable


# my_name, my_age, my_city , am_i_married = ['habib' , 20 , 'lagos', True]
# print(my_age , type(my_age))
# print('i am ', my_age ,  'years old' )
# print(am_i_married)

# #getting use input
# first_name = input('waht is you first name: ')
# second_name = input('what is your second name: ')
# print ('your name is', first_name , second_name)

# check data types
# print (type({1,2,3}))
# print (type ([2,3,4,4]))
# print (type({'name':'habib'}))

# num1=10
# print(float(num1))
# num2=20.23
# print(int(num2))
# num3=30
# numstr= str(num3)
# print(numstr)


# # str to int or float
# num_str = '10.6'
# num_float = float(num_str)  # Convert the string to a float first
# num_int = int(num_float)    # Then convert the float to an integer
# print('num_int', int(num_int))      # 10
# print('num_float', float(num_str))  # 10.6
# num_int = int(num_float)
# print('num_int', int(num_int))      # 10

#another method from str to int. //note you cannot convert str to int straight up
#you need to convert  str' to 'float' first then 'int'
num4='10.23'
num_int= float(num4)
num_float= int(num_int)
print (num_float)

