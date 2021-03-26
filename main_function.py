from Tkinter import *
import tkMessageBox
import sqlite3
cur=0
con=0
def main_program():
    root=Tk()
    root.geometry("1200x800")
    root.configure(background="#728C00")
    v=StringVar()
    x=StringVar()
    con=sqlite3.Connection('phone_book.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE if not exists RECORD(F_NAME VARCHAR(100) DEFAULT NULL,M_NAME VARCHAR(100) DEFAULT NULL,L_NAME VARCHAR(100) DEFAULT NULL,C_NAME VARCHAR(100) DEFAULT NULL,ADDRESS VARCHAR(100) DEFAULT NULL,CITY VARCHAR(100) DEFAULT NULL,PIN NUMBER(25) DEFAULT NULL,WEB VARCHAR(100) DEFAULT NULL,DOB DATE DEFAULT NULL,P_TYPE VARCHAR(100) DEFAULT NULL,P_NO NUMBER(100) DEFAULT NULL,E_TYPE VARCHAR(100) DEFAULT NULL,EMAIL VARCHAR(100) DEFAULT NULL)")
    Label(root,text="Welcome to phone book",font="Times 25 italic",bg="#E9967A").grid(row=0,column=0)
    a=PhotoImage(file="phone.gif")
    a=a.subsample(4,4)
    Label(root,image=a,bg="#1A008C",bd=3).grid(row=1,column=1,columnspan=10)
    Label(root,text="First Name",bg="#728C00",font=20).grid(row=2,column=1,)
    Label(root,text="Middle Name",bg="#728C00",font=20).grid(row=3,column=1)
    Label(root,text="Last Name",bg="#728C00",font=20).grid(row=4,column=1)
    Label(root,text="Company Name",bg="#728C00",font=20).grid(row=5,column=1)
    Label(root,text="Address",bg="#728C00",font=20).grid(row=6,column=1)
    Label(root,text="City",bg="#728C00",font=20).grid(row=7,column=1)
    Label(root,text="Pin-Code",bg="#728C00",font=20).grid(row=8,column=1)
    Label(root,text="Website URL",bg="#728C00",font=20).grid(row=9,column=1)
    Label(root,text="Birth",bg="#728C00",font=20).grid(row=10,column=1)
    Label(root,text="Select Phone Type",fg="THISTLE",bg="#728C00",font=20).grid(row=11,column=1)
    Radiobutton(root,text="Office",bg="#728C00",variable=v,value="Office",tristatevalue=0,font=15).grid(row=11,column=7)
    Radiobutton(root,text="Home",bg="#728C00",variable=v,value="Home",tristatevalue=0,font=15).grid(row=11,column=8)
    Radiobutton(root,text="Mobile",bg="#728C00",variable=v,value="Mobile",tristatevalue=0,font=15).grid(row=11,column=9)
    Label(root,text="Phone",bg="#728C00",font=20).grid(row=12,column=1)
    Label(root,text="Select Email Type ",bg="#728C00",fg="THISTLE",font=20).grid(row=13,column=1)
    Radiobutton(root,text="Office",bg="#728C00",variable=x,value="Office",tristatevalue=0,font=15).grid(row=13,column=7)
    Radiobutton(root,text="Personal",bg="#728C00",variable=x,value="Personal",tristatevalue=0,font=15).grid(row=13,column=8)
    Label(root,text="Email id ",bg="#728C00",font=20).grid(row=14,column=1)
    e1=Entry(root,bd=3)
    e1.grid(row=2,column=8)
    e2=Entry(root,bd=3)
    e2.grid(row=3,column=8)
    e3=Entry(root,bd=3)
    e3.grid(row=4,column=8)
    e4=Entry(root,bd=3)
    e4.grid(row=5,column=8)
    e5=Entry(root,bd=3)
    e5.grid(row=6,column=8)
    e6=Entry(root,bd=3)
    e6.grid(row=7,column=8)
    e7=Entry(root,bd=3)
    e7.grid(row=8,column=8)
    e8=Entry(root,bd=3)
    e8.grid(row=9,column=8)
    e9=Entry(root,bd=3)
    e9.grid(row=10,column=8)
    e10=Entry(root,bd=3)
    e10.grid(row=12,column=8)
    e11=Entry(root,bd=3)
    e11.grid(row=14,column=8)

    def insert():

        a,b,c,d,e,f,g,h,i,j,k,l,m=e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),v.get(),e10.get(),x.get(),e11.get()
        t=[1]
        t[0]=[a,b,c,d,e,f,g,h,i,j,k,l,m]
        cur.execute("INSERT INTO RECORD VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",t[0])
        con.commit()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
        tkMessageBox.showinfo("Inserted","Entry Is Sucessfully Entered")
    Button(root,text="Save",command=insert).grid(row=15,column=1)

    
    def search():
        root1=Tk()
        root1.geometry("1200x1200")
        root1.configure(bg="#C76730")
        Label(root1,text="Search Panel",font="Times 22 bold underline",bg="#C76730").grid(row=0,column=0)
        Label(root1,text="Enter The Name",font="Arial 15 bold",bg="#C76730").grid(row=3,column=3)
        e1=Entry(root1,bd=3)
        e1.grid(row=4,column=3)
        lb1=Listbox(root1,bd=3,height=17,width=40,selectmode=SINGLE,bg="#3090C7",font="Arial 18 bold")
        lb1.grid(row=5,column=2,columnspan=3)
        cur.execute("SELECT F_NAME,M_NAME,L_NAME FROM RECORD")
        t=cur.fetchall()
        for i in t:
            lb1.insert(END,i)
        def searching(*args):
            lb1.delete(0,END)
            t=["%"+e1.get()+"%","%"+e1.get()+"%","%"+e1.get()+"%"]
            cur.execute("SELECT F_NAME,M_NAME,L_NAME FROM RECORD WHERE F_NAME LIKE ? OR M_NAME LIKE ? OR L_NAME LIKE ? ",t)
            t=cur.fetchall()
            for i in t:
                lb1.insert(END,i)
        root1.bind('<KeyPress>',searching)
        
        def fetch():
            root2=Tk()
            lb2=Listbox(root2,bd=3,height=17,width=40,font="Arial 14 bold")
            lb2.pack()
            a= lb1.curselection()
            x=lb1.get(a)
            cur .execute("SELECT * FROM RECORD WHERE F_NAME=? AND M_NAME=? AND L_NAME=?",x)
            T=cur.fetchall()
            for i in T:
                print i
                a="F_NAME :  "+i[0]
                lb2.insert(END,a)
                a="M_NAME :  "+i[1]
                lb2.insert(END,a)
                a="L_NAME :  "+i[2]
                lb2.insert(END,a)
                a="COMPANY NAME :  "+i[3]
                lb2.insert(END,a)
                a="ADDRESS :  "+i[4]
                lb2.insert(END,a)
                a="CITY :  "+i[5]
                lb2.insert(END,a)
                x=str(i[6])
                a="PIN-CODE :  "+x
                lb2.insert(END,a)
                a="WEB-SITE :  "+i[7]
                lb2.insert(END,a)
                a="DATE-OF-BIRTH :  "+i[8]
                lb2.insert(END,a)
                a="PHONE NUMBER DETAILS...."
                lb2.insert(END,a)
                x=str(i[10])
                a=i[9]+" : "+x
                lb2.insert(END,a)
                a="EMAIL-ID DETAILS...."
                lb2.insert(END,a)
                a=i[11]+" : "+i[12]
                lb2.insert(END,a)
   
        def close():
             root1.destroy() 
        Button(root1,text="CLOSE",command=close).grid(row=20,column=4)
        def delete():
            try:
                a= lb1.curselection()
                x=lb1.get(a)
                cur .execute("DELETE FROM RECORD WHERE F_NAME=? AND M_NAME=? AND L_NAME=?",x)
                con.commit()
                lb1.delete(0,END)
                e1.delete(0,END)
                cur.execute("SELECT F_NAME,M_NAME,L_NAME FROM RECORD")
                t=cur.fetchall()
                for i in t:
                    lb1.insert(END,i)
            except TclError:
                tkMessageBox.showinfo("Error","Select Some Entry")    
        Button(root1, text="Delete",command=delete).grid(row=20,column=3)
        lb1.bind('<Double-Button-1>', lambda x:fetch())
        Button(root1,text="CLOSE",command=close).grid(row=20,column=4)
    Button(root,text="Search",command=search).grid(row=15,column=3)
    def close():
        root.destroy()
    Button(root,text="Close",command=close).grid(row=15,column=5)


    def edit():
        global cur
        global con
        root3=Tk()
        F=StringVar(root3,"1")
        G=StringVar(root3,"1")
        root3.geometry("1200x1200")
        root3.configure(bg="#C76730")
        Label(root3,text="Welcome To The Edit Panel",font="Times 22 bold underline",bg="#C76730").grid(row=0,column=0)
        Label(root3,text="Enter The Name",font="Arial 15 bold",bg="#C76730").grid(row=3,column=3)
        e1=Entry(root3,bd=3)
        e1.grid(row=4,column=3)
        lb3=Listbox(root3,bd=3,height=17,width=40,selectmode=SINGLE,bg="#3090C7",font="Arial 18 bold")
        lb3.grid(row=5,column=2,columnspan=3)
        cur.execute("SELECT F_NAME,M_NAME,L_NAME FROM RECORD")
        t=cur.fetchall()
        for i in t:
            lb3.insert(END,i)
        def searching(*args):
            lb3.delete(0,END)
            t=["%"+e1.get()+"%","%"+e1.get()+"%","%"+e1.get()+"%"]
            cur.execute("SELECT F_NAME,M_NAME,L_NAME FROM RECORD WHERE F_NAME LIKE ? OR M_NAME LIKE ? OR L_NAME LIKE ? ",t)
            t=cur.fetchall()
            for i in t:
                lb3.insert(END,i)
        root3.bind('<KeyPress>',searching)
        def update():
            global cur
            global con
            root4=Tk()
            root4.geometry("1200x1250")
            Label(root4,text="Welcome To The Edit Panel",fg="BLACK",font="Times 21 bold underline",bg="#E178AE").grid(row=0,column=0)
            root4.title("PhoneBook")
            root4.configure(bg="#3090C7")

            Label(root4,text="First Name",bg="#3090C7",font="Arial 15 bold").grid(row=2,column=1)
            Label(root4,text="Middle Name",bg="#3090C7",font="Arial 15 bold").grid(row=3,column=1)
            Label(root4,text="Last Name",bg="#3090C7",font="Arial 15 bold").grid(row=4,column=1)
            Label(root4,text="Comapany Name",bg="#3090C7",font="Arial 15 bold").grid(row=5,column=1)
            Label(root4,text="Address",bg="#3090C7",font="Arial 15 bold").grid(row=6,column=1)
            Label(root4,text="City",bg="#3090C7",font="Arial 15 bold").grid(row=7,column=1)
            Label(root4,text="Pin-Code",bg="#3090C7",font="Arial 15 bold").grid(row=8,column=1)
            Label(root4,text="Website URL",bg="#3090C7",font="Arial 15 bold").grid(row=9,column=1)
            Label(root4,text="Date Of Birth",bg="#3090C7",font="Arial 15 bold").grid(row=10,column=1)
            Label(root4,text="Select Phone Type",fg="Red",bg="#3090C7",font="Arial 15 bold").grid(row=11,column=1)
            
            Label(root4,text="Phone",bg="#3090C7",font="Arial 15 bold").grid(row=12,column=1)
            Label(root4,text="Select Email Type ",bg="#3090C7",fg="RED",font="Arial 15 bold").grid(row=13,column=1)
            
            Label(root4,text="Email id ",bg="#3090C7",font="Arial 15 bold").grid(row=14,column=1)
            e1=Entry(root4,bd=3)
            e1.grid(row=2,column=3)
            e2=Entry(root4,bd=3)
            e2.grid(row=3,column=3)
            e3=Entry(root4,bd=3)
            e3.grid(row=4,column=3)
            e4=Entry(root4,bd=3)
            e4.grid(row=5,column=3)
            e5=Entry(root4,bd=3)
            e5.grid(row=6,column=3)
            e6=Entry(root4,bd=3)
            e6.grid(row=7,column=3)
            e7=Entry(root4,bd=3)
            e7.grid(row=8,column=3)
            e8=Entry(root4,bd=3)
            e8.grid(row=9,column=3)
            e9=Entry(root4,bd=3)
            e9.grid(row=10,column=3)
            e10=Entry(root4,bd=3)
            e10.grid(row=12,column=3)
            e11=Entry(root4,bd=3)
            e11.grid(row=14,column=3)
            B= lb3.curselection()
            Z=lb3.get(B)
            cur.execute("SELECT * FROM RECORD WHERE F_NAME=? AND M_NAME=? AND L_NAME=?",Z)
            T=cur.fetchall()
            a=[]
            for i in T:
                e1.insert(0,i[0])
                e2.insert(0,i[1])
                e3.insert(0,i[2])
                e4.insert(0,i[3])
                e5.insert(0,i[4])
                e6.insert(0,i[5])
                e7.insert(0,i[6])
                e8.insert(0,i[7])
                e9.insert(0,i[8])
                a=[i[9],i[11]]
                e10.insert(0,i[10])
                e11.insert(0,i[12])
            F=StringVar(root4)
            G=StringVar(root4)
            g1=Radiobutton(root4,text="Office",bg="#0000FF",variable=F,value="Office",tristatevalue=0,font="Arial 10 bold")
            g1.grid(row=11,column=3)
            g1=Radiobutton(root4,text="Home",bg="#0000FF",variable=F,value="Home",tristatevalue=0,font="Arial 10 bold")
            g1.grid(row=11,column=4)
            g1=Radiobutton(root4,text="Mobile",bg="#0000FF",variable=F,value="Mobile",tristatevalue=0,font="Arial 10 bold")
            g1.grid(row=11,column=5)
            g2=Radiobutton(root4,text="Office",bg="#0000FF",variable=G,value="Office",tristatevalue=0,font="Arial 10 bold")
            g2.grid(row=13,column=3)
            g2=Radiobutton(root4,text="Personal",bg="#0000FF",variable=G,value="Personal",tristatevalue=0,font="Arial 10 bold")
            g2.grid(row=13,column=4)
            if(a[0]=="Office"):
                F="Office"
            elif(a[0]=="Home"):
                F="Home"
            elif(a[0]=="Mobile"):
                F="Mobile"
            if(a[1]=="Office"):
                G="Office"
            elif(a[1]=="Personal"):
                G="Personal"
                
            def update():
                global cur
                global con   
                H=[e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),F,e10.get(),G,e11.get(),Z[0],Z[1],Z[2]]
                #cur.execute("UPDATE RECORD SET F_NAME=?,M_NAME=?,L_NAME=?,C_NAME=?,ADDRESS=?,CITY=?,PIN=?,WEB=?,DOB=?,P_TYPE=?,P_NO=?,E_TYPE=?,EMAIL=? WHERE F_NAME=? AND M_NAME=? AND L_NAME=? ",H)
                cur.execute("UPDATE RECORD SET F_NAME=IfNull(?,F_NAME),M_NAME=IfNull(?,M_NAME),L_NAME=IfNull(?,L_NAME),C_NAME=IfNull(?,C_NAME),ADDRESS=IfNull(?,ADDRESS),CITY=IfNull(?,CITY),PIN=IfNull(?,PIN),WEB=IfNull(?,WEB),DOB=IfNull(?,DOB),P_TYPE=IfNull(?,P_TYPE),P_NO=IfNull(?,P_NO),E_TYPE=IfNull(?,E_TYPE),EMAIL=IfNull(?,EMAIL) WHERE F_NAME=? AND M_NAME=? AND L_NAME=? ",H)
                con.commit()
                tkMessageBox.showinfo("Updated","Entry Is Sucessfully Updated")
                root4.destroy()
                tkMessageBox.showinfo("Error","please fill all Entry fields")
            Button(root4,text="SAVE",command=update).grid(row=15,column=3)
        lb3.bind('<Double-Button-1>', lambda x:update())
        def close():
            root3.destroy()
        Button(root3,text="Close",command=close).grid(row=20,column=4)
    Button(root,text="Edit",command=edit).grid(row=15,column=7)
    root.mainloop()
