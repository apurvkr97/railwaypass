from tkinter import *
from PIL import ImageTk,Image
import os
import time
import datetime
import aback



def cchh():
    for cfb in aback.return_pbal():
        aback.insert_value5(cfb[0],cfb[1],cfb[2],cfb[3])




def cnf():
        for cfb in aback.return_pbal():
            #print(cfb)
            res=aback.checkcfid(int(cfb[0]))
            print(type(res))
            if type(res)==int:
                print("insert hua hai")
                aback.insert_value5(cfb[0],cfb[1],cfb[2],cfb[3])
            else:
                print("ni hua insert")
                aback.update_cfpbal(cfb[2],cfb[3],cfb[0])

        for eid in aback.officeremp():
            #print(eid[0])
            aback.update_pp(6.0,eid[0])
            aback.update_pto(4.0,eid[0])
        for eid2 in aback.nonofficeremp():
            #print(eid2[0])
            doa=aback.getdoa(eid2[0])[0][0]
            doay=doa[-4:]
            cy=aback.current_year
            #print(doa)
            yos=cy-int(doay)
            if (yos==5):
                doam=doa[3:5]
                cm=aback.current_month
                yosm=cm-int(doam)
                #print(yosm)
                if(yosm>0):
                    #print("comp 5 yrs ,,, 3pp")
                    ppass=3
                else:
                    if (yosm==0):
                        doad=doa[0:2]
                        cd=aback.current_day
                        yosd=cd-int(doad)
                        if (yosd>=0):
                            #5yrs completed
                            ppass=3
                        else:
                            ppass=1
                    else:
                        #print("not comp 5 yrs,,,,1pp")
                        ppass=1
            else:
                if(yos>5):
                    #print("completed 5 yrs --- 3pp")
                    ppass=3
                else:
                    #print("not comopleted-----1pp")
                    ppass=1
            #nnn
            aback.update_pp(ppass,eid2[0])
            aback.update_pto(4.0,eid2[0])

def bback1():
    filename='startpage.py'
    win.destroy()
    os.system(filename)


win = Tk()
win.title('RAILWAY PASS MANAGEMENT SYSTEM ')
win.state('zoomed')
#win.resizable(0,0)


lempty7=Label(win,text=" ",width=20)
lempty7.grid(row=0,column=0)
lempty74=Label(win,text=" ",width=20)
lempty74.grid(row=1,column=2)
ltext=Label(win,text="CLICK Button ONLY WHEN U WANT TO RESET THE PASS BALANCE",width=80,bg='grey',font="Verdana 10 bold")
ltext.grid(row=2,column=2,columnspan=4)
lempty74=Label(win,text=" ",width=20)
lempty74.grid(row=3,column=2)
lempty74=Label(win,text=" ",width=20)
lempty74.grid(row=4,column=2)
bb1=Button(win,text="CONFIRM AND RESET PASS BALANCE",width=30,command=cnf,font="Verdana 10 bold")
bb1.grid(row=4,column=3)
lempty75=Label(win,text=" ",width=20)
lempty75.grid(row=5,column=2)

bback=Button(win,text="Back",width=8,command=bback1,bg="brown",bd=4,font="Verdana 10 bold")
bback.grid(row=6,column=3)



win.mainloop()
