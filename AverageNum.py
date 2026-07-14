# Ask the user how many numbers they want to enter
num = int(input("Range of numbers: "))

# Create a variable to store the total sum of all the numbers
numberSum = 0

# Repeat the loop 'num' times
for n in range(num):

    # Ask the user to enter a number and convert it to a float
    numbers = float(input("Enter Number: "))

    # Add the entered number to the running total
    numberSum = numberSum + numbers

# Calculate the average by dividing the total sum by the number of values entered
avg = numberSum / num

# Display the average to the user
print("Average of numbers is:", avg)
