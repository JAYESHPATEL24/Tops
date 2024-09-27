# Write a Python function to check whether a number is perfect or not. 
    # function for check number is perfect or not.
def perfect_number(n):
    
    sum = 0

        #calculate sum of divisors of number. 
    for i in range(1, n):
        if n % i == 0:
            sum += i

        # Check if sum of divisors is equals the number
    if sum == n:
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is not a perfect number.")
    
    # Input the number
n = int(input("Enter a number: "))

    # function call
perfect_number(n)


