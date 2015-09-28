from tkinter import *
from random import randint
import time, threading

root = Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()

def click(event):
    if canvas.find_withtag(CURRENT):
        canvas.itemconfig(CURRENT, fill="blue")
        canvas.update_idletasks()
        canvas.after(200)
        canvas.delete(CURRENT)
def move(event):
    t = threading.Thread(target=start)
    t.start()
def start():
    while True:
        time.sleep(0.05)
        for i in canvas.find_withtag("oval"):
            
            num = randint(0,100)
            mod = 1 if num%2==0 else -1
            pos = canvas.coords(i)
            try:
                canvas.coords(i, pos[0]+mod, pos[1]+mod, pos[2]+mod, pos[3]+mod)
            except:
                continue

for i in range(100):
    x, y = randint(0, 500-1), randint(0, 500-1)
    oval = canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")
    canvas.itemconfig(oval, tags=("oval",))

canvas.bind("<Button-1>", click)
canvas.bind("<Button-3>", move)

root.mainloop()
