import tkinter as tk
from tkinter import messagebox
import random

USER_WINS = 0
COMPUTER_WINS = 0
TIES = 0

def update_score():
    score_label.config(text=f"YOUR WINS: {USER_WINS}\n COMPUTER WINS: {COMPUTER_WINS}\n TIES: {TIES}")

def play_game(user_choice):
    global USER_WINS, COMPUTER_WINS, TIES

    random_number = random.random()
    
    if random_number >= 0 and random_number < 1 / 3:
        computer_move = 'rock'
    elif random_number >= 1 / 3 and random_number < 2 / 3:
        computer_move = 'paper'
    else:
        computer_move = 'scissors'
    
    if user_choice == 'rock':
        if computer_move == 'rock':
            result = 'Tie.'
            TIES += 1
        elif computer_move == 'paper':
            result = 'You lose.'
            COMPUTER_WINS += 1
        else:
            result = 'You win.'
            USER_WINS += 1
    
    elif user_choice == 'paper':
        if computer_move == 'rock':
            result = 'You win.'
            USER_WINS += 1
        elif computer_move == 'paper':
            result = 'Tie.'
            TIES  += 1
        else:
            result = 'You lose.'
            COMPUTER_WINS += 1
    
    elif user_choice == 'scissors':
        if computer_move == 'rock':
            result = 'You lose.'
            COMPUTER_WINS += 1
        elif computer_move == 'paper':
            result = 'You win.'
            USER_WINS += 1
        else:
            result = 'Tie.'
            TIES += 1
    
    messagebox.showinfo("Game Result", f"You picked {user_choice}. Computer picked {computer_move}. {result}")

    update_score()

def quit_game():
    root.quit()

root = tk.Tk()
root.title("Rock, Paper, Scissors")

root.geometry("400x350")
root.resizable(False, False)

rock_button = tk.Button(root, text="\U0000274A Rock",font=("Arial",18), width=20, command=lambda: play_game('rock'))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="\U0000270B Paper",font=("Arial",18),width=20, command=lambda: play_game('paper'))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="\U0000270C Scissors",font=("Arial",18),width=20, command=lambda: play_game('scissors'))
scissors_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit",font=("Arial",14),width=20, command=quit_game)
quit_button.pack(pady=10)

score_label = tk.Label(root, text="YOUR WINS: 0\nCOMPUTER WINS: 0\nTIES: 0",font=("Arial",6))
score_label.pack(pady=20)

root.mainloop()
