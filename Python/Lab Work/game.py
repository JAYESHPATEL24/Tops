import random

def guess_number():
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
            
def rock_paper_scissors():
    Robot = random.choice(["rock", "paper", "scissors"])

    my_choice = input("Enter rock, paper, or scissors: ").lower()

    if my_choice == Robot:
        print(f"Both choose {my_choice}. It's a tie! \U0001F601")

    elif my_choice == "rock":
        if Robot == "paper":
            print("Paper covers rock! You lose. \U0001FAE1")
        else:
            print("Rock smashes scissors! You win. \U0001F607")

    elif my_choice == "paper":
        if Robot == "rock":
            print("Paper covers rock! You win. \U0001F607")
        else:
            print("Scissors cuts paper! You lose. \U0001FAE1")

    elif my_choice == "scissors":
        if Robot == "rock":
            print("Rock smashes scissors! You lose. \U0001FAE1")
        else:
            print("Scissors cuts paper! You win. \U0001F607")

    else:
        print("Please enter a valid choice. \U0001F624")

        
def coin_toss():
    result = random.choice(["Heads", "Tails"])
    guess = input("Guess Heads or Tails: ").capitalize()

    if guess == "Heads" or  guess == "Tails":
        if guess == result:
            print(f"Correct! It was {result}. \U0001F607")
        else:
            print(f"Wrong! It was {result}.\U0001FAE1")
    else:
        print("xxx invaild input. \U0001F624")