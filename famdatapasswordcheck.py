from tkinter import *
import os
import aback


paswd=aback.getpwd()
print(paswd)

def bback1():
    filename='startpage.py'
    root.destroy()
    os.system(filename)

def onokclick():
    PASSWORD = pwdbox.get()
    if PASSWORD==paswd:
        filename='familydet.py'
        root.destroy()
        os.system(filename)
    else:
        pwdbox.delete(0,END)

def onpwdentry(evt):
    PASSWORD = pwdbox.get()
    if PASSWORD==paswd:
        filename='familydet.py'
        root.destroy()
        os.system(filename)
    else:
        pwdbox.delete(0,END)

root = Tk()
Label(root, text = '                                          ').pack(side = 'left')
Label(root, text = '                                          ').pack(side = 'right')
Label(root, text = '                                          ').pack(side = 'top')

pwdbox = Entry(root, show = '*')

Label(root, text = 'Password').pack(side = 'top')

pwdbox.pack(side = 'top')
pwdbox.bind('<Return>', onpwdentry)
Button(root, command=onokclick, text = 'OK').pack(side = 'top')
Button(root, command=bback1, text = 'Back').pack(side = 'top')
root.mainloop()
