import tkinter, random
w=700
h=800
canvas = tkinter.Canvas(width=700, height=800)
canvas.pack()

def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

def plocha():
    for i in range(1,16):
        lodicka(x,y*i)
    canvas.create_line(w-50,0,w-50,h,width=3,fill="red")
#
# def starter(e):
#     movement()
#
# def movement():

x= 20
y= 50
#canvas.bind("<Button-1>",starter)
plocha()
canvas.mainloop()
