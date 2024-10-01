# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

    #list of decimal numbers
l = [12.4, 3.2, 9.8, 10.8, 5.6, 7.8, 1.4, 10.8, 11.9, 21.7]

    # Initialize max and min with the first element
max = l[0]
min = l[0]

    # find max and min
for i in l:
        # find maximum number.
    if i > max: 
        max = i
        # find minimum number.
    if i < min:
        min = i


print("Maximum number:", max)
print("Minimum number:", min)


