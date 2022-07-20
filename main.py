from tkinter import *
from PIL import ImageTk, Image
import signup
import signin

def main_w():

    def signin1():
        root.destroy()
        signin.sin()
    
    def signup1():
        root.destroy()
        signup.sup()

    root= Tk()
    root.geometry("600x364")
    root.iconbitmap(default='image/dragon.ico')
    root.title("CINEMA BUFFER")
    root.wm_attributes('-transparentcolor', '#ab23ff')
    root.resizable(False, False)

    img = ImageTk.PhotoImage(Image.open("image/fg.jpg"))  
    l=Label(root,image=img)
    l.place(x=0,y=0,relwidth=1,relheight=1)

    #buttons
    Label(root,text="",bg="black").grid(row=0,column=0,padx=1000,columnspan=50,pady=120)
    Label(root,text="",bg="black").grid(row=2,column=0,padx=120)
    login=Button(root,text="SIGN IN",bg='black',fg='red',padx=17,pady=10,command=signin1).grid(row=2,column=1)
    register=Button(root,text="SIGN UP",bg='black',fg='white',padx=16,pady=10,command=signup1).grid(row=2,column=2)

    root.mainloop()
main_w()
