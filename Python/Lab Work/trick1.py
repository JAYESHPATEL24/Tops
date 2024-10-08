# input : a1b10 output:abbbbbbbbbb

s = input("Enter a string : ")

s1 = ""
i=0

while i < len(s):
    count = 0
    ch = s[i]
    i += 1
    
    while i < len(s) and s[i].isdigit():
        count = count * 10 + int(s[i])
        i += 1

    s1 += ch * count
    
print(s1)