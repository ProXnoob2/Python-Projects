from operator import rshift
import time
from tkinter import *
from tkinter.ttk import *

sc=0; mn=0; hr=0; stp=0; rst=0

def start():
    global sc,mn,hr
    sc=sc+1
    if(sc==60):
        mn=mn+1
        sc=0
    if(mn==60):
        hr=hr+1
        mn=0
    if(stp==0):
        lbl=Label(root,text='%i:%i:%i'%(hr,mn,sc),font=('arial',30,'bold'),
        foreground='green',background="black",width=10)
        lbl.after(1000,start)
        lbl.place(x=70,y=60)

def stop():
    global stp
    stp=1

root=Tk(); style=Style()
root.title("Stopwatch")
root.geometry("250x200")
root.resizable(False,False)
root.configure(bg="black")

style.configure('TButton',font=('arial',10,'bold'),borderwidth='5')

button1=Button(root,text="Start",command=start).place(x=10,y=10)
button2=Button(root,text="Stop",command=stop).place(x=150,y=10)

root.mainloop()