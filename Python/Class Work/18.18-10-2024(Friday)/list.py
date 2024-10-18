# Creating a list
my_list = [1, 2, 3, "Hello", 6]

# Accessing elements
print("Index")
print(my_list[0])  
print(my_list[3])    

# Modifying elements
print("modification by index")
my_list[1] = "World"
print(my_list)  

# Appending elements
print("Append")
my_list.append(7)
print(my_list)  

print("Extend")
my_list.extend([4,5,6])
print(my_list)

print("insert")
my_list.insert(2,"Python")


# removing elements
print("Remove")
my_list.remove(6)
print(my_list)

print("Pop")
my_list.pop()
print(my_list)

my_list.pop(1)
print(my_list)


