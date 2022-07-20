from tkinter import *
from PIL import ImageTk, Image
import datetime
import time

def ticket(mo,se,da,ti):

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

    if mo=="AVATAR":
        Label(r_ticket,text="1",font=(" Goudy Old Style",22),fg="#BF3424",bg="#f5e8c5",padx=10,pady=10).place(x=700,y=305)
    elif mo=="INCEPTION":
        Label(r_ticket,text="2",font=(" Goudy Old Style",22),fg="#BF3424",bg="#f5e8c5",padx=10,pady=10).place(x=700,y=305)
    elif mo=="JOHN_WICK":
        Label(r_ticket,text="3",font=(" Goudy Old Style",22),fg="#BF3424",bg="#f5e8c5",padx=10,pady=10).place(x=700,y=305)
    elif mo=="MALEFICENT":
        Label(r_ticket,text="4",font=(" Goudy Old Style",22),fg="#BF3424",bg="#f5e8c5",padx=10,pady=10).place(x=700,y=305)

    r_ticket.mainloop()
