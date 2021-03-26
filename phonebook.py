from Tkinter import *
import sqlite3
from main_function import *
root=Tk()
root.geometry("1200x1200")
root.configure(background='white')
w1=Label(root,text=' Phonebook Project ', bg='white',fg='black',font="Times 25 italic")
w1.grid(row=0,column=0,columnspan=2,rowspan=2)
w0=Label(root,text=' Pyhton and Database Project ',bg='white',fg='red',font="Times 35 italic underline")
w0.grid(row=5,column=2)
w2=Label(root,text=' Developed By: Chaitanya Kaul ',bg='white',fg='red',font="Times 25 italic")
w2.grid(row=6,column=2)
w3=Label(root,text=' Enrollment No: 181B073 ', bg='white',fg='black',font="Times 25 italic")
w3.grid(row=7,column=2)
w4=Label(root,text=' Batch: B3 ', bg='white',fg='red',font="Times 25 italic")
w4.grid(row=8,column=2)
def stop(e=1):
    root.destroy()
    main_program()
    
root.bind('<Motion>',stop)
root.mainloop()
