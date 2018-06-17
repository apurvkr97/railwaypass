from tkinter import *
import os
import aback


def onokclick():
    PASSWORD = pwdbox.get()
    if PASSWORD=="som3536" or PASSWORD=="python1234" or PASSWORD=="ser-hte18":
        filename='startpage.py'
        root.destroy()
        os.system(filename)
    else:
        pwdbox.delete(0,END)

def onpwdentry(evt):
    PASSWORD = pwdbox.get()
    if PASSWORD=="som3536" or PASSWORD=="python1234" or PASSWORD=="ser-hte18":
        filename='startpage.py'
        root.destroy()
        os.system(filename)
    else:
        pwdbox.delete(0,END)

root = Tk()
pwdbox = Entry(root, show = '*')

Label(root, text = '                                          ').pack(side = 'left')
Label(root, text = '                                          ').pack(side = 'right')
Label(root, text = '                                          ').pack(side = 'top')
Label(root, text = 'Login Password').pack(side = 'top')

pwdbox.pack(side = 'top')
pwdbox.bind('<Return>', onpwdentry)

Button(root, command=onokclick, text = 'OK').pack(side = 'top')

Label(root, text = '                                          ').pack(side = 'bottom')
root.mainloop()
