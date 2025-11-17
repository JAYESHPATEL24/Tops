# # dictionary
# d = {1:"Bulati hai" , 2:"Magar" , 3:"Jane ka nai"}

# # get() return value of given key here we pass 1 so it returns "Bulati hai".
# print(d.get(1)) 

# # item() returns whole dictionary with key value pair
# print(d.items())

# # keys() returns on keys of dictionary.
# print(d.keys())

# # popitem() remove last key value pair of dictionary
# d.popitem()
# print(d)

# # pop() remove given key with its value.
# d.pop(2)
# print(d)

# # add whole dictionary (similar to extends in list)
# d.update({6:"Python",7:"Annoconda"})
# print(d)



# t = (1,2,3)
# d1= {}
# # fromkeys() converts whole tuple value into keys of dictionary and give them passed value here its is 20. by defalut value is none.
# print(d1.fromkeys(t,20))


d = {"1":"hello"}
d.update({"1":"hewwwwwlo","2":"jjshhs"})
print(d)

