from tkinter import * 
from PIL import ImageTk,Image
import payment
import database
import home_screen

seats=[]
def but(sea):   
    if(sea['bg']== "white"):
       sea.config(bg="#CEA408")
       seats.append(sea['text'])        
    else:
        sea.config(bg="white")
        if(sea["text"] in seats):
            seats.remove(sea['text'])

def seat(na,uname):

    def exitfn():
        screen.destroy()

    def Backfn():
        screen.destroy()
        seats.clear()
        home_screen.home("ad")
    
    def Backfn1():
        screen.destroy()
        seats.clear()
        home_screen.home(uname)

    def delefun():
        database.delseat(na)
        screen.destroy()
        seat(na,uname)

    def pt():
        screen.destroy()
        database.addseat(na,seats)
        payment.pay_s(seats,na,uname)

    filled=database.filledseat(na)
    item=[]
    letters=['A','B','C','D','E']
    for i in range(50):
        if(i+1<11):
            item.append(str(letters[0]+str(i+1)))

        elif(i+1<21):
            item.append(str(letters[1]+str(i-9)))

        elif(i+1<31):
            item.append(str(letters[2]+str(i-19)))

        elif(i+1<41):
            item.append(str(letters[3]+str(i-29)))

        elif(i+1<51):
            item.append(str(letters[4]+str(i-39)))
    
    screen=Tk()
    screen.geometry("1025x530")
    screen.config(bg="black")
    screen.iconbitmap(default='image/dragon.ico')
    screen.title("SELECT SEAT")

    #Labels
    Label(screen,text="SCREEN ON THIS SIDE",font=("Arial",18),padx=410,pady=20).grid(row=0,column=0,pady=20,columnspan=25)

    Label(screen,text="A",bg="black",fg='grey').grid(row=1,column=0,pady=20,padx=10)
    Label(screen,text="B",bg="black",fg='grey').grid(row=2,column=0,pady=20)
    Label(screen,text="C",bg="black",fg='grey').grid(row=3,column=0,pady=20)
    Label(screen,text="D",bg="black",fg='grey').grid(row=4,column=0,pady=20)
    Label(screen,text="E",bg="black",fg='grey').grid(row=5,column=0,pady=20)
    
    Label(screen,text="A",bg="black",fg='grey').grid(row=1,column=13,pady=20,padx=10)
    Label(screen,text="B",bg="black",fg='grey').grid(row=2,column=13,pady=20,padx=10)
    Label(screen,text="C",bg="black",fg='grey').grid(row=3,column=13,pady=20,padx=10)
    Label(screen,text="D",bg="black",fg='grey').grid(row=4,column=13,pady=20,padx=10)
    Label(screen,text="E",bg="black",fg='grey').grid(row=5,column=13,pady=20,padx=10)

    #Buttons
    no=0
    butt=[]
    if item[no] not in filled:
        a1=Button(screen,text='A1',padx=25,bg="white",command=lambda:but(a1))
        a1.grid(row=1,column=1)
        butt.append("A1")
    else:
        a1=Button(screen,text='A1',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(a1),state=DISABLED)
        a1.grid(row=1,column=1)
        butt.append("A1")
    no+=1
    if item[no] not in filled:
        a2=Button(screen,text='A2',padx=25,bg="white",command=lambda:but(a2))
        a2.grid(row=1,column=2)
        butt.append("A2")
    else:
        a2=Button(screen,text='A2',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(a2),state=DISABLED)
        a2.grid(row=1,column=2)
        butt.append("A2")
    no+=1
    Label(screen,text='',bg='black',padx=30).grid(row=1,column=3)
    if item[no] not in filled:
        a3=Button(screen,text='A3',padx=25,bg="white",command=lambda:but(a3))
        a3.grid(row=1,column=4)
        butt.append("A3")
    else:
        a3=Button(screen,text='A3',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(a3),state=DISABLED)
        a3.grid(row=1,column=4)
        butt.append("A3")
    no+=1
    if item[no] not in filled:
        a4=Button(screen,text='A4',padx=25,bg="white",command=lambda:but(a4))
        a4.grid(row=1,column=5)
        butt.append("A4")
    else:
        a4=Button(screen,text='A4',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(a4),state=DISABLED)
        a4.grid(row=1,column=5)
        butt.append("A4")
    no+=1
    if item[no] not in filled:
        a5=Button(screen,text='A5',padx=25,bg="white",command=lambda:but(a5))
        a5.grid(row=1,column=6)
        butt.append("A5")
    else:
        a5=Button(screen,text='A5',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(a5),state=DISABLED)
        a5.grid(row=1,column=6)
        butt.append("A5")
    no+=1
    if item[no] not in filled:
        a6=Button(screen,text='A6',padx=25,bg="white",command=lambda:but(a6))
        a6.grid(row=1,column=7)
        butt.append("A6")
    else:
        a6=Button(screen,text='A6',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(a6),state=DISABLED)
        a6.grid(row=1,column=7)
        butt.append("A6")
    no+=1
    if item[no] not in filled:
        a7=Button(screen,text='A7',padx=25,bg="white",command=lambda:but(a7))
        a7.grid(row=1,column=8)
        butt.append("A7")
    else:
        a7=Button(screen,text='A7',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(a7),state=DISABLED)
        a7.grid(row=1,column=8)
        butt.append("A7")
    no+=1
    if item[no] not in filled:
        a8=Button(screen,text='A8',padx=25,bg="white",command=lambda:but(a8))
        a8.grid(row=1,column=9)
        butt.append("A8")
    else:
        a8=Button(screen,text='A8',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(a8),state=DISABLED)
        a8.grid(row=1,column=9)
        butt.append("A8")
    no+=1
    Label(screen,text='',bg='black',padx=30).grid(row=1,column=10)
    if item[no] not in filled:
        a9=Button(screen,text='A9',padx=25,bg="white",command=lambda:but(a9))
        a9.grid(row=1,column=11)
        butt.append("A9")
    else:
        a9=Button(screen,text='A9',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(a9),state=DISABLED)
        a9.grid(row=1,column=11)
        butt.append("A9")
    no+=1
    if item[no] not in filled:
        a10=Button(screen,text='A10',padx=25,bg="white",command=lambda:but(a10))
        a10.grid(row=1,column=12)
        butt.append("A10")
    else:
        a10=Button(screen,text='A10',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(a10),state=DISABLED)
        a10.grid(row=1,column=12)
        butt.append("A10")
    no+=1


    if item[no] not in filled:
        b1=Button(screen,text='B1',padx=25,bg="white",command=lambda:but(b1))
        b1.grid(row=2,column=1)
        butt.append("B1")
    else:
        b1=Button(screen,text='B1',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(b1),state=DISABLED)
        b1.grid(row=2,column=1)
        butt.append("B1")
    no+=1
    if item[no] not in filled:
        b2=Button(screen,text='B2',padx=25,bg="white",command=lambda:but(b2))
        b2.grid(row=2,column=2)
        butt.append("B2")
    else:
        b2=Button(screen,text='B2',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(b2),state=DISABLED)
        b2.grid(row=2,column=2)
        butt.append("B2")
    no+=1
    Label(screen,text='',bg='black',padx=30).grid(row=2,column=3)
    if item[no] not in filled:
        b3=Button(screen,text='B3',padx=25,bg="white",command=lambda:but(b3))
        b3.grid(row=2,column=4)
        butt.append("B3")
    else:
        b3=Button(screen,text='B3',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(b3),state=DISABLED)
        b3.grid(row=2,column=4)
        butt.append("B3")
    no+=1
    if item[no] not in filled:
        b4=Button(screen,text='B4',padx=25,bg="white",command=lambda:but(b4))
        b4.grid(row=2,column=5)
        butt.append("B4")
    else:
        b4=Button(screen,text='B4',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(b4),state=DISABLED)
        b4.grid(row=2,column=5)
        butt.append("B4")
    no+=1
    if item[no] not in filled:
        b5=Button(screen,text='B5',padx=25,bg="white",command=lambda:but(b5))
        b5.grid(row=2,column=6)
        butt.append("B5")
    else:
        b5=Button(screen,text='B5',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(b5),state=DISABLED)
        b5.grid(row=2,column=6)
        butt.append("B5")
    no+=1
    if item[no] not in filled:
        b6=Button(screen,text='B6',padx=25,bg="white",command=lambda:but(b6))
        b6.grid(row=2,column=7)
        butt.append("B6")
    else:
        b6=Button(screen,text='B6',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(b6),state=DISABLED)
        b6.grid(row=2,column=7)
        butt.append("B6")
    no+=1
    if item[no] not in filled:
        b7=Button(screen,text='B7',padx=25,bg="white",command=lambda:but(b7))
        b7.grid(row=2,column=8)
        butt.append("B7")
    else:
        b7=Button(screen,text='B7',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(b7),state=DISABLED)
        b7.grid(row=2,column=8)
        butt.append("B7")
    no+=1
    if item[no] not in filled:
        b8=Button(screen,text='B8',padx=25,bg="white",command=lambda:but(b8))
        b8.grid(row=2,column=9)
        butt.append("B8")
    else:
        b8=Button(screen,text='B8',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(b8),state=DISABLED)
        b8.grid(row=2,column=9)
        butt.append("B8")
    no+=1
    Label(screen,text='',bg='black',padx=30).grid(row=2,column=10)
    if item[no] not in filled:
        b9=Button(screen,text='B9',padx=25,bg="white",command=lambda:but(b9))
        b9.grid(row=2,column=11)
        butt.append("B9")
    else:
        b9=Button(screen,text='B9',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(b9),state=DISABLED)
        b9.grid(row=2,column=11)
        butt.append("B9")
    no+=1
    if item[no] not in filled:
        b10=Button(screen,text='B10',padx=25,bg="white",command=lambda:but(b10))
        b10.grid(row=2,column=12)
        butt.append("B10")
    else:
        b10=Button(screen,text='B10',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(b10),state=DISABLED)
        b10.grid(row=2,column=12)
        butt.append("B10")
    no+=1

    if item[no] not in filled:
        c1=Button(screen,text='C1',padx=25,bg="white",command=lambda:but(c1))
        c1.grid(row=3,column=1)
        butt.append("C1")
    else:
        c1=Button(screen,text='C1',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(c1),state=DISABLED)
        c1.grid(row=3,column=1)
        butt.append("C1")
    no+=1
    if item[no] not in filled:
        c2=Button(screen,text='C2',padx=25,bg="white",command=lambda:but(c2))
        c2.grid(row=3,column=2)
        butt.append("C2")
    else:
        c2=Button(screen,text='C2',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(c2),state=DISABLED)
        c2.grid(row=3,column=2)
        butt.append("C2")
    no+=1
    Label(screen,text='',bg='black',padx=30).grid(row=2,column=3)
    if item[no] not in filled:
        c3=Button(screen,text='C3',padx=25,bg="white",command=lambda:but(c3))
        c3.grid(row=3,column=4)
        butt.append("C3")
    else:
        c3=Button(screen,text='C3',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(c3),state=DISABLED)
        c3.grid(row=3,column=4)
        butt.append("C3")
    no+=1
    if item[no] not in filled:
        c4=Button(screen,text='C4',padx=25,bg="white",command=lambda:but(c4))
        c4.grid(row=3,column=5)
        butt.append("C4")
    else:
        c4=Button(screen,text='C4',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(c4),state=DISABLED)
        c4.grid(row=3,column=5)
        butt.append("C4")
    no+=1
    if item[no] not in filled:
        c5=Button(screen,text='C5',padx=25,bg="white",command=lambda:but(c5))
        c5.grid(row=3,column=6)
        butt.append("C5")
    else:
        c5=Button(screen,text='C5',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(c5),state=DISABLED)
        c5.grid(row=3,column=6)
        butt.append("C5")
    no+=1
    if item[no] not in filled:
        c6=Button(screen,text='C6',padx=25,bg="white",command=lambda:but(c6))
        c6.grid(row=3,column=7)
        butt.append("C6")
    else:
        c6=Button(screen,text='C6',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(c6),state=DISABLED)
        c6.grid(row=3,column=7)
        butt.append("C6")
    no+=1
    if item[no] not in filled:
        c7=Button(screen,text='C7',padx=25,bg="white",command=lambda:but(c7))
        c7.grid(row=3,column=8)
        butt.append("C7")
    else:
        c7=Button(screen,text='C7',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(c7),state=DISABLED)
        c7.grid(row=3,column=8)
        butt.append("C7")
    no+=1
    if item[no] not in filled:
        c8=Button(screen,text='C8',padx=25,bg="white",command=lambda:but(c8))
        c8.grid(row=3,column=9)
        butt.append("C8")
    else:
        c8=Button(screen,text='C8',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(c8),state=DISABLED)
        c8.grid(row=3,column=9)
        butt.append("C8")
    no+=1
    Label(screen,text='',bg='black',padx=30).grid(row=2,column=10)
    if item[no] not in filled:
        c9=Button(screen,text='C9',padx=25,bg="white",command=lambda:but(c9))
        c9.grid(row=3,column=11)
        butt.append("C9")
    else:
        c9=Button(screen,text='C9',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(c9),state=DISABLED)
        c9.grid(row=3,column=11)
        butt.append("C9")
    no+=1
    if item[no] not in filled:
        c10=Button(screen,text='C10',padx=25,bg="white",command=lambda:but(c10))
        c10.grid(row=3,column=12)
        butt.append("C10")
    else:
        c10=Button(screen,text='C10',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(c10),state=DISABLED)
        c10.grid(row=3,column=12)
        butt.append("C10")
    no+=1


    if item[no] not in filled:
        d1=Button(screen,text='D1',padx=25,bg="white",command=lambda:but(d1))
        d1.grid(row=4,column=1)
        butt.append("D1")
    else:
        d1=Button(screen,text='D1',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(d1),state=DISABLED)
        d1.grid(row=4,column=1)
        butt.append("D1")
    no+=1
    if item[no] not in filled:
        d2=Button(screen,text='D2',padx=25,bg="white",command=lambda:but(d2))
        d2.grid(row=4,column=2)
        butt.append("D2")
    else:
        d2=Button(screen,text='D2',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(d2),state=DISABLED)
        d2.grid(row=4,column=2)
        butt.append("D2")
    no+=1
    Label(screen,text='',bg='black',padx=30).grid(row=2,column=3)
    if item[no] not in filled:
        d3=Button(screen,text='D3',padx=25,bg="white",command=lambda:but(d3))
        d3.grid(row=4,column=4)
        butt.append("D3")
    else:
        d3=Button(screen,text='D3',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(d3),state=DISABLED)
        d3.grid(row=4,column=4)
        butt.append("D3")
    no+=1
    if item[no] not in filled:
        d4=Button(screen,text='D4',padx=25,bg="white",command=lambda:but(d4))
        d4.grid(row=4,column=5)
        butt.append("D4")
    else:
        d4=Button(screen,text='D4',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(d4),state=DISABLED)
        d4.grid(row=4,column=5)
        butt.append("D4")
    no+=1
    if item[no] not in filled:
        d5=Button(screen,text='D5',padx=25,bg="white",command=lambda:but(d5))
        d5.grid(row=4,column=6)
        butt.append("D5")
    else:
        d5=Button(screen,text='D5',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(d5),state=DISABLED)
        d5.grid(row=4,column=6)
        butt.append("D5")
    no+=1
    if item[no] not in filled:
        d6=Button(screen,text='D6',padx=25,bg="white",command=lambda:but(d6))
        d6.grid(row=4,column=7)
        butt.append("D6")
    else:
        d6=Button(screen,text='D6',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(d6),state=DISABLED)
        d6.grid(row=4,column=7)
        butt.append("D6")
    no+=1
    if item[no] not in filled:
        d7=Button(screen,text='D7',padx=25,bg="white",command=lambda:but(d7))
        d7.grid(row=4,column=8)
        butt.append("D7")
    else:
        d7=Button(screen,text='D7',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(d7),state=DISABLED)
        d7.grid(row=4,column=8)
        butt.append("D7")
    no+=1
    if item[no] not in filled:
        d8=Button(screen,text='D8',padx=25,bg="white",command=lambda:but(d8))
        d8.grid(row=4,column=9)
        butt.append("D8")
    else:
        d8=Button(screen,text='D8',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(d8),state=DISABLED)
        d8.grid(row=4,column=9)
        butt.append("D8")
    no+=1
    Label(screen,text='',bg='black',padx=30).grid(row=2,column=10)
    if item[no] not in filled:
        d9=Button(screen,text='D9',padx=25,bg="white",command=lambda:but(d9))
        d9.grid(row=4,column=11)
        butt.append("D9")
    else:
        d9=Button(screen,text='D9',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(d9),state=DISABLED)
        d9.grid(row=4,column=11)
        butt.append("D9")
    no+=1
    if item[no] not in filled:
        d10=Button(screen,text='D10',padx=25,bg="white",command=lambda:but(d10))
        d10.grid(row=4,column=12)
        butt.append("D10")
    else:
        d10=Button(screen,text='D10',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(d10),state=DISABLED)
        d10.grid(row=4,column=12)
        butt.append("D10")
    no+=1


    if item[no] not in filled:
        e1=Button(screen,text='E1',padx=25,bg="white",command=lambda:but(e1))
        e1.grid(row=5,column=1)
        butt.append("E1")
    else:
        e1=Button(screen,text='E1',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(e1),state=DISABLED)
        e1.grid(row=5,column=1)
        butt.append("E1")
    no+=1
    if item[no] not in filled:
        e2=Button(screen,text='E2',padx=25,bg="white",command=lambda:but(e2))
        e2.grid(row=5,column=2)
        butt.append("E2")
    else:
        e2=Button(screen,text='E2',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(e2),state=DISABLED)
        e2.grid(row=5,column=2)
        butt.append("E2")
    no+=1
    Label(screen,text='',bg='black',padx=30).grid(row=2,column=3)
    if item[no] not in filled:
        e3=Button(screen,text='E3',padx=25,bg="white",command=lambda:but(e3))
        e3.grid(row=5,column=4)
        butt.append("E3")
    else:
        e3=Button(screen,text='E3',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(e3),state=DISABLED)
        e3.grid(row=5,column=4)
        butt.append("E3")
    no+=1
    if item[no] not in filled:
        e4=Button(screen,text='E4',padx=25,bg="white",command=lambda:but(e4))
        e4.grid(row=5,column=5)
        butt.append("E4")
    else:
        e4=Button(screen,text='E4',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(e4),state=DISABLED)
        e4.grid(row=5,column=5)
        butt.append("E4")
    no+=1
    if item[no] not in filled:
        e5=Button(screen,text='E5',padx=25,bg="white",command=lambda:but(e5))
        e5.grid(row=5,column=6)
        butt.append("E5")
    else:
        e5=Button(screen,text='E5',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(e5),state=DISABLED)
        e5.grid(row=5,column=6)
        butt.append("E5")
    no+=1
    if item[no] not in filled:
        e6=Button(screen,text='E6',padx=25,bg="white",command=lambda:but(e6))
        e6.grid(row=5,column=7)
        butt.append("E6")
    else:
        e6=Button(screen,text='E6',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(e6),state=DISABLED)
        e6.grid(row=5,column=7)
        butt.append("E6")
    no+=1
    if item[no] not in filled:
        e7=Button(screen,text='E7',padx=25,bg="white",command=lambda:but(e7))
        e7.grid(row=5,column=8)
        butt.append("E7")
    else:
        e7=Button(screen,text='E7',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(e7),state=DISABLED)
        e7.grid(row=5,column=8)
        butt.append("E7")
    no+=1
    if item[no] not in filled:
        e8=Button(screen,text='E8',padx=25,bg="white",command=lambda:but(e8))
        e8.grid(row=5,column=9)
        butt.append("E8")
    else:
        e8=Button(screen,text='E8',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(e8),state=DISABLED)
        e8.grid(row=5,column=9)
        butt.append("E8")
    no+=1
    Label(screen,text='',bg='black',padx=30).grid(row=2,column=10)
    if item[no] not in filled:
        e9=Button(screen,text='E9',padx=25,bg="white",command=lambda:but(e9))
        e9.grid(row=5,column=11)
        butt.append("E9")
    else:
        e9=Button(screen,text='E9',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(e9),state=DISABLED)
        e9.grid(row=5,column=11)
        butt.append("E9")
    no+=1
    if item[no] not in filled:
        e10=Button(screen,text='E10',padx=25,bg="white",command=lambda:but(e10))
        e10.grid(row=5,column=12)
        butt.append("E10")
    else:
        e10=Button(screen,text='E10',padx=25,bg="#C2C0B8",relief=SUNKEN,command=lambda:but(e10),state=DISABLED)
        e10.grid(row=5,column=12)
        butt.append("E10")
    no+=1    

    if uname=="ADMIN" or uname=="ad":
        dele=Button(screen,text="Clear",font=("Arial",12),padx=20,pady=4,bg="black",fg="red",activebackground="black",activeforeground="red",command=delefun)
        dele.grid(row=6,column=10)
        back=Button(screen,text="Back",font=("Arial",12),padx=20,pady=4,bg="black",fg="red",activebackground="black",activeforeground="red",command=Backfn)
        back.place(x=630,y=446)
        ex=Button(screen,text="Exit",font=("Arial",12),padx=20,pady=4,bg="black",fg="red",activebackground="black",activeforeground="red",command=exitfn)
        ex.grid(row=6,column=11,pady=30,columnspan=5)
    
    else:
        back=Button(screen,text="Back",font=("Arial",12),padx=20,pady=4,bg="black",fg="red",activebackground="black",activeforeground="red",command=Backfn1)
        back.grid(row=6,column=10)
        c=Button(screen,text="Confirm",font=("Arial",12),padx=20,pady=4,bg="black",fg="red",activebackground="black",activeforeground="red",command=pt)
        c.grid(row=6,column=11,pady=30,columnspan=5)
    
    for i in range(50):
        if butt[i]==item[i]:
            continue
        else:
            print("fail")
    screen.mainloop() 
