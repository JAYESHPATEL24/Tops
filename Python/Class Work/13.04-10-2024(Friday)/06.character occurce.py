# occurance of character in string(parameterized Function)

def character_occur(s):

    d = {}
    
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
            
    return d

str = input("Enter a String : ")

print(f"Occurnce of characters : {character_occur(str)}")