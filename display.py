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

if cm>5:
    #print ("update cf hua h")
    aback.updatecf()
else:
    pass


def get_selected_row(event):
    global selected_tuple
    index=list2.curselection()[0]
    #print(index)
    selected_tuple=list2.get(index)
    #print(selected_tuple)
    top_pp.set("")
    from_city.set("")
    to_city.set("")
    via_city.set("")
    top_j.set("")
    break_j.set("")
    fm.set("")
    doj.set("")
    texx1.delete(1.0,END)
    top_pp.set(selected_tuple[0])
    from_city.set(selected_tuple[1])
    to_city.set(selected_tuple[2])
    via_city.set(selected_tuple[3])
    top_j.set(selected_tuple[4])
    break_j.set(selected_tuple[5])
    fm.set(selected_tuple[6])
    doj.set(selected_tuple[7])
    texx1.insert(1.0,selected_tuple[8])


def clear_all():
    top_pp.set("")
    from_city.set("")
    to_city.set("")
    via_city.set("")
    top_j.set("")
    break_j.set("")
    fm.set("")
    doj.set("")
    texx1.delete(1.0,END)
    list1.delete(0,END)
    list2.delete(0,END)
    name_val.set("")
    dob_val.set("")
    desig.set("")
    basic_val.set("")
    grade_pay.set("")
    level_val.set("")
    doa_val.set("")
    variable4.set("")
    variable5.set("")
    pp_b.set("")
    pto_b.set("")
    cfpp_b.set("")
    cfpto_b.set("")


def search_emp():
    if emp_id.get()=="" or aadhar_no.get()=="":
        msg="PLEASE GIVE BOTH EMPLOYEE ID AND AADHAR"
        msgg.set(msg)
        list1.delete(0,END)
        list2.delete(0,END)
        name_val.set("")
        dob_val.set("")
        desig.set("")
        basic_val.set("")
        grade_pay.set("")
        level_val.set("")
        doa_val.set("")
        variable4.set("")
        variable5.set("")
        pp_b.set("")
        pto_b.set("")
        cfpp_b.set("")
        cfpto_b.set("")
    else:
        xyz=aback.checkid(int(emp_id.get()))
        #print(xyz)
        if type(xyz)==int:
            msgg.set("No such employee id exists")
            list1.delete(0,END)
            list2.delete(0,END)
            name_val.set("")
            dob_val.set("")
            desig.set("")
            basic_val.set("")
            grade_pay.set("")
            level_val.set("")
            doa_val.set("")
            variable4.set("")
            variable5.set("")
            pp_b.set("")
            pto_b.set("")
            cfpp_b.set("")
            cfpto_b.set("")
        else:

            msgg.set("SUCCESSFUL SEARCH")
            ADH=aback.getaadhaar(emp_id.get())[0][0]
            if int(aadhar_no.get())==ADH:
                for dd in aback.viewemp(emp_id.get()):
                    #print(dd)
                    name_val.set(dd[1])
                    dob_val.set(dd[2])
                    desig.set(dd[3])
                    basic_val.set(dd[4])
                    grade_pay.set(dd[5])
                    level_val.set(dd[6])
                    doa_val.set(dd[7])
                    variable4.set(dd[8])
                    variable5.set(dd[9])
                list1.delete(0,END)
                for fd in aback.viewfam(emp_id.get()):
                    #print(fd)
                    list1.insert(END,fd[2:6])
                ptovalue=aback.getpto(int(emp_id.get()))[0][0]
                pto_b.set("PTO BAL:   "+str(ptovalue))
                ppvalue=aback.getpp(int(emp_id.get()))[0][0]
                pp_b.set("PP BAL :   "+str(ppvalue))

                cfptovalue=aback.getcfpto(int(emp_id.get()))
                try:
                    type(cfptovalue[0][0])
                    cfpto_b.set("CF PTO BAL:   "+str(cfptovalue[0][0]))
                except IndexError:
                    cfpto_b.set(" NO CF PTO BAL")

                cfppvalue=aback.getcfpp(int(emp_id.get()))
                try:
                    type(cfppvalue[0][0])
                    cfpp_b.set("CF PP BAL:   "+str(cfppvalue[0][0]))
                except IndexError:
                    cfpp_b.set(" NO CF PP BAL")

                list2.delete(0,END)
                for td in aback.traveldata(emp_id.get()):
                    #print(td)
                    list2.insert(END,td)


            else:
                list1.delete(0,END)
                name_val.set("")
                dob_val.set("")
                desig.set("")
                basic_val.set("")
                grade_pay.set("")
                level_val.set("")
                doa_val.set("")
                variable4.set("")
                variable5.set("")
                pp_b.set("")
                pto_b.set("")
                list2.delete(0,END)
                top_pp.set("")
                from_city.set("")
                to_city.set("")
                via_city.set("")
                top_j.set("")
                break_j.set("")
                fm.set("")
                doj.set("")
                texx1.delete(1.0,END)
                msgg.set("WRONG AADHAR NO")


def submit():
    search_emp()

def bback1():
    filename='startpage.py'
    win.destroy()
    os.system(filename)



win = Tk()
win.title('RAILWAY PASS MANAGEMENT SYSTEM ')
win.state('zoomed')
#win.resizable(0,0)
img=ImageTk.PhotoImage(Image.open("ser.jpg"))
imglabel=Label(win,image=img)
imglabel.grid(row=0,column=2,columnspan=4)

lempty=Label(win,text=" ",width=20)
lempty.grid(row=1,column=2)


l1=Label(win,text="EMPLOYEE ID",width=20)
l1.grid(row=2,column=2)
emp_id=StringVar()
e1=Entry(win,width=20,textvariable=emp_id)
e1.grid(row=2,column=3)
alebel=Label(win,text="AADHAR NO",width=20)
alebel.grid(row=2,column=4)
aadhar_no=StringVar()
elebel=Entry(win,width=20,textvariable=aadhar_no)
elebel.grid(row=2,column=5)
msgg=StringVar()
ltext=Label(win,textvariable=msgg,width=40,bg='grey',font="Verdana 10 bold")
ltext.grid(row=2,column=6,columnspan=3)

lempty2=Label(win,text=" ",width=20)
lempty2.grid(row=3,column=2)
lempty3=Label(win,text=" ",width=20)
lempty3.grid(row=4,column=2)

l2=Label(win,text="NAME",width=20)
l2.grid(row=5,column=0)
name_val=StringVar()
e2=Label(win,width=20,textvariable=name_val,relief='solid')
e2.grid(row=5,column=1)
dob=Label(win,text="DOB (DD-MM-YYYY)",width=20)
dob.grid(row=5,column=3)
dob_val=StringVar()
e3=Label(win,width=20,textvariable=dob_val,relief='solid')
e3.grid(row=5,column=4)

l3=Label(win,text="DESIGNATION",width=20)
l3.grid(row=5,column=6)
desig=StringVar()
e3=Label(win,width=20,textvariable=desig,relief='solid')
e3.grid(row=5,column=7)

lempty4=Label(win,text=" ",width=20)
lempty4.grid(row=6,column=2)


l4=Label(win,text="BASIC",width=20)
l4.grid(row=7,column=0)
basic_val=StringVar()
e4=Label(win,width=20,textvariable=basic_val,relief='solid')
e4.grid(row=7,column=1)

l5=Label(win,text="GRADE PAY",width=20)
l5.grid(row=7,column=3)
grade_pay=StringVar()
e5=Label(win,width=20,textvariable=grade_pay,relief='solid')
e5.grid(row=7,column=4)

l6=Label(win,text="LEVEL",width=20)
l6.grid(row=7,column=6)
level_val=StringVar()
e6=Label(win,width=20,textvariable=level_val,relief='solid')
e6.grid(row=7,column=7)

lempty5=Label(win,text=" ",width=20)
lempty5.grid(row=8,column=2)



l7=Label(win,text="DOA (DD-MM-YYYY)",width=20)
l7.grid(row=9,column=0)
doa_val=StringVar()
ll7=Label(win,width=20,textvariable=doa_val,relief='solid')
ll7.grid(row=9,column=1)

l8=Label(win,text="ENTITLEMENT",width=20)
l8.grid(row=9,column=3)
variable4 = StringVar()
ent = Label(win,width=20 ,textvariable=variable4,relief='solid')
ent.grid(row=9,column=4)


l9=Label(win,text="DEPARTMENT",width=20)
l9.grid(row=9,column=6)
variable5 = StringVar()
members=Label(win,width=20 ,textvariable=variable5,relief='solid')
members.grid(row=9,column=7)

lempty6=Label(win,text=" ",width=20)
lempty6.grid(row=10,column=2)


la=Label(win,text="FAMILY DATA",width=20,font="Verdana 10 bold")
la.grid(row=11,column=1,columnspan=2)
list1=Listbox(win,width=60)
list1.grid(row=12,column=1,columnspan=2,rowspan=4)
sb1=Scrollbar(win)
sb1.grid(row=13,column=3,sticky='w',columnspan=2)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


l20=Label(win,text="PASS BALANCE:",width=20,font="Verdana 10 bold")
l20.grid(row=11,column=3,columnspan=2)
pto_b=StringVar()
ex1=Label(win,width=20,textvariable=pto_b)
ex1.grid(row=12,column=3,columnspan=2)
pp_b=StringVar()
ex2=Label(win,width=20,textvariable=pp_b)
ex2.grid(row=13,column=3,columnspan=2)
cfpto_b=StringVar()
ex3=Label(win,width=20,textvariable=cfpto_b)
ex3.grid(row=14,column=3,columnspan=2)
cfpp_b=StringVar()
ex4=Label(win,width=20,textvariable=cfpp_b)
ex4.grid(row=15,column=3,columnspan=2)



l21=Label(win,text="PASS APPLICATION HISTORY",width=23,font="Verdana 10 bold")
l21.grid(row=11,column=6,columnspan=2,sticky='w')

list2=Listbox(win,width=80)
list2.grid(row=12,column=5,columnspan=4,rowspan=4)
sb2=Scrollbar(win)
sb2.grid(row=13,column=9,sticky='w',columnspan=2)
list2.configure(yscrollcommand=sb2.set)
sb2.configure(command=list2.yview)
list2.bind("<<ListboxSelect>>",get_selected_row)

lempty7=Label(win,text=" ",width=20)
lempty7.grid(row=17,column=2)

llxx=Label(win,text="TYPE OF PASS",width=10)
llxx.grid(row=18,column=0)
top_pp=StringVar()
eexx=Label(win,width=15,textvariable=top_pp,relief='solid')
eexx.grid(row=19,column=0)


ll6=Label(win,text="FROM",width=10)
ll6.grid(row=18,column=1)
from_city=StringVar()
ee4=Label(win,width=15,textvariable=from_city,relief='solid')
ee4.grid(row=19,column=1)
ll7=Label(win,text="TO",width=10)
ll7.grid(row=18,column=2)
to_city=StringVar()
ee5=Label(win,width=15,textvariable=to_city,relief='solid')
ee5.grid(row=19,column=2)
lvia=Label(win,text='VIA',width=15)
lvia.grid(row=18,column=3)
via_city=StringVar()
ee6=Label(win,width=15,textvariable=via_city,relief='solid')
ee6.grid(row=19,column=3)
ltop=Label(win,text='TYPE OF JOURNEY',width=15)
ltop.grid(row=18,column=4)
top_j=StringVar()
ee67=Label(win,width=15,textvariable=top_j,relief='solid')
ee67.grid(row=19,column=4)

ll8=Label(win,text="BREAK JOURNEY AT: ",width=20)
ll8.grid(row=18,column=5)
break_j=StringVar()
ee7=Label(win,width=15,textvariable=break_j,relief='solid')
ee7.grid(row=19,column=5)
ll9=Label(win,text="NO. OF TICKETS :",width=20)
ll9.grid(row=18,column=6)
fm=StringVar()
ee77=Label(win,width=15,textvariable=fm,relief='solid')
ee77.grid(row=19,column=6)
ldate=Label(win,text="JOURNEY DATE(DD-MM-YYYY) :",width=24)
ldate.grid(row=18,column=7)
doj=StringVar()
edate=Label(win,width=15,textvariable=doj,relief='solid')
edate.grid(row=19,column=7)

lempty77=Label(win,text=" ",width=20)
lempty77.grid(row=20,column=2)

texx1=Text(win,width=60,height=4)
texx1.grid(row=21,column=1,columnspan=4,rowspan=2,sticky='w')







bb1=Button(win,text="CONFIRM AND DISPLAY",width=25,command=submit,bg="grey",bd=4,font="Verdana 10 bold")
bb1.grid(row=21,column=5,columnspan=2)
bb2=Button(win,text="CLEAR ALL:",width=25,command=clear_all,font="Verdana 10 bold")
bb2.grid(row=21,column=7)

bback=Button(win,text="Back",width=8,command=bback1,bg="brown",bd=4,font="Verdana 10 bold")
bback.grid(row=22,column=7)

win.mainloop()
