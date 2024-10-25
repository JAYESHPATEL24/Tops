import game

menu = """
        Select one game 
        1.Coin Toss
        2.Guess a Number
        3.Rock, Paper, Scissors
        4.Exit
       """
       
while True:
    
    print(menu)
    
    ch = int(input("Enter your Choice : "))
    
    if ch == 1:
        print("YOU SELECTED COIN TOSS......!!! \U0001F60A \U0001F60A \U0001F60A")
        game.coin_toss()
        
    elif ch == 2:
        print("YOU SELECTED GUESS GAME......!!! \U0001F60A \U0001F60A \U0001F60A")
        game.guess_number()
        
    elif ch == 3:
        print("YOU SELECTED ROCK PAPER SCISSORS......!!! \U0001F60A \U0001F60A \U0001F60A")
        game.rock_paper_scissors()
        
    elif ch == 4:
        print("I Hope you Enjoy the Games........ \U0001F607 \U0001F607 \U0001F607")
        break
    
    else:
        print("XXXX invalid Choice....")
        print("Please Enter right choice...\U0001F64F\U0001F64F")
        
