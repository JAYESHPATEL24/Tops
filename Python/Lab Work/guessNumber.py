import random

n = random.randint(1,10)
guess = 0

while guess != n:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess>10 or guess<1:
        print("XXXX invaild Number.")
    elif n>guess:
        print("Small Number.")
        
    elif n<guess:
        print("Large number.")
        
    else:
        print("YOU WIN !!!! \U0001F607 \U0001F607 \U0001F607")