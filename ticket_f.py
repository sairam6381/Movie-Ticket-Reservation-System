from tkinter import *
from PIL import ImageTk, Image
import datetime
import time

named_tuple = time.localtime() # get struct_time
tim = time.strftime("%H:%M")
#print(tim)
x = datetime.datetime.now()
#print(x.strftime("%x"))
#print(x.strftime("%X"))



def ticket(mo,se,da,ti):
    #print(da,ti)
        
    r_ticket=Tk()
    r_ticket.geometry("850x450")
    r_ticket.iconbitmap(default='image/dragon.ico')
    r_ticket.title("TICKET")
    img = ImageTk.PhotoImage(Image.open("image/ticket.png"))  
    l=Label(r_ticket,image=img)
    l.place(x=0,y=0,relwidth=1,relheight=1)
    r_ticket.wm_attributes('-transparentcolor', '#ab23ff')

    Label(r_ticket,text=mo,font=(" courier",22),fg="#76787E",bg="#f5e8c5").place(x=400,y=133)
    Label(r_ticket,text=se,font=(" Goudy Old Style",22),fg="#76787E",bg="#f5e8c5").place(x=390,y=195)
    Label(r_ticket,text=da,font=(" Goudy Old Style",22),fg="#76787E",bg="#f5e8c5").place(x=385,y=310)
    Label(r_ticket,text=ti,font=(" Goudy Old Style",22),fg="#76787E",bg="#f5e8c5").place(x=535,y=310)


    r_ticket.mainloop()

#a=["A1","A2","sai"]
#ticket("AVATHAR",a,x.strftime("%x"),tim)