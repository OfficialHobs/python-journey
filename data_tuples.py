# #creating possibilities with list
# my_list = [(i, j) for i in range(5) for j in range(4)]
# print(my_list)

# # creating a table with list
# mylist = [[i for i in range (4)] for j in range (3)]
# print (mylist)


# # printing a list[] of number 0-9
# list2 = [x for x in range (10)]
# print(list2)

# # printing a list[] of number 0-9
# list2 = []
# for x in range (10):
#     list2.append(x)
#     # print (list2) # indentation
# # indentation of print stops the print from being part of the loop
# print (list2)

#creating a list to print range 3, three time
# list3 =[]
# for x in range(3):
#     for y in range(3):
#         list3.append(x)
# print(list3)


# 
# for x in range (1,4):
#     print(x,1,x**2,x**3)

#Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

# for x in range (1,6):
#     print(x,x**0,x**1,x**2,x**3)
li = [i for i in range (0,101)]
li2 = li[3 : 9 : 3]
print (li2)