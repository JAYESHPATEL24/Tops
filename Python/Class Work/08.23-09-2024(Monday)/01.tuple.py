t = (1,2,1.38,14,"You are best",True,3,1)

print(t.count(1))

print(t.index(14))


# we can not change in tuple because tuple is immutable.
# so if you wanna change
# convert tuple into list

l = list(t)         # type casting : tuple to list.
print(l)
l.extend([100,200,"Set limits, break limits"])
print(l)


t1 = tuple(l)       # type casting : list to tuple.
print(t1)