a = int(input("Enter a Number 1 : "))
b = int(input("Enter a Number 2 : "))
c = int(input("Enter a Number 3 : "))

if a>b:
    if a>c:
        print(f"{a} is Gretest Number.")
    else:
        print(f"{c} is Gretest Number.")

else:
    if b>c:
        print(f"{b} is Gretest Number.")
    else:
        print(f"{c} is Gretest Number.")