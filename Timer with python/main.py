from tkinter import *
import time

root = Tk()
root.configure(bg = "white")

label1 = Label(root,font = 'Arial 50', bg = "white")
label1.pack()

def get_time():
    current_time = time.strftime("%H:%M:%S %p")
    label1.configure(text=current_time)
    label1.after(200,get_time)

get_time()
root.mainloop()
