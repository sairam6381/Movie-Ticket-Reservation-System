from  tkinter import *
from PIL import ImageTk, Image
import clickonseat
import datetime
import time
import ticket_f
from tkinter import messagebox
#named_tuple = time.localtime() # get struct_time
tim = time.strftime("%H:%M")
x = datetime.datetime.now()
"You can cancel the tickets 20 min(s) before the show. Refunds will be done according to Cancellation Policy"



def pay_s(seat,name):
    def tick():
        messagebox.showinfo("PAYMENT", "Payment Sucessfully")
        pay.destroy()
        ticket_f.ticket(name,seat,x.strftime("%x"),tim)

    def back():
        pay.destroy()
        clickonseat.arr=[]
        clickonseat.seat(name)
        
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

    Button(pay,text="PAY",font=("Calibri"),padx=10,command=tick).place(x=370,y=350)
    Button(pay,image=img,borderwidth=1,command=back).place(x=10,y=10)


    
    pay.mainloop()

    

#pay_s(10)
    
