# #creating possibilities with list
# my_list = [(i, j) for i in range(5) for j in range(4)]
# print(my_list)

# # creating a table with list
# mylist = [[i for i in range (4)] for j in range (3)]
# print (mylist)


# printing a list[] of number 0-9
list2 = [x for x in range (10)]
print(list2)

# printing a list[] of number 1-10
list2 = []
for x in range (1,11):
    list2.append(x)
    # print (list2) # indentation
# indentation of print stops the print for mbeing part of the loop
print (list2)