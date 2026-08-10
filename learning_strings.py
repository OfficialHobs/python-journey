# multiline = '''my nam is jonh doe
# i am a man with two cars
# i have twelve jobs
# i want to work harder to become the richest person in the world'''
# # print(multiline)

# single_line = 'my name is john doe ' \
# 'i hanve two cars'
# print(single_line)

# concatenation
# firstname = "john"
# lastname = "doe"
# space = " "
# proffesion = "developer"
# profile = proffesion +space+ lastname +space+ firstname
# print(profile)
# print(len(firstname)>len(lastname))

# # \ escape sequences
# print("my name is \n John doe") #\n creates new line
# print("days\ttopic\texercise") #\t create tab = 8 spaces between two words
# print("1\t5\t20")
# print("2\t2\t8")
# print("3\t3\t12")
# print ("this is backslash symbol \\ to write a new backslash symbol")
# print('my name is \"John doe\"') # \"\" allows you to write "" in a sentence

# string formating== %s or %d or %f or %.2f or %.3f --argument specifiers used to format values of a var
# to string or int or float or even float of signifacant figures
# subject = "maths"
# classroom = "grade 4"
# Bio = "my best subject is %s and im in %s" %(subject, classroom) #%s formats the values of subject
# print(Bio) # output = my best subject is maths and im in grade 4
# # print("my best subject is %s and i'm in %s")

# radius = 10
# pi = 3.14
# area = pi * radius**2
# formatted_str = "the area of a circle with radius %d is %.2f." %(radius, area)
# print(formatted_str)

# python_library = ["django", "flask", "nmupy"]
# formatted = "the python library include:%s" %(python_library)
# print(formatted)

# name = "nasir"
# lname = "bashir"
# fullname = "your name is {} {}" .format(name,lname)
# print(fullname)

# num1 = 4
# num2 = 2
# summation = "{} + {} = {}" .format(num1,num2,num1+num2)
# print(summation)
# print("the sum of the numbers is: {} ".format(num1+num2))


# radius = 10
# pi = 3.14
# area = pi * radius**2
# print("the area of a circle with radius {} is {:.2f}".format(radius,area))

# string interpolation-- f""  this allows us to directly add a value into a string in print()
# num3 = 4
# num4 = 5
# print(f"{num3} + {num4} = {num3+num4}")
# print (f"{num3} / {num4} = {num3/num4:.2f}")

# unpacking characters from a string
# syntax
character = "python"
a,b,c,d,e,f = character #now with this a = p,b=y,c=t,...
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)