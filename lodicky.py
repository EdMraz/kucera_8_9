import tkinter, random
w = 700
h = 650
canvas = tkinter.Canvas(width=w, height=h)
canvas.pack()
a = [20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20]
temp = True
def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

def vyrob_lode():
    for i in range(1,16):
        lodicka(a[i],40*i)
    canvas.create_line(w-40,0,w-40,h,width=3,fill="red")

def vyhra(num):
    global temp,color
    temp = False
    canvas.create_text(w//2,h//2,text="Vyhrala lodička číslo:"+str(num),font="Arial 20",fill="black")




def movement():
    global a,m,counter
    if temp == True:
        canvas.delete("all")
        vyrob_lode()
        counter = 0
        for z in range(1,16):
            m = random.randrange(1,11)
            a[z]+=m
            if a[z]>w-40:
                counter += 1
                if counter == 1:
                    vyhra(z)
            print(a)
        canvas.after(100,movement)


def klik(e):
    movement()

vyrob_lode()
canvas.bind("<Button-1>",klik)
canvas.mainloop()
