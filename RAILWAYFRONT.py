from tkinter import *
from PIL import ImageTk,Image
import os
import time
import aback
global ppass
current_year=aback.current_year
current_month=aback.current_month
current_day=aback.current_day
global mmid

def get_selected_row1(event):
    global selected_tuple1
    index=list1.curselection()[0]
    #print(index)
    selected_tuple1=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple1[0])
    e2.delete(0,END)
    e2.insert(END,selected_tuple1[1])
    dobdisp.set(selected_tuple1[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple1[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple1[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple1[5])
    e6.delete(0,END)
    e6.insert(END,selected_tuple1[6])
    doadisp.set(selected_tuple1[7])
    ent.delete(0,END)
    ent.insert(END,selected_tuple1[8])
    members.delete(0,END)
    members.insert(END,selected_tuple1[9])
    elebel.delete(0,END)
    elebel.insert(END,selected_tuple1[10])


def clearpart1():
    e2.delete(0,END)
    dobvariable1.set(OPTIONS1[0])
    dobvariable2.set(OPTIONS2[0])
    dobvariable3.set(OPTIONS3[25])
    variable1.set(OPTIONS1[0])
    variable2.set(OPTIONS2[0])
    variable3.set(OPTIONS3[0])
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    ent.delete(0,END)
    members.delete(0,END)
    dobdisp.set("")
    doadisp.set("")
    currage.set("")

def clearlist():
    list1.delete(0,END)


def search_emp():
    if emp_id.get()=="":
        msg="PLEASE GIVE EMPLOYEE ID"
        list1.delete(0,END)
        list1.insert(END,msg)
    else:
        xyz=aback.checkid(int(emp_id.get()))
        #print(xyz)
        if type(xyz)==int:
            list1.delete(0,END)
            list1.insert(END,"No such employee id exists")
        else:
            list1.delete(0,END)
            for i in aback.viewemp(emp_id.get()):
                list1.insert(END,i)
        clearpart1()


def update_details():
    doy=dobvariable3.get()
    age=current_year-int(doy)
    currage.set("CURRENT AGE : "+str(age))
    dateofbirth=dobvariable1.get()+"-"+dobvariable2.get()+'-'+dobvariable3.get()
    dateofappointment=variable1.get()+"-"+variable2.get()+'-'+variable3.get()
    if emp_id.get()=="" or name_val.get()=="" or desig.get()=="" or basic_val.get()=="" or grade_pay.get()=="" or level_val.get()=="" or aadhar_no.get()=="":
        msg=" ENTRIES cannot be NULL FOR UPDATING"
        list1.delete(0,END)
        list1.insert(END,msg)
    else:
        list1.delete(0,END)
        aback.update_det(emp_id.get(),name_val.get(),dateofbirth,desig.get(),basic_val.get(),grade_pay.get(),level_val.get(),dateofappointment,variable4.get(),variable5.get(),aadhar_no.get())
        t=(emp_id.get(),name_val.get(),dateofbirth,desig.get(),basic_val.get(),grade_pay.get(),level_val.get(),dateofappointment,variable4.get(),variable5.get(),aadhar_no.get())
        list1.insert(END,t)



def passbal():
    flag2=0    #here is pbal PART
    if emp_id.get()=="" or aadhar_no.get()=="" or gpp.get()=="":
        pass
    else:
        if flag==0:
            xyz=aback.checkid(int(emp_id.get()))
            xyz2=aback.checkad(int(aadhar_no.get()))
        else:
            xyz=11 #jst giving an integer
            xyz2=11 #integer value
        if (type(xyz)==int and type(xyz2)==int):
            flag2=1
            if gpp.get()=="NOT OFFICER":
                doa=variable3.get()
                #print(doa)
                yos=current_year-int(doa)
                if (yos==5):
                    doam=variable2.get()
                    #print(doam)
                    yosm=current_month-int(doam)
                    #print(yosm)
                    if(yosm>0):

                        #print("comp 5 yrs ,,, 3pp")
                        ppass=3
                    else:
                        if (yosm==0):
                            #now same month so check for day
                            doad=variable1.get()
                            yosd=current_day-int(doad)
                            if (yosd>0):
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
            else:
                #print("officer ,6pp")
                #officer
                ppass=6
        else:
            list1.delete(0,END)
            list1.insert(END,"aadhar Number already exists")


    #to insert aadhar data
    if flag2==1:
        aback.insert_value3(emp_id.get(),aadhar_no.get(),ppass)
    else:
        pass


def add_data():
    global flag
    flag=0
    gpp.set("")
    doy=dobvariable3.get()
    age=current_year-int(doy)
    currage.set("CURRENT AGE : "+str(age))
    dateofbirth=dobvariable1.get()+"-"+dobvariable2.get()+'-'+dobvariable3.get()
    dateofappointment=variable1.get()+"-"+variable2.get()+'-'+variable3.get()
    if emp_id.get()=="" or name_val.get()=="" or desig.get()=="" or basic_val.get()=="" or grade_pay.get()=="" or level_val.get()=="" or variable4.get()=="" or variable5.get()=="" or aadhar_no.get()=="":
        msg="ENTRIES cannot be NULL"
        list1.delete(0,END)
        list1.insert(END,msg)
    else:
        flag=1
        xyz=aback.checkid(int(emp_id.get()))
        xyz2=aback.checkad(int(aadhar_no.get()))
        #print(xyz2)
        if (type(xyz)==int and type(xyz2)==int):
            list1.delete(0,END)
            aback.insert_value1(emp_id.get(),name_val.get(),dateofbirth,desig.get(),basic_val.get(),grade_pay.get(),level_val.get(),dateofappointment,variable4.get(),variable5.get(),aadhar_no.get())
            t=(emp_id.get(),name_val.get(),dateofbirth,desig.get(),basic_val.get(),grade_pay.get(),level_val.get(),dateofappointment,variable4.get(),variable5.get(),aadhar_no.get())
            list1.insert(END,t)
            if (float(grade_pay.get())>=5400):
                gpp.set("OFFICER")
            else:
                gpp.set("NOT OFFICER")
        else:
            list1.delete(0,END)
            list1.insert(END,"id or aadhar Number duplicate")
        passbal()

def del_emp():
        if emp_id.get()=="":
            msg="Employee id cannot be NULL"
            list1.delete(0,END)
            list1.insert(END,msg)
        else:
            aback.delete_emp(emp_id.get())
            list1.delete(0,END)
            list1.insert(END,"MEMBER DELETED SUCCESSFULLY")

def go_next():
        filename='passpage.py'
        win.destroy()
        os.system(filename)

def bback1():
    filename='startpage.py'
    win.destroy()
    os.system(filename)

OPTIONS1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15",
"16","17","18","19","20","21","22","23","24",
"25","26","27","28","29","30","31"]

OPTIONS2 = ["01","02","03","04","05","06","07","08","09","10","11","12"] #etc

OPTIONS3 = ["2028","2027","2026","2025","2024","2023","2022","2021","2020","2019","2018","2017","2016","2015","2014","2013","2012",
"2011","2010","2009",'2008',
'2007',
'2006',
'2005',
'2004',
'2003',
'2002',
'2001',
'2000',
'1999',
'1998',
'1997',
'1996',
'1995',
'1994',
'1993',
'1992',
'1991','1990','1989','1988','1987','1986','1985','1984','1983','1982','1981','1980','1979','1978',
'1977','1976','1975','1974','1973','1972','1971','1970','1969','1968','1967','1966','1965','1964','1963','1962','1961','1960','1959','1958','1957','1956','1955','1954','1953',
'1952','1951','1950','1949','1948','1947','1946','1945','1944','1943','1942']



win = Tk()
win.title('RAILWAY PASS MANAGEMENT SYSTEM ')
win.state('zoomed')
#win.resizable(0,0)
img=ImageTk.PhotoImage(Image.open("ser.jpg"))
imglabel=Label(win,image=img)
imglabel.grid(row=0,column=3,columnspan=4)

l1=Label(win,text="EMPLOYEE ID",width=20)
l1.grid(row=1,column=0)
emp_id=StringVar()
e1=Entry(win,width=20,textvariable=emp_id,relief='solid')
e1.grid(row=1,column=1)


l2=Label(win,text="NAME",width=20)
l2.grid(row=2,column=0)
name_val=StringVar()
e2=Entry(win,width=20,textvariable=name_val,relief='solid')
e2.grid(row=2,column=1)


dob=Label(win,text="DOB (DD-MM-YYYY)",width=20)
dob.grid(row=3,column=0)
dobvariable1 = StringVar()
dobvariable1.set(OPTIONS1[0]) # default value
dobvariable2 = StringVar()
dobvariable2.set(OPTIONS2[0]) # default value
dobvariable3 = StringVar()
dobvariable3.set(OPTIONS3[40]) # default value
day = OptionMenu(win, dobvariable1, *OPTIONS1)
day.grid(row=3,column=1,sticky="e")
mon = OptionMenu(win, dobvariable2, *OPTIONS2)
mon.grid(row=3,column=2)
yr = OptionMenu(win, dobvariable3, *OPTIONS3)
yr.grid(row=3,column=3)
currage=StringVar()
dobdisp=StringVar()
dobdis=Label(win,textvariable=dobdisp,width=20)
dobdis.grid(row=3,column=4)


l3=Label(win,text="DESIGNATION",width=20)
l3.grid(row=4,column=0)
desig=StringVar()
e3=Entry(win,width=20,textvariable=desig,relief='solid')
e3.grid(row=4,column=1)
agelebel=Label(win,textvariable=currage,width=20)
agelebel.grid(row=4,column=2)

l4=Label(win,text="BASIC",width=20)
l4.grid(row=5,column=0)
basic_val=StringVar()
e4=Entry(win,width=20,textvariable=basic_val,relief='solid')
e4.grid(row=5,column=1)

l5=Label(win,text="GRADE PAY",width=20)
l5.grid(row=6,column=0)
grade_pay=StringVar()
e5=Entry(win,width=20,textvariable=grade_pay,relief='solid')
e5.grid(row=6,column=1)
gpp=StringVar()
gplebel=Label(win,textvariable=gpp,width=20)
gplebel.grid(row=6,column=3)




l6=Label(win,text="LEVEL",width=20)
l6.grid(row=7,column=0)
level_val=StringVar()
e6=Entry(win,width=20,textvariable=level_val,relief='solid')
e6.grid(row=7,column=1)
alebel=Label(win,text="AADHAR NO",width=20)
alebel.grid(row=7,column=3)
aadhar_no=StringVar()
elebel=Entry(win,width=20,textvariable=aadhar_no,relief='solid')
elebel.grid(row=7,column=4)



l7=Label(win,text="DOA (DD-MM-YYYY)",width=20)
l7.grid(row=8,column=0)

variable1 = StringVar()
variable1.set(OPTIONS1[0]) # default value

variable2 = StringVar()
variable2.set(OPTIONS2[0]) # default value

variable3 = StringVar()
variable3.set(OPTIONS3[10]) # default value

d = OptionMenu(win, variable1, *OPTIONS1)
d.grid(row=8,column=1,sticky="e")
m = OptionMenu(win, variable2, *OPTIONS2)
m.grid(row=8,column=2)
y = OptionMenu(win, variable3, *OPTIONS3)
y.grid(row=8,column=3)

doadisp=StringVar()
doadis=Label(win,textvariable=doadisp,width=20)
doadis.grid(row=8,column=4)

l8=Label(win,text="ENTITLEMENT",width=20)
l8.grid(row=9,column=0)
variable4 = StringVar()
ent = Entry(win,width=20 ,textvariable=variable4,relief='solid')
ent.grid(row=9,column=1,sticky="e")


l9=Label(win,text="DEPARTMENT",width=20)
l9.grid(row=10,column=0)
variable5 = StringVar()
members=Entry(win,width=20 ,textvariable=variable5,relief='solid')
members.grid(row=10,column=1,sticky="e")



b2=Button(win,text="CONFIRM DETAILS",width=20,height=3,command=add_data,bg="grey",bd=4,font="Verdana 10 bold")
b2.grid(row=11,column=1)


#########LISSTT###########
list1=Listbox(win,width=70,height=20)
list1.grid(row=7,column=5,rowspan=5,columnspan=5)
list1.bind("<<ListboxSelect>>",get_selected_row1)

b10=Button(win,text="CLEAR LISTBOXES",width=20,command=clearlist,font="Verdana 10 bold",bg="grey",bd=4)
b10.grid(row=15,column=7)
bback=Button(win,text="Back",width=8,command=bback1,bg="brown",bd=4,font="Verdana 10 bold")
bback.grid(row=15,column=8)

########################
l16=Label(win,text="EMPLOYEE ID",width=20)
l16.grid(row=1,column=7)
emp_id2=StringVar()
e16=Entry(win,width=20,textvariable=emp_id,relief='solid')
e16.grid(row=1,column=8)

b3=Button(win,text="SEARCH EMPLOYEE",width=20,command=search_emp,font="Verdana 10 bold",bg="grey",bd=4)
b3.grid(row=3,column=7)
b4=Button(win,text=" UPDATE-DETAILS ",width=20,command=update_details,font="Verdana 10 bold",bg="grey",bd=4)
b4.grid(row=3,column=8)
b5=Button(win,text="DELETE ENTRY",width=20,command=del_emp,font="Verdana 10 bold",bg="grey",bd=4)
b5.grid(row=4,column=7)
bnext=Button(win,text="GO TO PASS APPLICATION",width=20,command=go_next,font="Verdana 10 bold",bg="grey",bd=4)
bnext.grid(row=4,column=8)


win.mainloop()
