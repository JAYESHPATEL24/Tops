# Write a Python function to calculate the factorial of a number (a nonnegative integer) 

    # function for find factorial of given number
def factorial(n):
        # Check if the input is a nonnegative integer
    if n < 0:
        return "We can not find Factorial for negative numbers."
    elif n == 0:
        return 1
    else:
            # calculate the factorial of a number.
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    # user input
n = int(input("Enter a integer: "))

print(f"The factorial of {n} is {factorial(n)}")
