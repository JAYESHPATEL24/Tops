s = input("Enter a String : ")

if len(s)%2 == 0 :
    print(s)
    
else:
    m = len(s)//2
    
    print(s[m-1]+s[m]+s[m+1])