# okay this code will check the type of value you enter and return it type to you

value = input("Enter a value: ")


try:    #try checking if value can be converted to int
    value = int(value) # Can value be of this type? yes: print. NO: run the except function
except ValueError:
    try:
        value = float(value) # Can value be of this type? yes: print. NO: run the except function
    except ValueError:
        if value.lower() == "true": #this checks whether the value when converted to lower case
            value = True            #can be smae as true. if yes, store value as True bool
        elif value.lower() == "false": # same as truebut for false this time. so can the vale be 
            value = False              # converted to a sting false? yes, stores as False Bool

print(value) 
print(type(value)) # print the type of value