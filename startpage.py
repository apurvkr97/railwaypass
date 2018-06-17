from tkinter import *
from PIL import ImageTk,Image
import os
import time
import datetime
import aback

xx=datetime.datetime.today().strftime('%Y-%m-%d')
#print(xx)
cy=int(xx[0:4])
cm=int(xx[5:7])
cd=int(xx[-2:])


for eid2 in aback.nonofficeremp():
    #print(eid2[0])
    doa=aback.getdoa(eid2[0])[0][0]
    doay=int(doa[-4:])
    doam=int(doa[3:5])
    doad=int(doa[0:2])
    #print(str(eid2[0])+str(doa))
    yos=cy-doay
    #print(yos)
    if(yos==5):
        yosm=cm-doam
        if (yosm==0):
            yosd=cd-doad
            cc=aback.getcount(eid2[0])[0][0]
            if(yosd>=0) and (cc==1):
                #do
                curr_pp=aback.getpp(eid2[0])[0][0]
                #print(eid2[0])
                new_pp=curr_pp+2
                aback.update_pp(new_pp,eid2[0])
                aback.update_count(eid2[0])
                #print(str(eid2[0])+"  "+"update SUCCESSFUL")
            else:
                pass
        else:
            pass

    else:
        pass



def submit1():
    filename='RAILWAYFRONT.py'
    win.destroy()
    os.system(filename)

def submit2():
    filename='passpage.py'
    win.destroy()
    os.system(filename)
def submit3():
    filename='display.py'
    win.destroy()
    os.system(filename)
def submit4():
    filename='resetpassword.py'
    win.destroy()
    os.system(filename)
def submit5():
    filename='famdatapasswordcheck.py'
    win.destroy()
    os.system(filename)

win = Tk()
win.title('RAILWAY EMPLOYEE & PASS MANAGEMENT SYSTEM ')
win.withdraw()
win.state('zoomed')
#win.resizable(0,0)
img=ImageTk.PhotoImage(Image.open("ser-rnc.jpg"))
imglabel=Label(win,image=img)
imglabel.grid(row=0,column=2,columnspan=4)


lempty1=Label(win,text=" ",width=20)
lempty1.grid(row=2,column=0)
lempty2=Label(win,text=" ",width=20)
lempty2.grid(row=2,column=1)
lempty3=Label(win,text=" ",width=20)
lempty3.grid(row=2,column=2)
lempty4=Label(win,text=" ",width=20)
lempty4.grid(row=2,column=3)
lempty5=Label(win,text=" ",width=20)
lempty5.grid(row=3,column=4)
lempty6=Label(win,text=" ",width=20)
lempty6.grid(row=3,column=5)
lempty7=Label(win,text=" ",width=20)
lempty7.grid(row=4,column=6)




bb1=Button(win,text="INSERT/DELETE/UPDATE/SEARCH EMPLOYEE ",width=50,command=submit1,bg="grey",bd=4,font="Verdana 10 bold")
bb1.grid(row=5,column=3,columnspan=2)
lempty8=Label(win,text=" ",width=20)
lempty8.grid(row=6,column=6)

ba1=Button(win,text="INSERT/DELETE/SEARCH FAMILY DATA ",width=50,command=submit5,bg="grey",bd=4,font="Verdana 10 bold")
ba1.grid(row=7,column=3,columnspan=2)
lempty48=Label(win,text=" ",width=20)
lempty48.grid(row=8,column=6)

bb2=Button(win,text="APPLICATION FOR RAILWAY PASS",width=50,command=submit2,bg="grey",bd=4,font="Verdana 10 bold")
bb2.grid(row=9,column=3,columnspan=2)
lempty9=Label(win,text=" ",width=20)
lempty9.grid(row=10,column=6)

bb3=Button(win,text="VIEW ENTIRE EMPLOYEE DATA",width=50,command=submit3,bg="grey",bd=4,font="Verdana 10 bold")
bb3.grid(row=11,column=3,columnspan=2)
lempty10=Label(win,text=" ",width=20)
lempty10.grid(row=12,column=6)

bb4=Button(win,text="RESET PASSES (at start of new session only)",width=50,command=submit4,bg="grey",bd=4,font="Verdana 10 bold")
bb4.grid(row=13,column=3,columnspan=2)
lempty11=Label(win,text=" ",width=20)
lempty11.grid(row=14,column=6)

lempty12=Label(win,text=" ",width=20)
lempty12.grid(row=15,column=6)

lempty13=Label(win,text=" ",width=20)
lempty13.grid(row=16,column=6)

#lempty14=Label(win,text=" ",width=20,height=3)
#lempty14.grid(row=17,column=6)


lname=Label(win,text="DEVELOPED BY :- ",width=20,font="Verdana 10 bold",fg="red")
lname.grid(row=17,column=5)

lname2=Label(win,text="APURV KUMAR (8051217771)",font="Verdana 10 bold",width=25)
lname2.grid(row=18,column=5)
lname3=Label(win,text="apurv.kr96@gmail.com",font="Verdana 10 bold",width=25)
lname3.grid(row=19,column=5)



lname12=Label(win,text="UNDER GUIDANCE:- ",width=20,font="Verdana 10 bold",fg="red")
lname12.grid(row=17,column=1)
lname13=Label(win,text="S.SRINIVAS(DPO) ",width=20,font="Verdana 10 bold")
lname13.grid(row=18,column=1)
lname14=Label(win,text="DR.RISHAV SINHA(APO) ",width=20,font="Verdana 10 bold")
lname14.grid(row=19,column=1)
lname=Label(win,text="MD.IBRAR(APO)",width=20,font="Verdana 10 bold")
lname.grid(row=20,column=1)

win.mainloop()
