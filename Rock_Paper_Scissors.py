import tkinter as t
from tkinter import messagebox
import tkinter.font as font
import random
from PIL import Image, ImageTk
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        messagebox.showinfo("Info","It's a tie!!")
        return "None has won!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        global user_score
        user_score += 1
        return "So You win!"
    else:
        global computer_score
        computer_score += 1
        return "Computer wins!"
def play(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}",bg="light blue")
    score_label.config(text=f"Score -\n You: {user_score}\n Computer: {computer_score}")
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="Score - You: 0 Computer: 0")
def show_message():
    top = t.Toplevel(app)
    top.title("Info")
    path = r'C:\Bhavya Gada\rock-paper-scissors.png'
    image = Image.open(path)
    img = ImageTk.PhotoImage(image)
    label = t.Label(top, image=img).pack()
    message = t.Label(top, text="All the best!!")
    message.pack(pady=10)
    button = t.Button(top, text="OK", command=top.destroy)
    button.pack(pady=10)
    top.image = img
app = t.Tk()
app.title("Rock-Paper-Scissors")
app.geometry("500x500")
app.iconbitmap(r'C:\Users\Bhavya Gada\Pictures\rock-paper-scissors.ico.bmp')
app.after(100, show_message)

custom_font = font.Font(family="Helvetica", size=14, weight="bold", underline=True)
user_score = 0
computer_score = 0
instruction_label = t.Label(app, text="Choose rock, paper, or scissors:")
instruction_label.pack()

rock_button = t.Button(app, text="Rock", command=lambda: play("rock"))
rock_button.pack(side=t.LEFT, padx=20)

paper_button = t.Button(app, text="Paper", command=lambda: play("paper"))
paper_button.pack(side=t.LEFT, padx=20)

scissors_button = t.Button(app, text="Scissors", command=lambda: play("scissors"))
scissors_button.pack(side=t.LEFT, padx=20)

result_label = t.Label(app, text="",font=custom_font)
result_label.pack(pady=20)

score_label = t.Label(app, text="Score - You: 0 Computer: 0",font=custom_font)
score_label.pack(pady=20)

reset_button = t.Button(app, text="Reset Game", command=reset_game)
reset_button.pack(pady=20)
app.mainloop()