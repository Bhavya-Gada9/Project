from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Python Calculator")
root.geometry("500x550")

Label(root, text="Enter first number:").grid(row=0, column=0)
f = Entry(root, width=20)
f.grid(row=0, column=1)

Label(root, text="Enter second number:").grid(row=1, column=0)
s = Entry(root, width=20)
s.grid(row=1, column=1)

Label(root, text="Select operation to perform:").grid(row=2, column=0)
operation = StringVar()
operation.set(None)
r1=Radiobutton(root, text="Addition", variable=operation, value="Addition").grid(row=2, column=1)
r2=Radiobutton(root, text="Subtraction", variable=operation, value="Subtraction").grid(row=3, column=1)
r3=Radiobutton(root, text="Multiply", variable=operation, value="Multiply").grid(row=4, column=1)
r4=Radiobutton(root, text="Divide", variable=operation, value="Divide").grid(row=5, column=1)
r5=Radiobutton(root, text="Modulus", variable=operation, value="Modulus").grid(row=6, column=1)
Label(root, text="Result:").grid(row=8, column=0)
r = Entry(root, width=20)
r.grid(row=8, column=1)
def calculate():
    num1 = float(f.get())
    num2 = float(s.get())
    operations = operation.get()
    
    if operations == "Addition":
        result = num1 + num2
    elif operations == "Subtraction":
        result = num1 - num2
    elif operations == "Multiply":
        result = num1 * num2
    elif operations == "Divide":
        if num2 != 0:  
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Cannot divide by zero")
            return
    elif operations == "Modulus":
        if num2 != 0:  
            result = num1 % num2
        else:
            messagebox.showerror("Error", "Cannot perform modulus by zero")
            return
    r.delete(0, END)
    r.insert(0, result)
def Clear():
    f.delete(0,END)
    s.delete(0,END)
    r.delete(0,END)
    operation.set(None)
    messagebox.showinfo("Message","Deleted successfully!")
b1=Button(root, text="Calculate", command=calculate,bg="blue", fg="white")
b1.grid(row=12, columnspan=2)
Button(root,text="Clear All",command=Clear,bg="blue", fg="white").grid(row=12,column=1)
root.mainloop()
