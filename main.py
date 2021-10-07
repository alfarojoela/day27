import tkinter
from tkinter import *
import playground

def button_clicked():
    print("I got clicked.")
    #my_label["text"] = "I got clicked."
    my_label["text"] = input.get()

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()  #this is a method that puts the above on the window.  The Packer has optional arguments such as
#my_label.pack(side="left") or my_label.pack(expand =1)

#more docs at https://tcl.tk/man/tcl8.6/TkCmd/pack.htm#M21

#can change value of text by :
my_label["text"] = "New Text"

#alternative way:
my_label.config(text="New Text")

#button
button = tkinter.Button(text="Click Me", command=button_clicked)  #name of function set to command.  triggers function
button.pack()

#ADVANCED PYTHON ARGUMENTS
##########
#def my_function(a=1, b=2, c=3):
#    print(a)
#    print(b)
#    print(c)

#above has default values in definition.
#my_function(b=5)
#above changes value of b.

#can have cursor hover to get more info on parameters.
##########

playground.add(1, 2, 3, 4, 5)

playground.calculate(2, add=3, multiply=5)

input = Entry(width=10)
input.pack()
print(input.get())

















#line of code keeps window on screen.
window.mainloop()