numbers = [4, 6, 1, 2, 3, 4, 5, 9, 8]
largest = numbers[0]
smallest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest element : ", largest) 
print("Smallest elements : ",smallest)
