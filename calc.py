from tkinter import *

siv=Tk()
siv.geometry("500x500")

e1=Entry(siv,width=56,borderwidth=5)
e1.place(x=0,y=0)
def click(n):
    res=e1.get()
    e1.delete(0,END)
    e1.insert(1,str(res)+str(n))

# buttons
b=Button(siv,text='1',width=12,command=lambda:click(1))
b.place(x=10,y=60)
b1=Button(siv,text='2',width=12,command=lambda:click(2))
b1.place(x=80,y=60)
b2=Button(siv,text='3',width=12,command=lambda:click(3))
b2.place(x=170,y=60)

b3=Button(siv,text='4',width=12,command=lambda:click(4))
b3.place(x=10,y=120)
b4=Button(siv,text='5',width=12,command=lambda:click(5))
b4.place(x=80,y=120)
b5=Button(siv,text='6',width=12,command=lambda:click(6))
b5.place(x=170,y=120)

b3=Button(siv,text='7',width=12,command=lambda:click(7))
b3.place(x=10,y=180)
b4=Button(siv,text='8',width=12,command=lambda:click(8))
b4.place(x=80,y=180)
b5=Button(siv,text='9',width=12,command=lambda:click(9))
b5.place(x=170,y=180)

b5=Button(siv,text='0',width=12,command=lambda:click(0))
b5.place(x=10,y=240)

#operations
def add():
    global math
    math = "addition"
    n1=e1.get()
    global i
    i=int(n1)
    e1.delete(0,END)
def sub():
    global math
    math = "subtraction"
    n1=e1.get()
    global i
    i=int(n1)
    e1.delete(0,END)
def mul():
    global math
    math = "multiplication"
    n1=e1.get()
    global i
    i=int(n1)
    e1.delete(0,END)
def div():
    global math
    math = "division"
    n1=e1.get()
    global i
    i=int(n1)
    e1.delete(0,END)
b5=Button(siv,text='+',width=12,command=add)
b5.place(x=80,y=240)

b5=Button(siv,text='-',width=12,command=sub)
b5.place(x=170,y=240)
b5=Button(siv,text='*',width=12,command=mul)
b5.place(x=10,y=300)

b5=Button(siv,text='/',width=12,command=div)
b5.place(x=80,y=300)
def equal():
    n2=e1.get()
    e1.delete(0,END)
    if math=='addition':
        e1.insert(0,i+int(n2))
    elif math=='subtraction':
        e1.insert(0,i-int(n2))
    elif math == 'multiplication':
        e1.insert(0, i * int(n2))
    elif math == 'division':
        e1.insert(0, i / int(n2))
def clr():
    e1.delete(0,END)
b5=Button(siv,text='=',width=12 ,command=equal)
b5.place(x=170,y=300)

b5=Button(siv,text='clear',width=12,command=clr)
b5.place(x=80,y=350)
mainloop()