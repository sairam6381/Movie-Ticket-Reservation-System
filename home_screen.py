from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import clickonseat

def home(uname):
    def movie(n):
        root_h.destroy()
        clickonseat.seat(n,uname)

    global root_h
    root_h=Tk()
    root_h.geometry("800x500")
    root_h.title("SELECT MOVIE")
    root_h.iconbitmap(default='image/dragon.ico')
    root_h.resizable(False, False)
    root_h.config(background="black")
    Label(root_h,text="SELECT THE MOVIE",font=("times new roman",18),bg="black",fg="white").grid(row=0,column=0,pady=30,padx=300,columnspan=8)
    Label(root_h,text=" ",font=("times new roman",15),bg="black").grid(row=1,column=0,padx=18)

    img1 = ImageTk.PhotoImage(Image.open("image/movies/avathar.jpg"))  
    Button(root_h,image=img1,command=lambda:movie("AVATAR")).grid(row=1,column=1)
    Label(root_h,text="Avatar",font=("times new roman",15),bg="black",fg="white").grid(row=2,column=1)
    Label(root_h,text="CBFC: U/A\nSci-fi/Action\n2h 42m",font=("times new roman",11),bg="black",fg='grey').grid(row=3,column=1)

    img2 = ImageTk.PhotoImage(Image.open("image/movies/inception.jpg"))  
    Button(root_h,image=img2,command=lambda:movie("INCEPTION")).grid(row=1,column=2)
    Label(root_h,text="Inception",font=("times new roman",15),bg="black",fg="white").grid(row=2,column=2)
    Label(root_h,text="CBFC: U/A\nAction/Sci-fi\n2h 28m",font=("times new roman",11),bg="black",fg='grey').grid(row=3,column=2)

    img3 = ImageTk.PhotoImage(Image.open("image/movies/john wick.jpg"))  
    Button(root_h,image=img3,command=lambda:movie("JOHN_WICK")).grid(row=1,column=3)
    Label(root_h,text="John Wick",font=("times new roman",15),bg="black",fg="white").grid(row=2,column=3)
    Label(root_h,text="CBFC: U/A\nAction/Thriller\n1h 41m",font=("times new roman",11),bg="black",fg='grey').grid(row=3,column=3)

    img4 = ImageTk.PhotoImage(Image.open("image/movies/malificant.jpg"))  
    Button(root_h,image=img4,command=lambda:movie("MALEFICENT")).grid(row=1,column=4)
    Label(root_h,text="Maleficent",font=("times new roman",15),bg="black",fg="white").grid(row=2,column=4)
    Label(root_h,text="CBFC: U/A\nFantasy/Adventure\n1h 38m",font=("times new roman",11),bg="black",fg='grey').grid(row=3,column=4)

    if uname=="ADMIN":
        messagebox.showinfo("INFO", "This is ADMIN account\n Here you can reset seat availability ")
    root_h.mainloop()
