from tkinter import *
from PIL import ImageTk,Image
import os
import sys
import time
import datetime
import aback

xx=datetime.datetime.today().strftime('%Y-%m-%d')
#print(xx)
cy=int(xx[0:4])
cm=int(xx[5:7])

if cm>5:
    #print ("update cf hua h")
    aback.updatecf()
else:
    pass

def checkpbal():
        if empl_id.get()=="" or ad_no.get()=="":
            ee3.delete(0,END)
            ee3.insert(END,"NULL ENTRIES NOT POSSIBLE")
        else:
            xyz=aback.checkid(int(empl_id.get()))
            #print(xyz)
            if type(xyz)==int:
                ee3.delete(0,END)
                ee3.insert(END,"No such employee id exists")
            else:
                ADH=aback.getaadhaar(empl_id.get())[0][0]
                #print(ADH)
                if int(ad_no.get())==ADH:
                    #print("DO SOMETHING HERE")
                    top=passvariable1.get()
                    if top=="PTO":
                        ptovalue=aback.getpto(int(empl_id.get()))
                        ee3.delete(0,END)
                        ee3.insert(END,ptovalue)
                    elif top=="PRIVILEGE PASS":
                        ppvalue=aback.getpp(int(empl_id.get()))
                        #print(type(ppvalue[0][0]))
                        ee3.delete(0,END)
                        ee3.insert(END,ppvalue)
                    elif top=="CARRY FWD PTO":
                        ee3.delete(0,END)
                        cfpto=aback.getcfpto(int(empl_id.get()))
                        #print(cfpto)
                        try:
                            type(cfpto[0][0])
                            ee3.delete(0,END)
                            ee3.insert(END,cfpto)
                        except IndexError:
                            ee3.delete(0,END)
                            ee3.insert(END,"NO CARRY FWD PTO")

                    elif top=="CARRY FWD PP":
                        ee3.delete(0,END)
                        cfpp=aback.getcfpp(int(empl_id.get()))
                        #print(cfpp)
                        try:
                            type(cfpp[0][0])
                            ee3.delete(0,END)
                            ee3.insert(END,cfpp)
                        except IndexError:
                            ee3.delete(0,END)
                            ee3.insert(END,"NO CARRY FWD PP")

                else:
                    ee3.delete(0,END)
                    ee3.insert(END,"WRONG AADHAR NUMBER")


def submitdata():
    if empl_id.get()=="" or ad_no.get()=="" or from_city.get()=="" or to_city.get()=="" or via_city.get()==""  or route.get()=="" or fm.get()=="" or doj.get()=="" or dov.get()=="":
        msg="ENTRIES cannot be NULL"
        msgg.set(msg)
    else:
        #print("xxxxxxxxxvvvvvvvvvvvvv")
        xyz=aback.checkid(int(empl_id.get()))
        #print(xyz)
        if type(xyz)==int:
                msgg.set("no such emp id exists")
        else:
            ADH=aback.getaadhaar(empl_id.get())[0][0]
            if int(ad_no.get())==ADH:
                #print("DO SOMETHING HERE")
                if passvariable1.get()=="PTO":
                    ptoval=aback.getpto(int(empl_id.get()))[0][0]
                    if journeyvariable.get()=="HALF/ONE WAY JOURNEY":
                        newpto=ptoval-0.5
                        if newpto>=0:
                            aback.insert_value4(empl_id.get(),ad_no.get(),passvariable1.get(),from_city.get(),to_city.get(),via_city.get(),journeyvariable.get(),route.get(),fm.get(),doj.get(),dov.get(),texx.get(1.0,END))
                            aback.update_pto(newpto,empl_id.get())
                            msgg.set("SUCCESSFUL")
                            ee4.delete(0,END)
                            ee5.delete(0,END)
                            ee6.delete(0,END)
                            ee7.delete(0,END)
                            ee77.delete(0,END)
                            edate.delete(0,END)
                            edate2.delete(0,END)
                            texx.delete(1.0,END)
                            checkpbal()
                        else:
                            msgg.set("NOT ENOUGH PTO BALANCE")
                    else:
                        newpto=ptoval-1.0
                        if newpto>=0:
                            aback.insert_value4(empl_id.get(),ad_no.get(),passvariable1.get(),from_city.get(),to_city.get(),via_city.get(),journeyvariable.get(),route.get(),fm.get(),doj.get(),dov.get(),texx.get(1.0,END))
                            aback.update_pto(newpto,empl_id.get())
                            msgg.set("SUCCESSFUL")
                            ee4.delete(0,END)
                            ee5.delete(0,END)
                            ee6.delete(0,END)
                            ee7.delete(0,END)
                            ee77.delete(0,END)
                            edate.delete(0,END)
                            edate2.delete(0,END)
                            texx.delete(1.0,END)
                            checkpbal()
                        else:
                            msgg.set("NOT ENOUGH PTO BALANCE")
                elif passvariable1.get()=="PRIVILEGE PASS":
                    ppval=aback.getpp(int(empl_id.get()))[0][0]
                    if journeyvariable.get()=="HALF/ONE WAY JOURNEY":
                        newpp=ppval-0.5
                        if newpp>=0:
                            aback.insert_value4(empl_id.get(),ad_no.get(),passvariable1.get(),from_city.get(),to_city.get(),via_city.get(),journeyvariable.get(),route.get(),fm.get(),doj.get(),dov.get(),texx.get(1.0,END))
                            aback.update_pp(newpp,empl_id.get())
                            msgg.set("SUCCESSFUL")
                            ee4.delete(0,END)
                            ee5.delete(0,END)
                            ee6.delete(0,END)
                            ee7.delete(0,END)
                            ee77.delete(0,END)
                            edate.delete(0,END)
                            edate2.delete(0,END)
                            texx.delete(1.0,END)
                            checkpbal()
                        else:
                            msgg.set("NOT ENOUGH PP BALANCE")
                    else:
                        newpp=ppval-1
                        if newpp>=0:
                            aback.insert_value4(empl_id.get(),ad_no.get(),passvariable1.get(),from_city.get(),to_city.get(),via_city.get(),journeyvariable.get(),route.get(),fm.get(),doj.get(),dov.get(),texx.get(1.0,END))
                            aback.update_pp(newpp,empl_id.get())
                            msgg.set("SUCCESSFUL")
                            ee4.delete(0,END)
                            ee5.delete(0,END)
                            ee6.delete(0,END)
                            ee7.delete(0,END)
                            ee77.delete(0,END)
                            edate.delete(0,END)
                            edate2.delete(0,END)
                            texx.delete(1.0,END)
                            checkpbal()
                        else:
                            msgg.set("NOT ENOUGH PP BALANCE")

                elif passvariable1.get()=="CARRY FWD PTO":
                    cfptoval=aback.getcfpto(int(empl_id.get()))[0][0]
                    if journeyvariable.get()=="HALF/ONE WAY JOURNEY":
                        newcfpto=cfptoval-0.5
                        if newcfpto>=0:
                            aback.insert_value4(empl_id.get(),ad_no.get(),passvariable1.get(),from_city.get(),to_city.get(),via_city.get(),journeyvariable.get(),route.get(),fm.get(),doj.get(),dov.get(),texx.get(1.0,END))
                            aback.update_cfpto(newcfpto,empl_id.get())
                            msgg.set("SUCCESSFUL")
                            ee4.delete(0,END)
                            ee5.delete(0,END)
                            ee6.delete(0,END)
                            ee7.delete(0,END)
                            ee77.delete(0,END)
                            edate.delete(0,END)
                            edate2.delete(0,END)
                            texx.delete(1.0,END)
                            checkpbal()
                        else:
                            msgg.set("NOT ENOUGH CARRY FORWARD PTO BALANCE")

                    else:
                        newcfpto=cfptoval-1.0
                        if newcfpto>=0:
                            aback.insert_value4(empl_id.get(),ad_no.get(),passvariable1.get(),from_city.get(),to_city.get(),via_city.get(),journeyvariable.get(),route.get(),fm.get(),doj.get(),dov.get(),texx.get(1.0,END))
                            aback.update_cfpto(newcfpto,empl_id.get())
                            msgg.set("SUCCESSFUL")
                            ee4.delete(0,END)
                            ee5.delete(0,END)
                            ee6.delete(0,END)
                            ee7.delete(0,END)
                            ee77.delete(0,END)
                            edate.delete(0,END)
                            edate2.delete(0,END)
                            texx.delete(1.0,END)
                            checkpbal()
                        else:
                            msgg.set("NOT ENOUGH CARRY FORWARD PTO BALANCE")

                elif passvariable1.get()=="CARRY FWD PP":
                    cfppval=aback.getcfpp(int(empl_id.get()))[0][0]
                    if journeyvariable.get()=="HALF/ONE WAY JOURNEY":
                        newcfpp=cfppval-0.5
                        if newcfpp>=0:
                            aback.insert_value4(empl_id.get(),ad_no.get(),passvariable1.get(),from_city.get(),to_city.get(),via_city.get(),journeyvariable.get(),route.get(),fm.get(),doj.get(),dov.get(),texx.get(1.0,END))
                            aback.update_cfpp(newcfpp,empl_id.get())
                            msgg.set("SUCCESSFUL")
                            ee4.delete(0,END)
                            ee5.delete(0,END)
                            ee6.delete(0,END)
                            ee7.delete(0,END)
                            ee77.delete(0,END)
                            edate.delete(0,END)
                            edate2.delete(0,END)
                            texx.delete(1.0,END)
                            checkpbal()
                        else:
                            msgg.set("NOT ENOUGH CARRY FORWARD PP BALANCE")
                    else:
                        newcfpp=cfppval-1
                        if newcfpp>=0:
                            aback.insert_value4(empl_id.get(),ad_no.get(),passvariable1.get(),from_city.get(),to_city.get(),via_city.get(),journeyvariable.get(),route.get(),fm.get(),doj.get(),dov.get(),texx.get(1.0,END))
                            aback.update_cfpp(newcfpp,empl_id.get())
                            msgg.set("SUCCESSFUL")
                            ee4.delete(0,END)
                            ee5.delete(0,END)
                            ee6.delete(0,END)
                            ee7.delete(0,END)
                            ee77.delete(0,END)
                            edate.delete(0,END)
                            edate2.delete(0,END)
                            texx.delete(1.0,END)
                            checkpbal()
                        else:
                            msgg.set("NOT ENOUGH CARRY FORWARD PP BALANCE")

            else:
                msgg.set("WRONG AADHAR NO.")

def bback1():
    filename='startpage.py'
    root.destroy()
    os.system(filename)



OPTIONSpass = ["PTO","PRIVILEGE PASS","CARRY FWD PTO","CARRY FWD PP"]
OPTIONS12 = ["HALF/ONE WAY JOURNEY","RETURN/FULL JOURNEY"]
root = Tk()

root.title('RAILWAY PASS MANAGEMENT SYSTEM 2')
root.state('zoomed')
img=ImageTk.PhotoImage(Image.open("ser.jpg"))
imglabel=Label(root,image=img)
imglabel.grid(row=0,column=3,columnspan=4)

lempty=Label(root,text=" ",width=20,height=3)
lempty.grid(row=1,column=2)


ll1=Label(root,text="EMPLOYEE ID",width=20)
ll1.grid(row=2,column=0)
empl_id=StringVar()
ee1=Entry(root,width=20,textvariable=empl_id,relief='solid')
ee1.grid(row=2,column=1)
ll2=Label(root,text="AADHAR NO.",width=20)
ll2.grid(row=2,column=2)
ad_no=StringVar()
ee2=Entry(root,width=20,textvariable=ad_no,relief='solid')
ee2.grid(row=2,column=3)

lempty2=Label(root,text=" ",width=20)
lempty2.grid(row=3,column=0)


ll3=Label(root,text="TYPE OF PASS :",width=20)
ll3.grid(row=4,column=0)
passvariable1 = StringVar()
passvariable1.set(OPTIONSpass[0])
p = OptionMenu(root,passvariable1, *OPTIONSpass)
p.grid(row=4,column=1,sticky="e")


lempty2=Label(root,text=" ",width=20)
lempty2.grid(row=5,column=0)

bb1=Button(root,text="CHECK PASS BALANCE",width=20,command=checkpbal)
bb1.grid(row=6,column=1)
lempty4=Label(root,text=" ",width=20)
lempty4.grid(row=7,column=0)
ll4=Label(root,text="REMAINING BAL:",width=20)
ll4.grid(row=8,column=0)
rbalval=StringVar()
ee3=Entry(root,width=30,textvariable=rbalval,relief='solid')
ee3.grid(row=8,column=1)

lempty3=Label(root,text=" ",width=20)
lempty3.grid(row=9,column=0)

ll5=Label(root,text="APPLICATION FOR PASS :",width=30)
ll5.grid(row=10,column=2,columnspan=2)
msgg=StringVar()
ltext=Label(root,textvariable=msgg,width=50,bg='grey',font="Verdana 10 bold")
ltext.grid(row=10,column=4,columnspan=4)

lempty5=Label(root,text=" ",width=20)
lempty5.grid(row=11,column=0)
#############################
ll6=Label(root,text="FROM",width=10)
ll6.grid(row=12,column=0,sticky='e')
from_city=StringVar()
ee4=Entry(root,width=15,textvariable=from_city,relief='solid')
ee4.grid(row=12,column=1)

ll7=Label(root,text="TO",width=10)
ll7.grid(row=12,column=2,sticky='e')
to_city=StringVar()
ee5=Entry(root,width=15,textvariable=to_city,relief='solid')
ee5.grid(row=12,column=3)
lvia=Label(root,text='VIA',width=15)
lvia.grid(row=12,column=4,sticky='e')
via_city=StringVar()
ee6=Entry(root,width=15,textvariable=via_city,relief='solid')
ee6.grid(row=12,column=5)
lempty6=Label(root,text=" ",width=20)
lempty6.grid(row=11,column=0)
journeyvariable = StringVar()
journeyvariable.set(OPTIONS12[0])
j = OptionMenu(root,journeyvariable, *OPTIONS12)
j.grid(row=12,column=6,sticky="e")

###################################
ll8=Label(root,text="BREAK JOURNEY AT: ",width=20)
ll8.grid(row=13,column=0,sticky='e')
route=StringVar()
ee7=Entry(root,width=15,textvariable=route,relief='solid')
ee7.grid(row=13,column=1)
ll9=Label(root,text="NUMBER OF TICKETS :",width=20)
ll9.grid(row=13,column=2,sticky='e')
fm=StringVar()
ee77=Entry(root,width=15,textvariable=fm,relief='solid')
ee77.grid(row=13,column=3)
ldate=Label(root,text="APPLICATION DATE(DD-MM-YYYY) :",width=28)
ldate.grid(row=13,column=4,sticky='e')
doj=StringVar()
edate=Entry(root,width=15,textvariable=doj,relief='solid')
edate.grid(row=13,column=5)
ldate2=Label(root,text="VALID TILL(DD-MM-YYYY) :",width=20)
ldate2.grid(row=13,column=6,sticky='w')
dov=StringVar()
edate2=Entry(root,width=15,textvariable=dov,relief='solid')
edate2.grid(row=13,column=7)


lempty7=Label(root,text=" ",width=20)
lempty7.grid(row=14,column=0)
data_v=StringVar()
texx=Text(root,width=60,height=5)
texx.grid(row=15,column=1,columnspan=4,rowspan=2)
bb1=Button(root,text="CONFIRM AND SUBMIT",width=25,command=submitdata,bg="grey",bd=4,font="Verdana 10 bold")
bb1.grid(row=15,column=5)
bback=Button(root,text="Back",width=8,command=bback1,bg="brown",bd=4,font="Verdana 10 bold")
bback.grid(row=15,column=7)







root.mainloop()
