# multiline = '''my nam is jonh doe
# i am a man with two cars
# i have twelve jobs
# i want to work harder to become the richest person in the world'''
# print(multiline)

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
# print("my best subject is %s and i'm in %s" ) 

# radius = 10
# pi = 3.14
# area = pi * radius**2
# formatted_str = "the area of a circle with radius %d is %.2f" %(radius, area)
# print(formatted_str)


# python_library = ["django", "flask", "nmupy"]
# formatted = "the python library include:%s" %(python_library)
# print(formatted)

# new style of string formating --- .format(var)
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
# techincally it allows us to perform operations inside print
# num3 = 4
# num4 = 5
# print(f"my name is {num3} + {num4} = {num3+num4}")
# print (f"{num3} / {num4} = {num3/num4:.2f}")

# unpacking characters from a string
# syntax

# character = "python"
# a,b,c,d,e,f = character #now with this a = p,b=y,c=t,...
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)



#accessing char by index number 
# language = 'Python'
# # first_letter = language[0] #p
# # second_letter = language[1]
# # print(second_letter) # y
# last_index = len(language) - 1
# last_letter = language[last_index]
# print(last_letter) # n

        #indexes
        #   012345
        #   -6-5-4-3-2-1
# language = 'python'
# last_index = language[-1]
# print(last_index)
# last_three = language[3:5] #slicing strings
# print(last_three)
# pto = language[0:5:2]
# print(pto)
# pto2 = language[-1:-7:-2]
# hon = language[-3:]
# hon2= language[3:]
# print(pto2, hon, hon2)

# greeting = 'Hello, World!'
# print(greeting[::-1]) # !dlroW ,olleH

# string formating = format strings using different methods
# challenge = 'thirty days of python'
# print(challenge.capitalize()) # Thirty days of python
# print(challenge.title()) # Thirty Days Of Python
# print(challenge.count('y')) # 3 - how many y's are in the string
# print(challenge.count('y', 7, 14)) # 1- how many y's are in the string from index 7 to 14
# print(challenge.endswith('on')) # True - does the string end with 'on' - a true or false statement
# print(challenge.endswith('tion')) # False - does the string end with 'tion' - a true or false statement

# challenge = 'thirty\tdays\tof\tpython'
# print(challenge.expandtabs()) # thirty  days    of      python - expands the tabs to 8 spaces
# print(challenge.expandtabs(10)) # thirty    days      of        python - expands the tabs to 10 spaces

# challenge = 'thirty days of python'
# print(challenge.find('y')) # 5 - finds the index of the first occurrence of y 
# print(challenge.find('th')) # 0 - finds the index of the first occurrence of 'th'
# print(challenge.find('abc')) # -1 - 'abc' is not found in the string

# print(challenge.rfind('y')) # 16 - finds the index of the last occurrence of y
# print(challenge.rfind('th')) # 17 - finds the index of the last occurrence of 'th'
# print(challenge.rfind('abc')) # -1 - 'abc' is not found in the string


# creating a string with already learned string formating methods
# first_name = "michael"
# last_name = "jordan"
# age = 33
# job = "basketball player"
# # sentence = "my name is {} {}. i am {} years old. " \
#         # "i work as a {}" .format(first_name,last_name,age,job)

# # print(sentence)

# # using old stlye foramtting
# # print("my name is %s %s and i am %d years old" %(first_name,last_name,age))
# new_sentence = ("my name is %s %s, i am a %s " 
#                 "and i am %d years old" %(first_name,last_name,job,age))
# print(new_sentence)

# radius = 10
# pi = 3.14
# area = pi * radius**2
# result = ("the area of a circle with radius {} is {}" .format(str(radius), int(area)))
# print(result) #the area of a circcle with radius 10 is 314.0

# challenge2 = "thirty days with python da"
# substring2 = "da"
# print(challenge2.index("da")) #print the lowest index where the substing "da" lies; which is = 7
# print(challenge2.index(substring2)) # output 7
# print(challenge2.index(substring2, 9)) # output an error as the substring "da"
# print(challenge2.index(substring2, 0, -1)) #output 7 - because startindex 0, endindex automatically is 
                                        #    -1 which is the last index- but lastindex are always excluded
                                        # in a slice like [0, -1]

# rindex now prints the highest index where "da" appears
# print(challenge2.rindex(substring2))
# print(challenge2.rindex(substring2, 0, -1))
# print(challenge2.find(substring2, 2)) # i did this only to test whether you can pass arguements to .find

# check for alpanumeric chars. using .isalnum
# Note that this doesnt support arguments i.e challenge.isalnum(substring3)
# challenge3 = "ThirtyDaysWithPythonDa" #Notice no space is used - this is what alphanumeric means
# substring3 = "Da"
# either
# print(substring3.isalnum())
# or we say
# print(challenge3.isalnum())
# and not this
# print(challenge3.isalnum(substring3)) # error as it doesnt support arguements

# isalpha - checks if the entire string is alphabet
# challenge4 = "thirty days of python"
# print(challenge4.isalpha()) #expected output = False beccause it contains space
# challenge5 = 'thirtydaysofpython'
# print(challenge5.isalpha()) #expected output = True

# isDecimal -chccks if all strings are decimal (0-9) dec
# new= '23'
# print(new.isalpha())
# print(new.isdecimal())
# nodec = '50 60'
# print(nodec.isdecimal()) #why? because '50 space 60' is not a digit of 0-9,
                        
# nodec2 = '5060'
# print(nodec2.isdecimal()) #but if it was 5060 = true

# digit = '0775hk6/'
# result = digit.isdigit()
# print(result)

# num = '\u00b2' # \u00b2 character represents the superscript two
# print(num.isdigit()) # apparently, because this is a Unicode character, it return as true digit
# print(num.isdecimal()) # returns false
# print(num.isnumeric()) # returns true because it checks if the characters are
# print(num.isidentifier()) # is valid variable name?

# letter = 'abcdef'
# print(letter.isupper()) 
# print(letter.islower())

# .joins lets you join all strings of an arguement (technologies- html,css..) together with a 'value'
# technologies = 'html', 'css', 'java'
# fruits = 'apple', 'mango', 'orange'
# # print(fruits.join(technologies)) #error
# print(fruits[0].join(technologies))
# print(', '.join(technologies))

# word = 'hello im biggire'
# print(word.strip('hie')) #removes arguent (all 'chars') from beginin and end
                        #  therefore, 'h' and 'e' begins and only 'e' ends.
                        # final result = llo i biggir..if we used ''hire' result = llo i bigg

# newvar = 'My name is celine'
# print(newvar.replace('celine', 'Tani')) # replace takes two argumemnt - current and new-(replacer)
# print(newvar.split()) #uses the comma to split or replace anywhere 'space' is found
# print(newvar.split('e')) #all 'e' is replaced by ','
# print(newvar.split('e ')) #the 'e space' = name space (nam e space) --- is replaced by ','
# print(newvar.split("m ")) #since no string end with "m space', it simply take all strings and combine as one
# print(newvar.swapcase()) #swaps the cace of the string = mY NAME IS CELINE
# print(newvar.startswith('My')) #true - because it starts with My


# excersize

# Concatenate the string 
# 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# first = 'thirty'
# second= 'days'
# third = 'of'
# fourth = 'python'
# join = first + ' ' + second + ' ' + third + ' ' + fourth
# print(join)

# # Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
# new1= "Coding"
# new2= "For"
# new3 = "All"
# new4 = "{} {} {}" .format(new1,new2,new3)
# print(new4)

# # Declare a variable named company and assign it to an initial value "Coding For All".
# company = "Coding For All"
# # Print the variable company using print().
# print(company)
# # Print the length of the company string using len() method and print().
# print(len(company))
# # Change all the characters to uppercase letters using upper() method.
# print(company.upper())
# # Change all the characters to lowercase letters using lower() method.
# print(company.lower())
# # Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# print(company.capitalize()) #first letter of sentence is capitalized
# print(company.title()) #Capitalize each string
# print(company.swapcase()) #cases are reversed
# # Cut(slice) out the first word of Coding For All string.
# print(company[7::])
# # Check if Coding For All string contains a word Coding using the method index, 
# # find or other methods.
# print(company.index('Coding')) # output 0'th index - that is the first index it can be found
# print(company.index('Coding', 0, -1)) # output 0'th index
# print(company.index('Coding', 7, -1)) #error output because Coding cannot be found in index 7 to -1
# print(company.find('Coding', 0, -1))    

# # Replace the word coding in the string 'Coding For All' to Python.
# print(company.replace('Coding', 'Python'))
# # Change "Python for Everyone" to "Python for All" using the replace method or other methods
# print('Python for Everyone'.replace('Everyone', 'All'))
# # Split the string 'Coding For All' using space as the separator (split()) .
# print(company.split())
# # "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
# # What is the character at index 0 in the string Coding For All.
# print(company[0])
# # What is the last index of the string Coding For All.
# print(company.rfind('l')) #rfind looks for the highest index of a particular character
# # What character is at index 10 in "Coding For All" string.
# print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'
# streep = 'Python For Everyone'

# s1 = streep[0]
# s2 = streep[7]
# s3 = streep[11]
# print(s1 + s2 + s3)
# # another method
# pfe = ''
# spleet = streep.split()
# # print(spleet)
# for word in spleet:
#         pfe += word[0]
# print(pfe)

# Create an acronym or an abbreviation for the name 'Coding For All'.
# dell = 'Coding For All'

# cut = ''
# newdell = dell.split()
# print(newdell)
# for strin in newdell:
#         cut += strin[0]
# print(cut)

# # Use index to determine the position of the first occurrence of C in Coding For All.
# print(dell.index('C'))
# # Use index to determine the position of the first occurrence of F in Coding For All.
# print(dell.index('F'))
# # Use rfind to determine the position of the last occurrence of l in Coding For All People.
# print(dell.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 
# 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
newword = 'You cannot end a sentence with because because because is a conjunction'
cut1 = newword.split()
print(cut1.index('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence:
#  'You cannot end a sentence with because because because is a conjunction'
oldword = 'You cannot end a sentence with because because because is a conjunction'
# cut2 = oldword.split()
# print(len(cut2))
print(oldword.rindex('because'))# NOTe that this outputs : index 47 of the whole string. no split is used

