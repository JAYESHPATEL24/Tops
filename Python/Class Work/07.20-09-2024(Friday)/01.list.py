l = [1,1.23,2,3,2.45,True,False,"Hero","Vilain","Just me"]

# append() is used to enter a single element in the end of list. 
print("append()")
l.append(100)
print(l)

print()
# copy() is used for copy one list into another. 
l1 = l.copy()
print("copy()")
print(l1)

print()
# extend() is used for add a list or more than one elements in the end of list. 
print("extend()")
l.extend([100,150,"Happy Birthday Dear"])
print(l)

print()
# insert() is used to add element on perticular index. 
print("insert()")
l.insert(2,"Kam karo bhai kam karo")
print(l)

print()
# count() for count elements. 
print("Count()")
print(l.count(100))

# index() returns index of element. 
print()
print("index()")
print(l.index(1))

print()
# pop() remove elemets from index .(by default last element). 
print("pop()")
l.pop(3)
print(l)

print()
#  remove()  used for remove given element.
l.remove(100) 
print(l)

print()
# sorting
l1 = [3,65,57]
l1.sort()
print("sort()")
print(l1[::-1])