for i in range(6):
    print("@"*i)
 
# A
# BB
# CCC
# DDDD
# EEEEE
a = 65
for i in range(1,6):
    print(chr(a)*i)
    a+=1

#       A
#      B B
#     C C C
#    D D D D
#   E E E E E       
a = 65
for i in range(1,6):
    print(" "*(6-i),f"{chr(a)} "*i)
    a+=1
    
# A
# BC
# DEF
# GHIJ
# KLMNO
a = 65 
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(a), end="")
        a += 1
    print()