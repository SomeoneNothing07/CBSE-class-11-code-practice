
# Taking input from the user
a = int(input('Enter the no. for finding the factorial : '))

# Initialize the variable to store the result
f = 1

# Loop backwards from a down to 1
for i in range(a, 0, -1):
    # Multiply the current result by the loop variable
    f = f * i

# Print the final factorial result
print(f)
