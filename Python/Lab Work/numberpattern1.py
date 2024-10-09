# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444

n = int(input("Enter a Number : "))

# Calculate the size of the grid
size = 2 * n - 1

# Loop through each row
for i in range(size):
    # Loop through each column
    for j in range(size):
        # Calculate the value to print based on the minimum distance from edges
        print(n - min(min(i, j), min(size - 1 - i, size - 1 - j)), end=" ")
    # Move to the next line after finishing a row
    print()

    