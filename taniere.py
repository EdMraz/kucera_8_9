import tkinter
import random

def setup(x,y):
    for i in range(1,11):
        canvas.create_oval(x*i-30,y-30,x*i+30,y+30,width=3,fill="blue",tag=i)
        canvas.create_oval(x*i-20,y-20,x*i+20,y+20,tag=i)
        canvas.create_text(x*i,y,text=abc[i-1],font="Arial 20",fill="white",tag=i)

def vyhra():
    canvas.delete('all')
    canvas.create_text(w//2,h//2,text="Gratulujem, označil si puknutý tanier!",font="Arial 20",fill="blue")


def viackrat():
    canvas.create_text(w//2,h//2+30,text="Viackrát si klikol na taniere:",font="Arial 20",fill="red")


def check(e):
    poradie = int(canvas.gettags("current")[0])
    if poradie == puknuty_tanier:
        vyhra()
        viackrat()

puknuty_tanier = random.randrange(1,11)
print(puknuty_tanier)
w = 780
h = 100
size = 50


abc = ["A","B","C","D","E","F","G","H","I","J"]

root = tkinter.Tk()
canvas = tkinter.Canvas(root,width=w,height=h,bg="white")
canvas.pack()
canvas.bind("<Button-1>",check)
setup(70,50)

root.mainloop()
