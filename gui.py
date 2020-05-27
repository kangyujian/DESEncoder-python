#_*_ coding:utf-8 _*_
from Tkinter import *

import dedes
import des

root =Tk()
root.title('DES Encoder and Decoder')
root.geometry('300x350')
Label(root, text='Info:').grid(row=0, column=0)
Label(root, text='Key:').grid(row=1, column=0)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


text1 = Text(root, width=30, height=2)
text1.grid(row=3, column=1)

def encoder():
    res=des.desencode(e1.get(),e2.get())
    text1.insert(INSERT,res)

Button(root, text='Encode', width=20,command=encoder).grid(row=2, column=1, sticky=W, padx=10, pady=5)



e3 = Entry(root)
e4 = Entry(root)

e3.grid(row=4, column=1, padx=10, pady=5)
e4.grid(row=5, column=1, padx=10, pady=5)

Label(root, text='Info:').grid(row=4, column=0)
Label(root, text='Key:').grid(row=5, column=0)
e3.grid(row=4, column=1, padx=10, pady=5)
e4.grid(row=5, column=1, padx=10, pady=5)



text2 = Text(root, width=30, height=2)
text2.grid(row=7, column=1)

def decoder():
    res=dedes.desdecode(e3.get(),e4.get())
    text2.insert(INSERT,res)

Button(root, text='Encode', width=20, command=decoder).grid(row=6, column=1, sticky=W, padx=10, pady=5)

mainloop()
