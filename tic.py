from tkinter import *
import random


def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        buttons[row][column]["text"] = player
        if check_winner() is False:
            player = players[(players.index(player) + 1) % 2]
            label.config(text=(player + " Turn"))
        elif check_winner() is True:
            label.config(text=(player + " Wins"))
        elif check_winner() == "Tie":
            label.config(text="Tie!")




def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
            
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    
    else:
        return False



def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True
            
        
def new_game():
    global player
    player = random.choice(players)
    label.config(text = player + " Turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="white")

window = Tk()
window.title("Tic Tac Toe")
window.config(bg="grey")
window.geometry("1000x700")
window.resizable(False, False)

players =["X", "O"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

top_frame = Frame(window, bg="#5D6D7E", width=1000, height=250)
top_frame.place(x=0, y=0)


game_title = Label(top_frame, bg="#5D6D7E", fg="white", text="Tic-Tac-Toe", font=("", 48))

game_title.place(x=320, y=0)


label = Label(top_frame, text=player + " Turn", font=("arial", 30), bg="#5D6D7E", fg="white")
label.place(x=440, y=200)


reset_button = Button(top_frame, text="Restart Game", font=("arial", 30), bg="gray", fg="green", command=new_game)
reset_button.place(x=360, y=95)


bottom_frame = Frame(window, bg="white", width=400, height=400)
bottom_frame.place(x=265, y =300)


for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(bottom_frame, text="", font=("arial", 40), width=5, height=1, command=lambda row=row, column=column: next_turn(row, column))

        buttons[row][column].grid(row=row, column=column)

window.mainloop()