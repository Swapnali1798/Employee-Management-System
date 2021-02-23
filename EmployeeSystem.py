from tkinter import *
import mysql.connector
from tkinter import messagebox,ttk

root=Tk()
root.geometry("1500x700")
root.resizable(False,False)
root.title("EMPLOYEE MANAGEMENT SYSTEM")

#global connection to database for multiuses
conn= mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database='employee'
        )
print(conn)
cursor = conn.cursor()
                               # The raise keyword is used to raise an exception.
                               # You can define what kind of error to raise, and the text to print to the user.
def raise_frame(frame):
    if frame=="Signup":
        name1=name.get()
        password1=password.get()
        query = 'insert into users(name,password) values(%s,%s)'
        values = (name1, password1)
        cursor.execute(query, values)
        conn.commit()
        print(cursor.rowcount, 'rows inserted.')
        Frame.tkraise(for_frame)

    elif frame=="register":
        Frame.tkraise(thi_frame)

    elif frame=="Login":
        currentUser = lname.get()
        currentpassword = lpassword.get()
        count=0
        flag="false"

        Query = "select * from users"
        cursor.execute(Query)
        records = cursor.fetchall()
        print("Total number of users : ", cursor.rowcount)

        for row in records:
            if currentUser == row[0] and currentpassword == row[1]:
                Frame.tkraise(fif_frame)
                flag = "true"
                break
            else:
                count = count + 1

        if count > 0 and flag == "false":
            messagebox.showinfo("LOGIN FAILED", "USERNAME OR PASSWORD SHOULD BE WRONG?")

    elif frame=="fir_frame":
        Frame.tkraise(fir_frame)
    elif frame == "sec_frame":
        Frame.tkraise(sec_frame)
    elif frame == "thi_frame":
        Frame.tkraise(thi_frame)
    elif frame == "for_frame":
        Frame.tkraise(for_frame)
    elif frame == "fif_frame":
        Frame.tkraise(fif_frame)
    elif frame=="six_frame1":
        Query = "select * from emp1"
        cursor.execute(Query)
        records = cursor.fetchall()
        print("Total number of users : ", cursor.rowcount)

        for i in table.get_children():
            table.delete(i)
        for row in records:
                table.insert('', 'end', values=row)

        Frame.tkraise(six_frame)

    elif frame == "sev_frame":
        Frame.tkraise(sev_frame)
    elif frame == "eig_frame":
        Frame.tkraise(eig_frame)
    elif frame == "nin_frame":
        Frame.tkraise(nin_frame)
    elif frame == "ten_frame":
        Frame.tkraise(ten_frame)
    elif frame == "add_employee":
        eid = e_id.get()
        ename = e_name.get()
        eaddress = e_address.get()
        emob = e_mob.get()
        esal = e_sal.get()

        query = 'insert into emp1(id,name,address,mobile,salary) values(%s,%s,%s,%s,%s)'
        values = (eid,ename,eaddress,emob,esal)
        cursor.execute(query, values)
        conn.commit()
        print(cursor.rowcount, 'rows inserted.')
        messagebox.showinfo("Info", "Employee Successfully Added")
        Frame.tkraise(sev_frame)

    elif frame == "delete_employee":
        delete_id=del_id.get()
        query="delete from emp1 WHERE id='{temp}'".format(temp=delete_id)
        cursor.execute(query)
        messagebox.showinfo("Info", "Employee Successfully Deleted")
        Frame.tkraise(ten_frame)

    elif frame == "search":
        searchid = search_id.get()
        query = "select * from emp1 WHERE id='{temp}'".format(temp=searchid)
        cursor.execute(query)

        records2 = cursor.fetchall()
        for row2 in records2:
            table1.insert('', 'end', values=row2)
        Frame.tkraise(eig_frame)

    elif frame == "update":
        updateid = update_id.get()
        updateaddress = update_address.get()
        updatemob = update_mob.get()
        updatesal = update_sal.get()

        query = "update emp1 set address='{u1}',mobile='{u2}',salary='{u3}' WHERE id='{u4}'".format(u1=updateaddress,u2=updatemob,u3=updatesal,u4=updateid)
        cursor.execute(query)
        messagebox.showinfo("Info", "Employee Record Successfully Updated")
        Frame.tkraise(nin_frame)

# Frames************************************************************************************
# second frame
sec_frame=Frame(root,bg="green")
sec_frame.place(x=0, y=0, width=1500, height=500)
# third frame
thi_frame=Frame(root,bg="green")
thi_frame.place(x=0, y=0, width=1500, height=500)
# forth frame
for_frame=Frame(root,bg="pink")
for_frame.place(x=0, y=0, width=1500, height=500)
# fifth frame
fif_frame=Frame(root,bg="sky blue")
fif_frame.place(x=0,y=0,width=1500,height=500)
# sixth frame
six_frame=Frame(root,bg="sky blue")
six_frame.place(x=0,y=0,width=1500,height=500)
# seventh frame
sev_frame=Frame(root,bg="sky blue")
sev_frame.place(x=0,y=0,width=1500,height=500)
 # eighth frame
eig_frame=Frame(root,bg="sky blue")
eig_frame.place(x=0,y=0,width=1500,height=500)
 # nineth frame
nin_frame=Frame(root,bg="sky blue")
nin_frame.place(x=0,y=0,width=1500,height=500)
 # tenth frame
ten_frame=Frame(root,bg="sky blue")
ten_frame.place(x=0,y=0,width=1500,height=500)
# first frame
fir_frame=Frame(root,bg="pink")
fir_frame.place(x=0,y=0,width=1500,height=500)

# GUI**********************************************************************************************
# first frame
lb=Label(fir_frame,text="Welcome To Employee Management System ",bg="green",fg="yellow",font=("bold",25))
lb.place(x=50,y=30)
# login btn
b1=Button(fir_frame,borderwidth=3, bd=3,text='Login',font=("bold",16),width=10, bg='brown', fg='white', command=lambda: raise_frame("sec_frame"))
b1.place(x=80,y=120)
#registration btn
b2=Button(fir_frame,borderwidth=3, bd=3,font=("bold",16),text="Register",width=10, bg='brown', fg='white', command=lambda: raise_frame("thi_frame"))
b2.place(x=80,y=170)

lb0=Label(fir_frame,text="Create new account",bg="blue",fg="white")
lb0.place(x=90,y=220)

# second frame**********login********************************************************
lb1=Label(sec_frame,bg="yellow",text="*Please Enter Details Below to Login*",font=("bold",25))
lb1.place(x=20,y=20)

lb2=Label(sec_frame,text="Username:",fg="black",bg="pink",width=12,font=("bold",16))
lb2.place(x=40,y=120)
lname=StringVar()
e1=Entry(sec_frame,textvariable=lname,bd=3,borderwidth=3,width=20,font=("bold",12))
e1.place(x=200,y=120)

lb3=Label(sec_frame,text="Password:",fg="black",bg="pink",width=12,font=("bold",16))
lb3.place(x=40,y=180)
lpassword=StringVar()
e2=Entry(sec_frame,textvariable=lpassword,bd=3,borderwidth=3,width=20,show='*',font=("bold",12))
e2.place(x=200,y=180)

b3=Button(sec_frame,text="Login",width=10, bg='brown',font=("bold",12), fg='white',command=lambda: raise_frame("Login"))
b3.place(x=150,y=250)

# third frame*****************registration************************************************88

lb4=Label(thi_frame,bg="yellow",text="*Please Enter Details Below to Register*",font=("bold",25))
lb4.place(x=20,y=20)
lb5=Label(thi_frame,text="Username:",fg="black",bg="pink",width=12,font=("bold",16))
lb5.place(x=40,y=120)
name=StringVar()
e3=Entry(thi_frame,textvariable=name,bd=3,borderwidth=3,width=20,font=("bold",12))
e3.place(x=200,y=120)

lb6=Label(thi_frame,text="Password:",fg="black",bg="pink",width=12,font=("bold",16))
lb6.place(x=40,y=180)

password=StringVar()
e4=Entry(thi_frame,textvariable=password,bd=3,borderwidth=3,width=20,show='*',font=("bold",12))
e4.place(x=200,y=180)

b4=Button(thi_frame,text="Register",width=10, bg='brown',font=("bold",12), fg='white',command=lambda: raise_frame("Signup"))
b4.place(x=150,y=250)

# forth frame
lb7=Label(for_frame,text="Thank You!!! Registered Successfully",fg='blue',font=("arial",25,"bold"))
lb7.place(x=30,y=100)

b5=Button(for_frame,text="Back",fg='white',bg='brown',width=12,font=("arial",16),command=lambda: raise_frame("fir_frame"))
b5.place(x=150,y=150)

lb8=Label(for_frame,text="Back to login page",fg='blue')
lb8.place(x=180,y=200)

# fifth frame
lb9=Label(fif_frame,text="Employee management System",bg="red",font=("bold",25))
lb9.place(x=40,y=30)
lf1 = LabelFrame(fif_frame, text="Employee Information",bg="yellow", width=300, height=50)
lf1.pack(fill="both"  ,side="left", padx=100, pady=100)

Button(lf1, text="Show All Employee", bg="white",font=("bold",12),command=lambda: raise_frame("six_frame1")).place(x=1, y=10)

Button(lf1, text="Add Employee", bg="red",font=("bold",12),command=lambda: raise_frame("sev_frame")).place(x=1, y=50)

Button(lf1, text="Search Employee",bg="blue",font=("bold",12),command=lambda: raise_frame("eig_frame")).place(x=1, y=90)

Button(lf1, text="Update Employee",bg="pink",font=("bold",12),command=lambda: raise_frame("nin_frame")).place(x=1, y=130)

Button(lf1, text="Delete Employee",bg="orange",font=("bold",12),command=lambda: raise_frame("ten_frame")).place(x=1, y=170)

Button(lf1, text="Back",bg="green",font=("bold",12),command=lambda: raise_frame("fir_frame")).place(x=1, y=210)

Button(lf1, text="Logout",bg="white",font=("bold",12),command=quit).place(x=1, y=250)

# sixth frame
# A tree view represents a hierarchical view of information, where each item can have a number of subitems
table=ttk.Treeview( six_frame, columns=(1,2,3,4,5), show="headings", height=15 )
table.place(x=100,y=100)

table.heading(1,text="Employee Id")
table.heading(2,text="Name")
table.heading(3,text="Address")
table.heading(4,text="Mobile No")
table.heading(5,text="Salary")

Button(six_frame, text="Back",bg="yellow",font=("bold",12),command=lambda: raise_frame("fif_frame")).place(x=10, y=200)
Button(six_frame, text="Quit",bg="yellow",font=("bold",12),command=quit).place(x=10, y=260)

# sevnth frame
e_id=StringVar()
e_name=StringVar()
e_address=StringVar()
e_mob=StringVar()
e_sal=StringVar()
lf3 = LabelFrame(sev_frame, text="Add Employee",bg="sky blue", width=300, height=10)
lf3.pack(fill="both"  ,side="left", padx=100, pady=100)
Label(lf3, text="Employee Id :",font=("arial",12),bg="red").place(x=1, y=20)
Entry(lf3,bd=3,borderwidth=3,width=25,textvariable=e_id).place(x=130, y=20)
Label(lf3, text="Employee Name:",font=("arial",12),bg="orange").place(x=1, y=60)
Entry(lf3,bd=3,borderwidth=3,width=25,textvariable=e_name).place(x=130, y=60)
Label(lf3, text="Address :",font=("arial",12),bg="pink").place(x=1, y=100)
Entry(lf3,bd=3,borderwidth=3,width=25,textvariable=e_address).place(x=130, y=100)
Label(lf3, text="Mobile no :",font=("arial",12),bg="blue").place(x=1, y=140)
Entry(lf3,bd=3,borderwidth=3,width=25,textvariable=e_mob).place(x=130, y=140)
Label(lf3, text="Salary :",font=("arial",12),bg="white").place(x=1, y=180)
Entry(lf3,bd=3,borderwidth=3,width=25,textvariable=e_sal).place(x=130, y=180)

Button(lf3,text="Add Employee",bg="yellow",width=12,bd=2,borderwidth=2,font=("bold",12),command=lambda: raise_frame("add_employee"))\
    .place(x=80,y=240)

Button(lf3, text="Back",bg="green",font=("bold",12),command=lambda: raise_frame("fif_frame")).place(x=10, y=240)

Button(lf3, text="Quit",bg="red",font=("bold",12),command=quit).place(x=220, y=240)

# eightframe
table1=ttk.Treeview( eig_frame, columns=(1,2,3,4,5), show="headings",height=15 )
table1.place(x=330,y=100)

table1.heading(1,text="Employee Id")
table1.heading(2,text="Name")
table1.heading(3,text="Address")
table1.heading(4,text="Mobile No")
table1.heading(5,text="Salary")

search_id=StringVar()
lf4 = LabelFrame(eig_frame, text="Search Employee",bg="sky blue", width=300, height=50)
lf4.pack(fill="both"  ,side="left", padx=10, pady=100)
Label(lf4, text="Employee Id :",bg="orange",font=("arial",12)).place(x=1, y=20)
Entry(lf4,bd=3,borderwidth=3,width=25,textvariable=search_id).place(x=130, y=20)

Button(lf4,text="Search Employee",bg="yellow",width=15,bd=2,borderwidth=2,font=("bold",12),command=lambda: raise_frame("search")).place(x=70,y=60)

Button(lf4, text="Back",bg="green",font=("bold",12),command=lambda: raise_frame("fif_frame")).place(x=30, y=220)
Button(lf4, text="Quit",bg="red",font=("bold",12),command=quit).place(x=200, y=220)

# ninethframe
update_id=StringVar()
update_address=StringVar()
update_mob=StringVar()
update_sal=StringVar()
lf5 = LabelFrame(nin_frame, text="Update Employee",bg="sky blue", width=300, height=50)
lf5.pack(fill="both"  ,side="left", padx=100, pady=100)
Label(lf5, text="Employee Id :",font=("arial",12),bg="pink").place(x=1, y=20)
Entry(lf5,bd=3,borderwidth=3,width=25,textvariable=update_id).place(x=130, y=20)
Label(lf5, text="*Enter new data*",font=("bold",8),bg="white").place(x=1, y=60)
Label(lf5, text="Address :",font=("arial",12),bg="red").place(x=1, y=100)
Entry(lf5,bd=3,borderwidth=3,width=25,textvariable=update_address).place(x=130, y=100)
Label(lf5, text="mobile no :",font=("arial",12),bg="blue").place(x=1, y=140)
Entry(lf5,bd=3,borderwidth=3,width=25,textvariable=update_mob).place(x=130, y=140)
Label(lf5, text="Salary :",font=("arial",12),bg="orange").place(x=1, y=180)
Entry(lf5,bd=3,borderwidth=3,width=25,textvariable=update_sal).place(x=130, y=180)

Button(lf5,text="Update Employee",bg="yellow",width=15,bd=2,borderwidth=2,font=("bold",12),command=lambda: raise_frame("update")).place(x=70,y=220)

Button(lf5, text="Back",bg="green",font=("bold",12),command=lambda: raise_frame("fif_frame")).place(x=10, y=220)
Button(lf5, text="Quit",bg="red",font=("bold",12),command=quit).place(x=230, y=220)

# tenthframe
del_id=StringVar()
lf5 = LabelFrame(ten_frame, text="Delete Employee",bg="sky blue", width=300, height=50)
lf5.pack(fill="both"  ,side="left", padx=100, pady=100)
Label(lf5, text="Employee Id :",font=("arial",12),bg="pink").place(x=1, y=20)
Entry(lf5,bd=3,borderwidth=3,width=25,textvariable=del_id).place(x=130, y=20)

Button(lf5,text="Delete Employee",bg="yellow",width=15,bd=2,borderwidth=2,font=("bold",12),command=lambda: raise_frame("delete_employee")).place(x=70,y=60)

Button(lf5, text="Back",bg="green",font=("bold",12),command=lambda: raise_frame("fif_frame")).place(x=30, y=220)

Button(lf5, text="Quit",bg="red",font=("bold",12),command=quit).place(x=200, y=220)

root.mainloop()