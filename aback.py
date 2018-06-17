import sqlite3
global e_id
global a_id
global current_year
global current_month
import time
import datetime


xx=datetime.datetime.today().strftime('%Y-%m-%d')
cy=int(xx[0:4])
cm=int(xx[5:7])
cd=int(xx[-2:])
current_year=cy
current_month=cm
current_day=cd

def create_table():
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS empdata(emp_id INTEGER PRIMARY KEY ,name TEXT NOT NULL,DOB DATE NOT NULL,designation TEXT NOT NULL,Basic FLOAT NOT NULL,Grade_pay FLOAT NOT NULL ,Level INTEGER NOT NULL ,DOA DATE NOT NULL ,Entitlement TEXT NOT NULL,department TEXT NOT NULL,aadhar INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS famdata2(num INTEGER PRIMARY KEY, emp_id INTEGER,relationship TEXT,fname TEXT,fdob DATE,faadhar INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS pbal (emp_id INTEGER,aadhar INTEGER PRIMARY KEY,pto_bal FLOAT,pp_bal FLOAT,counter INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS travel_data5 (emp_id INTEGER,aadhar INTEGER,top TEXT,f_city VARCHAR(25),to_city VARCHAR(25),via_city VARCHAR(20),TOJ TEXT,route_city VARCHAR(50),num_tickets INTEGER,DOJ DATE,DOV DATE,comment TEXT,year INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS cfpbal (emp_id INTEGER,aadhar INTEGER PRIMARY KEY,cfpto_bal FLOAT,cfpp_bal FLOAT)")
    cur.execute("CREATE TABLE IF NOT EXISTS pwd (num INTEGER PRIMARY KEY,pass VARCHAR(25))")
    con.commit()
    con.close()

def insert_value1(id,n,dob,de,b,gp,l,doa,e,dpt,ano):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("INSERT INTO empdata VALUES(?,?,?,?,?,?,?,?,?,?,?)",(id,n,dob,de,b,gp,l,doa,e,dpt,ano))
    con.commit()
    con.close()

def insert_value2(id,rel,fname,fdob,fad):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("INSERT INTO famdata2 VALUES(NULL,?,?,?,?,?)",(id,rel,fname,fdob,fad))
    con.commit()
    con.close()

def insert_value3(id,ano,pp):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("INSERT INTO pbal VALUES(?,?,?,?,?)",(id,ano,4,pp,1))
    con.commit()
    con.close()

def insert_value4(id,ano,top,fc,tc,vc,toj,rc,nt,dj,dv,com):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("INSERT INTO travel_data5 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(id,ano,top,fc,tc,vc,toj,rc,nt,dj,dv,com,current_year))
    con.commit()
    con.close()

def insert_value5(id,ano,pto,pp):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("INSERT INTO cfpbal VALUES(?,?,?,?)",(id,ano,pto,pp))
    con.commit()
    con.close()

def insert_value6(pwd1):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("INSERT INTO pwd VALUES(NULL,?)",(pwd1,))
    con.commit()
    con.close()


def update_pw(pw):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("UPDATE pwd SET pass=? WHERE num=?",(pw,1))
    con.commit()
    con.close()


def getpwd():
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("SELECT pass FROM pwd WHERE num=?",(1,))
    r = cur.fetchall()
    con.close()
    if (len(r)==0):
        insert_value6("password123")
        return getpwd()
    else:
        return r[0][0]


def update_cfpbal(pto,pp,id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("UPDATE cfpbal SET cfpto_bal=?,cfpp_bal=? WHERE emp_id=?",(pto,pp,id))
    con.commit()
    con.close()

def view1():
        con=sqlite3.connect("employeedata.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM empdata")
        r = cur.fetchall()
        con.close()
        return r

def view2():
        con=sqlite3.connect("employeedata.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM famdata2")
        r = cur.fetchall()
        con.close()
        return r

def view3():
        con=sqlite3.connect("employeedata.db")
        cur=con.cursor()
        cur.execute("SELECT emp_id,aadhar,pto_bal,pp_bal FROM pbal")
        r = cur.fetchall()
        con.close()
        return r

def view4():
        con=sqlite3.connect("employeedata.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM travel_data5")
        r = cur.fetchall()
        con.close()
        return r

def view5():
        con=sqlite3.connect("employeedata.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM cfpbal")
        r = cur.fetchall()
        con.close()
        return r

def viewfam(id):
        con=sqlite3.connect("employeedata.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM famdata2 WHERE emp_id=?",(id,))
        r = cur.fetchall()
        con.close()
        return r

def viewemp(id):
        con=sqlite3.connect("employeedata.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM empdata WHERE emp_id=?",(id,))
        r = cur.fetchall()
        con.close()
        return r

def officeremp():
        con=sqlite3.connect("employeedata.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM empdata WHERE grade_pay>=5000")
        r = cur.fetchall()
        con.close()
        return r

def nonofficeremp():
        con=sqlite3.connect("employeedata.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM empdata WHERE grade_pay <5000")
        r = cur.fetchall()
        con.close()
        return r


def traveldata(id):
        con=sqlite3.connect("employeedata.db")
        cur=con.cursor()
        cur.execute("SELECT top,f_city,to_city,via_city,TOJ,route_city,num_tickets,DOJ,comment FROM travel_data5 WHERE emp_id=?",(id,))
        r = cur.fetchall()
        con.close()
        return r


def checkid(id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM empdata WHERE emp_id=?",(id,))
    r = cur.fetchall()
    con.close()
    #print(len(r))
    if (len(r)==0):
        return id #do not exist
    else:
        return "id no already exist"


def checkad(ano):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM empdata WHERE aadhar=?",(ano,))
    r = cur.fetchall()
    con.close()
    #print(r)
    if (len(r)==0):
        return ano #do not exist
    else:
        return "id no already exist"


def delete_mem(mid):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("DELETE FROM famdata2 WHERE num=?",(mid,))
    con.commit()
    con.close()

def delete_emp(id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("DELETE FROM empdata WHERE emp_id=?",(id,))
    cur.execute("DELETE FROM famdata2 WHERE emp_id=?",(id,))
    cur.execute("DELETE FROM pbal WHERE emp_id=?",(id,))
    cur.execute("DELETE FROM travel_data5 WHERE emp_id=?",(id,))
    cur.execute("DELETE FROM cfpbal WHERE emp_id=?",(id,))
    con.commit()
    con.close()


def update_det(id,n,dob,de,b,gp,l,doa,e,dpt,ano):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("UPDATE empdata SET name=?,DOB=?,designation=?,Basic=?,Grade_pay=?,Level=?,DOA=?,Entitlement=?,department=?,aadhar=? WHERE emp_id=?",(n,dob,de,b,gp,l,doa,e,dpt,ano,id))
    cur.execute("UPDATE pbal SET aadhar=? WHERE emp_id=?",(ano,id))
    con.commit()
    con.close()

def getaadhaar(id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("SELECT aadhar FROM pbal WHERE emp_id=?",(id,))
    r = cur.fetchall()
    con.close()
    if (len(r)==0):
        return "no aadhar exists" #do not exist
    else:
        return r


def getdoa(id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("SELECT DOA FROM empdata WHERE emp_id=?",(id,))
    r = cur.fetchall()
    con.close()
    return r

def getpto(id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("SELECT pto_bal FROM pbal WHERE emp_id=?",(id,))
    r = cur.fetchall()
    con.close()
    return r

def getpp(id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("SELECT pp_bal FROM pbal WHERE emp_id=?",(id,))
    r = cur.fetchall()
    con.close()
    return r

def getcount(id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("SELECT counter FROM pbal WHERE emp_id=?",(id,))
    r = cur.fetchall()
    con.close()
    return r



def getcfpto(id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("SELECT cfpto_bal FROM cfpbal WHERE emp_id=?",(id,))
    r = cur.fetchall()
    con.close()
    return r

def getcfpp(id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("SELECT cfpp_bal FROM cfpbal WHERE emp_id=?",(id,))
    r = cur.fetchall()
    con.close()
    return r


def update_pto(val,id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("UPDATE pbal SET pto_bal=? WHERE emp_id=?",(val,id))
    con.commit()
    con.close()

def update_pp(val,id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("UPDATE pbal SET pp_bal=? WHERE emp_id=?",(val,id))
    con.commit()
    con.close()

def update_count(id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("UPDATE pbal SET counter=? WHERE emp_id=?",(0,id))
    con.commit()
    con.close()

def update_cfpto(val,id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("UPDATE cfpbal SET cfpto_bal=? WHERE emp_id=?",(val,id))
    con.commit()
    con.close()

def update_cfpp(val,id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("UPDATE cfpbal SET cfpp_bal=? WHERE emp_id=?",(val,id))
    con.commit()
    con.close()

def updatecf():
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("UPDATE cfpbal SET cfpto_bal=? ,cfpp_bal=?",(0.0,0.0))
    con.commit()
    con.close()


def return_pbal():
        con=sqlite3.connect("employeedata.db")
        cur=con.cursor()
        cur.execute("SELECT emp_id,aadhar,pto_bal,pp_bal FROM pbal ")
        r = cur.fetchall()
        con.close()
        return r

def checkcfid(id):
    con=sqlite3.connect("employeedata.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM cfpbal WHERE emp_id=?",(id,))
    r = cur.fetchall()
    con.close()
    #print(len(r))
    if (len(r)==0):
        return id #do not exist
    else:
        return "id no already exist"


def setid(id,ad):
    global e_id
    global a_id
    e_id=id
    a_id=ad

def geteid():
    return e_id
def getaid():
    return a_id

create_table()
#insert_value1(11878715,"testerrr22",'10-01-1990',"clerk12",554.9,1667,5,'11-10-2005','sleeper',3)
#insert_value2(11315,"wife","amita kumari",'1-1-1991')
#insert_value2(11315,"DAUGHTER","amitI kumarI",'1-11-1999')
#update_det(1506100,"b sahu",'10-01-1990',"clerk12",554.9,1667,5,'11-10-2005','sleeper',3)

#update_mem(2,"WIFE","AMISHA KUMAR",'9-9-1999')
#print(view5())
#insert_value3(12345,9876543211234567,6)
#print(checkad(99887766))
#print(checkcfid(1506100))
#setid(11111,99999)
#insert_value4(1506108,1957,)
