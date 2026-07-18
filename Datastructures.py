                        # |||||
# x = set("hello")
# print(x)

# sets is unordered, x is the same as x2
# x = {1,2,3,4,4,5,5}
# x2 = {2,1,3,5,4,5,4}
# print(x==x2)

# set is mutable but can only take in one value at a time
# x = {1,2,3,4,4,5,5}
# x.add(6)
# print(x)

# set cannot contain immutable type of element like the list
# so the below code will return an error
# x = {[1,2,3,], 4,5}
# print (x)


# Linked list structure                 |||||||
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# # Create nodes
node1 = Node("Hello")
node2 = Node(20)
node3 = Node(30)

# # Link them together
node1.next = node2
node2.next = node3

# # Traverse the linked list
current = node1

while current:
    print(current.data)
    current = current.next


# Array or list (python) data structure         |||||
# Array (List)

numbers = [10, 20, 30, 40, 50]

# Access an element
print(numbers[2])

# # Add an element
numbers.append(60)
numbers.extend(70, 80 ,90 ,100)

# # Remove an element
numbers.remove(20)

# # Update an element
numbers[0] = 100

print(numbers)


# An array that cannot be modified is called a tuple
# Immutable array (Tuple)

numbers = (10, 20, 30, 40, 50)

print(numbers)

# Trying to modify it will give error
numbers[0] = 100

# or say
numbers.append(60)

fruits = ("Apple", "Banana", "Orange")

print(fruits)

print(fruits[1])



#stack list: this one ofllows the Last in first out formula LIFO|||
stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Pop
print(stack.pop())

print(stack)