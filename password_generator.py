#Password Generator Application
import random     #   1.random.shuffle   2. random.choice  3. random.sample
import tkinter
from tkinter.ttk import *
from tkinter import messagebox, END
import string as s
import pyperclip
root = tkinter.Tk()
root.title("Password Generator Application")
root.geometry("500x800")
l1 = Label(root, text="Password Length:").grid(row=0,column=0)
length = Entry(root)
length.grid(row=0,column=2)
l2 = Label(root, text="How many letters do u want?").grid(row=1,column=0)
letters = Entry(root)
letters.grid(row=1,column=2)
l3 = Label(root, text="Your password:").grid(row=2,column=0)
entry = Entry(root)
entry.grid(row=2,column=2)
def PasswordGenerator():
    try:
        password_length = int(length.get())
        letter = int(letters.get())
        password = ''
        error = "Wrong input"
        for i in range(letter):
            password = password + random.choice(s.ascii_letters)
            
        for x in range(password_length-letter):
            password += random.choice(s.digits)
        password = ''.join(random.sample(password, len(password)))
        entry.delete(0, END)
        entry.insert(0, password)
        if letter > password_length:
            entry.delete(0, END)

            entry.insert(0, error)
    except ValueError:
        messagebox.showerror("Error","Please enter integer values")
        
def Clear():
    length.delete(0, END)
    letters.delete(0, END)
    entry.delete(0, END)
def Copy():
    password = str(entry.get())
    pyperclip.copy(password)
    messagebox.showinfo("Info","Password copied successfully!")
def Change():
    password = str(entry.get())
    char_list = list(password)
    random.shuffle(char_list)
    new_password  = ''.join(char_list)
    entry.delete(0, END)
    entry.insert(0, new_password)
button = Button(root, command=PasswordGenerator, text="Generate Password")
button.grid(row=6,column=0)
button2 = Button(root, text="Clear all", command=Clear)
button2.grid(row=6,column=1)
button3 = Button(root,text="Copy Password",command=Copy)
button3.grid(row=6,column=2)
button4 = Button(root, text="Shuffle Password",command=Change)
button4.grid(row=6,column=3)

root.mainloop()
