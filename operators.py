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

x1, y1, x2, y2 = 2,2,6,10
slope1 = (y2-y1) / (x2-x1)
euclidean = (x2-x1) + (y2-y1)
print (slope1)
print (euclidean)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# slope == y = mx+b

b= -2
m = 2
y_intercept = b
slope =m
#where  y is 0
x_intercept = -b / m
print (x_intercept)
print (y_intercept)
print (slope)



#ccomparwe slope 8 and 9
if slope > slope1:
    print('slope is bigger: ', slope)
else:
    print("slpoe1 is bigger: ", slope1)    