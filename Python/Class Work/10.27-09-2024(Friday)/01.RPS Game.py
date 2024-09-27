import random

l = ["r","p","s"]


sum =0

print("*"*20,"Welcome to the game","*"*20)

for i in range(1,5):

    cc = random.choice(l) 
    
    menu = """
        press r for Rock
        press p for Paper
        pree s for Scissors
    """
    
    print(menu)
    
    uc = input("Enter choice : ").lower()
    
    if uc == "r" or uc == "p" or uc == "s":
        
        print(f"Computer Choice : {cc}")
        print(f"User Choice : {uc}")
        
        if uc == cc:
            print("Its Tie !!!!")
            
        elif cc == "r" :
            if uc == "p":
                print("User Win!!!!")
                sum += 100
            else:
                print("Computer Win!!")
                
            
        elif cc == "p":
            if uc == "s":
                print("User Win!!!!")
                sum += 100
            else:
                print("Computer Win!!")
                
        elif cc == "s":
            if uc == "r":
                print("User Win!!!!")
                sum += 100
            else:
                print("Computer Win!!")
    
    else:
        print("XXX Invaid Choice!!!")
        break
    
print(f"Your Score : {sum}")

if sum >= 300 :
    print("Excellent !!!!!")
    
elif sum>0:
    print("Good !!!!")
    
else:
    print("Better Luck Next time !!!")