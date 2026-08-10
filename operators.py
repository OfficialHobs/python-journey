# x = 5%2
# print(x)
# newx = x // 4
# print (newx)
# oldx = x +3
# print (oldx)

# Age = int(22)
# print(Age)
# Height = float(170.22)
# print (Height)
# Complex = 1 + 1j
# print (Complex)

#Area of a triangle

# Base = int (input("enter base: "))
# Height = int (input("enter height: "))
# Area_traingle = float (0.5 * Base * Height)
# print("Area of triangle = ", Area_traingle)

# perimeter of a triangle
# A = int (input("enter side A: "))
# B = int (input("enter side B: "))
# C = int (input("enter side C: "))

# area_of_triangle = A+B+C
# print (area_of_triangle)

#calculating perimeter and area of a rectangle
# length = int (input("enter length: "))
# width = int (input("enter width: "))

# area = length * width
# perimeter = 2 * (length + width)
# print (area, perimeter)

#calculating the area and circumference of a circle

# radius = float (input("what is the radius? "))
# pi = float (3.14)
# area = float (pi * radius **2)
# circumference = float (2 * pi * radius)
# print (area, circumference)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# calculating the slope of a line and the euclidean distance

# x1, y1, x2, y2 = 2,2,6,10
# slope1 = (y2-y1) / (x2-x1)
# euclidean = (x2-x1) + (y2-y1)
# print (slope1)
# print (euclidean)

# # Calculate the slope, x-intercept and y-intercept of y = 2x -2
# # slope == y = mx+b

# b= -2
# m = 2
# y_intercept = b
# slope =m
# #where  y is 0
# x_intercept = -b / m
# print (x_intercept)
# print (y_intercept)
# print (slope)



# #ccomparwe slope 8 and 9
# if slope > slope1:
#     print('slope is bigger: ', slope)
# else:
#     print("slpoe1 is bigger: ", slope1)    



# Calculate the value of y (y = x^2 + 6x + 9).
# Try to use different x values
# and figure out at what x value y is going to be 0.

# for x in range(-6, 1):
#     y = x**2 + 6*x + 9
#     print(f"x = {x}, y = {y}")
# # the {} allows use to put a value in a string


# print(len("python"))
# print(len("dragon"))
# print(len("python") > len("dragon"))

# print("on" in "python" and "on" in "dragon")
# print("jargon" in "I hope this course is not full of jargon")
# print("on" not in "jargon")
# word = len("python")
# newword= float(word)
# finalValue = str(newword)
# print(str(finalValue))

# num1 = float(input("enter a number: "))
# if num1 % 2 == 0:
#     print (True)
# else:
#     print (False)    

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# print(7//3 == int(2.7))

# Check if type of '10' is equal to type of 10
# Check if int('9.8') is equal to 10

# # print("10"==10)
# a = int('9.8')
# b = 10
# print(a == b)
# # print(int("9.8") == 10)

# Write a script that prompts the user to enter hours and rate per hour.
#  Calculate pay of the person?

# hour = float(input("enter hour worked per day: "))
# rph = int(input("enter rate per hour(amount): "))
# perweek = rph*hour*7
# print("total amount to be paid for week: ", perweek)

# Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
# Yrs = int(input("enter your age: "))
# TotalSecs = Yrs*365*24*60*60
# print(TotalSecs)

#Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for n in range(1, 6):
    print(n, 1, n, n**2, n**3)