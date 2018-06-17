from tkinter import *
from PIL import ImageTk,Image
import os
import time
import aback
global ppass
global mmid


def get_selected_row(event):
    global selected_tuple
    index=list2.curselection()[0]
    #print(index)
    selected_tuple=list2.get(index)
    print(selected_tuple)
    mmid=selected_tuple[0]
    memid.set("")
    rel.set("")
    rel.set(selected_tuple[2])
    e7.delete(0,END)
    e7.insert(END,selected_tuple[3])
    e8.delete(0,END)
    e8.insert(END,selected_tuple[4])
    eA1.delete(0,END)
    eA1.insert(END,selected_tuple[5])
    #print(mmid)
    memid.set(mmid)


def addfam_data():

    if emp_id.get()=="" or f1name.get()=="" or f1dob.get()=="" or fam_ad.get()=="":
        msg="ENTRIES cannot be NULL"
        list2.delete(0,END)
        list2.insert(END,msg)
    else:
        xyz=aback.checkid(int(emp_id.get()))
        #print(xyz)
        if type(xyz)==int:
            list2.delete(0,END)
            list2.insert(END,"No such employee id exists")
        else:
            list2.delete(0,END)
            aback.insert_value2(emp_id.get(),variable6.get(),f1name.get(),f1dob.get(),fam_ad.get())
            list2.insert(END,"MEMBER ADDED SUCCESSFULLY")
            e7.delete(0,END)
            e8.delete(0,END)
            eA1.delete(0,END)



def dispfam_data():
        if emp_id.get()=="":
            msg="Employee id cannot be NULL"
            list2.delete(0,END)
            list2.insert(END,msg)
        else:
            xyz=aback.checkid(int(emp_id.get()))
            #print(xyz)
            if type(xyz)==int:
                list2.delete(0,END)
                list2.insert(END,"No such employee id exists")
            else:
                list2.delete(0,END)
                for i in aback.viewfam(emp_id.get()):
                        list2.insert(END,i)


def delmem():
    mmid=memid.get()
    if (len(mmid)==0):
        list2.delete(0,END)
        list2.insert(END,"PLEASE SEARCH AND SELECT A MEMBER FROM LIST")
    else:
        aback.delete_mem(int(mmid))
        list2.delete(0,END)
        list2.insert(END,"MEMBER DELETED SUCCESSFULLY")


def changepass():
    filename='famdatapasswordchange.py'
    win.destroy()
    os.system(filename)


def bback1():
    filename='startpage.py'
    win.destroy()
    os.system(filename)

OPTIONS6 = ["SPOUSE","SON","DAUGHTER","DEPENDENT FATHER","DEPENDENT MOTHER"]

win = Tk()
win.title('RAILWAY PASS MANAGEMENT SYSTEM ')
win.state('zoomed')
#win.resizable(0,0)
img=ImageTk.PhotoImage(Image.open("ser.jpg"))
imglabel=Label(win,image=img)
imglabel.grid(row=0,column=3,columnspan=4)


l1=Label(win,text="EMPLOYEE ID",width=20)
l1.grid(row=1,column=1)
emp_id=StringVar()
e1=Entry(win,width=20,textvariable=emp_id,relief='solid')
e1.grid(row=1,column=3)

lempty67=Label(win,text=" ",width=20)
lempty67.grid(row=2,column=2)

l11=Label(win,text="RELATIONSHIP",width=20)
l11.grid(row=3,column=1)
l12=Label(win,text="NAME",width=20)
l12.grid(row=5,column=1)
l13=Label(win,text="DOB",width=20)
l13.grid(row=9,column=1)


lA1=Label(win,text="AADHAR NO:",width=20)
lA1.grid(row=7,column=1)
fam_ad=StringVar()
eA1=Entry(win,width=20,textvariable=fam_ad,relief='solid')
eA1.grid(row=7,column=3)

lempty2=Label(win,text=" ",width=20)
lempty2.grid(row=4,column=4)
lempty3=Label(win,text=" ",width=20)
lempty3.grid(row=6,column=2)
lempty=Label(win,text=" ",width=20)
lempty.grid(row=8,column=2)
#####family member
variable6 = StringVar()
variable6.set(OPTIONS6[0]) # default value
f1relation= OptionMenu(win, variable6, *OPTIONS6)
f1relation.grid(row=3,column=3)
rel=StringVar()
lx11=Label(win,textvariable=rel,width=20)
lx11.grid(row=3,column=4)



f1name=StringVar()
e7=Entry(win,width=20,textvariable=f1name,relief='solid')
e7.grid(row=5,column=3)
f1dob=StringVar()
e8=Entry(win,width=20,textvariable=f1dob,relief='solid')
e8.grid(row=9,column=3)
######################################################
bt1=Button(win,text="ADD MEMBER",width=20,command=addfam_data,bg="grey",bd=4,font="Verdana 10 bold")
bt1.grid(row=11,column=1)
lmm=Label(win,text="MEMBER id:",width=20)
lmm.grid(row=11,column=3)
memid=StringVar()
l17=Label(win,textvariable=memid,width=10)
l17.grid(row=11,column=4,sticky='w')

lempty4=Label(win,text=" ",width=20)
lempty4.grid(row=10,column=0)

lempty9=Label(win,text=" ",width=20)
lempty9.grid(row=12,column=0)

b6=Button(win,text="DISPLAY ALL FAMILY MEMBER",width=30,command=dispfam_data,bg="grey",bd=4,font="Verdana 10 bold")
b6.grid(row=13,column=0,columnspan=2)

lempty5=Label(win,text=" ",width=20)
lempty5.grid(row=14,column=2)
b7=Button(win,text="DELETE-MEMBER",width=20,command=delmem,bg="grey",bd=4,font="Verdana 10 bold")
b7.grid(row=13,column=2)


famlebel=Label(win,text="FAMILY DETAILS",font="Verdana 10 bold")
famlebel.grid(row=1,column=5,columnspan=5)
list2=Listbox(win,width=70,height=27)
list2.grid(row=3,column=5,rowspan=13,columnspan=5)
list2.bind("<<ListboxSelect>>",get_selected_row)

lempty53=Label(win,text=" ",width=20)
lempty53.grid(row=16,column=2)

b75=Button(win,text="CHANGE PASSWORD",width=20,command=changepass,bg="red",bd=4,font="Verdana 10 bold")
b75.grid(row=15,column=1)


bback=Button(win,text="Back",width=8,command=bback1,bg="brown",bd=4,font="Verdana 10 bold")
bback.grid(row=15,column=3)

win.mainloop()
