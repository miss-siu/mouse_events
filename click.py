from tkinter import *
from random import *
import time, threading
class Game:
    def __init__(self):
        root = Tk()

        self.canvas = Canvas(root, width=500, height=500)
        self.canvas.pack()
        self.score = 0
        self.ovals = {}

        for i in range(100):
            num = randint(0,100)
            mod = 1 if num%2==0 else -1
            num = randint(0,100)
            mod2 = 1 if num%2==0 else -1

            x, y = randint(0, 500-1), randint(0, 500-1)
            oval = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="red")
            self.ovals[oval] = (random()*mod,random()*mod2);
            self.canvas.itemconfig(oval, tags=("oval",))

        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<Button-3>", self.move)
        root.mainloop()

    def click(self, event):
        if self.canvas.find_withtag(CURRENT):
            self.canvas.itemconfig(CURRENT, fill="blue")
            self.canvas.update_idletasks()
            self.canvas.after(20)
            pos = self.canvas.coords(CURRENT)
            self.score = self.score+int((10/abs(pos[0]-pos[2])*100))
            self.canvas.delete(CURRENT)
            print (self.score)
        else:
            self.score = self.score - 100
            print(self.score)
    def move(self, event):
        t = threading.Thread(target=self.start)
        t.start()
    def start(self):
        while True:
            self.canvas.update_idletasks()
            self.canvas.after(5)
            for i in self.canvas.find_withtag("oval"):
                
                num = randint(0,100)
                mod = 1 if num%2==0 else -1
                num = randint(0,100)
                mod2 = 1 if num%2==0 else -1
                
                pos = self.canvas.coords(i)
                try:
                    self.canvas.coords(i, pos[0], pos[1], pos[2]+mod2, pos[3]+mod2)
                except:
                    continue
                x = self.ovals.get(i)[0]
                y = self.ovals.get(i)[1]
                try:
                    pos = self.canvas.coords(i)
                    if pos[0] > 490 or pos[0] < 10:
                        x = x*-1
                    if pos[1] > 490 or pos[1] < 10:
                        y = y*-1
                    self.ovals[i] = (x, y)
               
                
                    self.canvas.coords(i, pos[0]+x, pos[1]+y, pos[2]+x, pos[3]+y)
                except:
                    continue
            
Game()            
                
    
