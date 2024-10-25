import random

Robot = random.choice(["rock", "paper", "scissors"])

my_choice = input("Enter rock, paper, or scissors: ").lower()

if my_choice == Robot:
    print(f"Both chose {my_choice}. It's a tie! \U0001F601")

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
