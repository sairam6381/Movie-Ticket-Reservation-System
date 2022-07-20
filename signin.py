from tkinter import *
import smtplib
from tkinter import messagebox
import database
import home_screen
from PIL import ImageTk, Image
import signup


def sin():

    def go():    
        un=user_n.get()
        pa=password.get()
        if(database.check(un)):
            if(database.check_p(un,pa)):
                root_s.destroy()
                home_screen.home(un)
            else:
                reponse=messagebox.showerror("ERROR","UserName/PassWord does not match")     
        else:
            reponse=messagebox.showerror("ERROR","UserName Does not EXIST")
    def my_func(*args):
        root_s.destroy()
        signup.sup()

    root_s =Tk()
    root_s.geometry("350x350")
    root_s.title("LOGIN")
    root_s.iconbitmap(default='image/dragon.ico')

    #Label
    Label(root_s,text="").grid(row=0,column=0)
    Label(root_s,text="Username",font=("",12)).grid(row=1,column=0,pady=10,columnspan=3)
    Label(root_s,text="Password",font=(" ",12)).grid(row=3,column=0,pady=10,columnspan=3)
    Label(root_s,text="You don't have an account? ",fg='grey').grid(row=6,column=1,pady=50)
    l2=Label(root_s,text="signup",fg="#1C54BB",cursor="hand2")
    l2.place(x=250,y=310)
    l2.bind("<Button-1>",my_func)

    #entry
    global user_n
    global password
    user_n=Entry(root_s,width=25,font=("Bahnschrift SemiLight",13))
    user_n.grid(row=2,column=0,columnspan=3,padx=60)
    password=Entry(root_s,width=25,font=("times new roman",13),show='*')
    password.grid(row=4,column=0,padx=60,columnspan=4)

    #buttons
    bae=Button(root_s,text="SIGN IN",command=go,padx=15,pady=10).grid(row=5,column=0,columnspan=5,pady=30,padx=60)
