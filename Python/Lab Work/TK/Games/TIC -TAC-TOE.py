from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
y = (root.winfo_screenwidth()//2) - (720//2)
x = (root.winfo_screenheight()//2) - (750//2)
root.geometry(f"720x750+{x+350}+{y-y+10}")

def clickbutton(ind):
    global player
    if board[ind] == "" and not Winner():
        board[ind] = player
        buttons[ind].config(text=player)
        if Winner():
            messagebox.showinfo("Winner", f"Player {player} Wins!")
            reset_board()
        elif "" not in board:
            messagebox.showinfo("Winner", "It's a Tie!")
            reset_board()
        else:
            player = "X" if player == "O" else "O"

def Winner():
    win = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]] != "":
            buttons[i[0]].config(bg="darkblue") 
            buttons[i[1]].config(bg="darkblue") 
            buttons[i[2]].config(bg="darkblue")
            return True
    return False

def reset_board(): 
    global board, player, buttons
    board = [""] * 9 
    for i in buttons: 
        i.config(text="",bg="black") 
    player = "O"


player = "O"
board = [""] * 9
buttons = []

for i in range(9):
    button = Button(root, font=("Arial", 30), width=10, height=4,fg = "white", bg = "black", command=lambda i=i: clickbutton(i),relief=GROOVE)
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

reset_button = Button(root, text="RESET", font=("Arial", 30), width=8, height=1, bg ="lightblue", command=reset_board)
reset_button.place(x=140, y=660)

exit_game = Button(root, text="Exit", font=("Arial", 30), width=8, height=1, bg="orange", command=root.destroy)
exit_game.place(x=390, y=660)


root.mainloop()
