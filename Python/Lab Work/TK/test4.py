user = input("Enter : ")


print(user.isspace())
print(user.isalpha()) 

if user.isalpha() or user.isspace() or user == "":
    print("1")