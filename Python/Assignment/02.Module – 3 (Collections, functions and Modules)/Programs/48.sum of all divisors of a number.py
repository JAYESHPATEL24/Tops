#  Write a Python program to returns sum of all divisors of a number 

    # get a number from the user.
n = int(input("Enter a Number : "))

sum = 0
    # Find sum of all divisors of a number
for i in range(1,n+1):
    if n % i == 0:
        sum += i
        
print(f"The sum of all divisors of {n} = {sum}")
