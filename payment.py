from  tkinter import *
from PIL import ImageTk, Image
import clickonseat
import datetime
import time
import ticket_f
from tkinter import messagebox

tim = time.strftime("%H:%M")
x = datetime.datetime.now()

def pay_s1(seat,name):
    global e1
    global e5

    def c1(event):
        e1.delete(0,END)
        e1.configure(fg="black")
    def c2(event):
        e2.delete(0,END)
        e2.configure(fg="black") 
    def c3(event):
        e3.delete(0,END)
        e3.configure(fg="black")
    def c4(event):
        e4.delete(0,END)
        e4.configure(fg="black")
    def c5(event):
        e5.delete(0,END)
        e5.configure(fg="black")   
    
    def my_func():
        cn=e1.get()
        cvv=e5.get()
        if len(str(cn))==6:
            if len(str(cvv))==3:
                messagebox.showinfo("PAYMENT", "Payment Sucessfully")
                pay1.destroy()
                ticket_f.ticket(name,seat,x.strftime("%x"),tim)
            else:
                messagebox.showerror("INVALID", "Invalid CVV Number")

        else:
            messagebox.showerror("INVALID", "Invalid Card Number")

    pay1=Tk()
    pay1.geometry("505x300")
    pay1.iconbitmap(default='image/dragon.ico')
    pay1.configure(bg='#D6D5D5')
    pay1.title("Credit/Debit Card")
    l=Label(pay1,text="Card Number",font=("Candara Light",15),fg="#696969",bg='#D6D5D5')
    l.place(x=60,y=30)
    e1 = Entry(pay1, width=25,font=("Bahnschrift Light SemiCondensed",16),fg="#C4C4C4")
    e1.insert(0,"Enter Last 6 Numbers")
    e1.place(x=60,y=60)
    e1.bind("<FocusIn>", c1)
    e2 = Entry(pay1, width=25,font=("Bahnschrift Light SemiCondensed",16),fg="#C4C4C4")
    e2.place(x=60,y=110)
    e2.insert(0,"Name on the Card")
    e2.bind("<FocusIn>", c2)
    Label(pay1,text="Expiry",font=("Candara Light",15),fg="#696969",bg='#D6D5D5').place(x=60,y=150)
    Label(pay1,text="CVV",font=("Candara Light",15),fg="#696969",bg='#D6D5D5').place(x=210,y=150)
    e3=Entry(pay1, width=4,font=("Bahnschrift Light SemiCondensed",16),fg="#C4C4C4")
    e3.place(x=60,y=180)
    e3.insert(0, "MM")
    e3.bind("<FocusIn>", c3)
    e4=Entry(pay1, width=4,font=("Bahnschrift Light SemiCondensed",16),fg="#C4C4C4")
    e4.place(x=120,y=180)
    e4.insert(0, "YY")
    e4.bind("<FocusIn>", c4)
    e5=Entry(pay1, width=8,font=("Bahnschrift Light SemiCondensed",16),fg="#C4C4C4")
    e5.place(x=210,y=180)
    e5.insert(0, "CVV ")
    e5.bind("<FocusIn>", c5)
    Button(pay1,text="Pay",font=("Arial",16),command=my_func).place(x=350,y=230)
    pay1.mainloop()

def pay_s(seat,name,uname):

    def tick():
        pay.destroy()
        pay_s1(seat,name)
    def back():
        pay.destroy()
        clickonseat.arr=[]
        clickonseat.seat(name,uname)
        
    #print(seat)
    pay=Tk()
    pay.geometry("550x500")
    pay.iconbitmap(default='image/dragon.ico')
    pay.title("MAKE PAYMENT")

    Label(pay,text="Payment Gateway",font=("Goudy Old Style",20),fg="#050505").place(x=180,y=20)
    Label(pay,text="Per Seat",font=(10),fg="#423F3F").place(x=50,y=120)
    Label(pay,text="No.of.Seats",font=(10),fg="#423F3F").place(x=50,y=180)
    Label(pay,text="Amount to be Paid",font=(10),fg="#423F3F").place(x=50,y=240)
    Label(pay,text="200 ₹",font=(10),fg="black").place(x=390,y=120)
    Label(pay,text=len(seat),font=(10),fg="black").place(x=390,y=180)
    Label(pay,text=str(len(seat)*200)+" ₹",font=(10),fg="black",bg="white").place(x=390,y=240)
    img = ImageTk.PhotoImage(Image.open("image/back.jpg"))
    Label(pay,text="(inclusive of all taxes)",fg="#82C967").place(x=370,y=270)
    Label(pay,text="Refunds will be done according to Cancellation Policy.",fg="gray").place(x=125,y=470)
    Button(pay,text="PROCEED",font=("Calibri"),padx=10,command=tick).place(x=370,y=350)
    Button(pay,image=img,borderwidth=1,command=back).place(x=10,y=10) 
    pay.mainloop()

