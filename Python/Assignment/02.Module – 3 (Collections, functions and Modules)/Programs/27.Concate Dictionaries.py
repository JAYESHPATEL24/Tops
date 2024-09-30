# Write a Python script to concatenate following dictionaries to create a new one.  

    # Dictionaries
d1 = {1 : "Hello", 2 : "Welcome", 3 : "My Friend"}
d2 = {4 : 4.5, 5 : 6.4, 6 : 8.4}
d3 = {7 : 10, 8 : 20, 9 : 30}

d ={}
    # concatenate all dictionaries into single dictionary.
for i in (d1,d2,d3):
    d.update(i)
    
print(d)