from tkinter import *
import smtplib
from tkinter import messagebox
import random
import database
import signin
import otp_verify
vnum_mail=0
vnum_num=0

#❌✅☒☑  ❎✅
#account_id = "AC3fc04fc188d73b2aef88bee8a6362513"

#function
def rand():
    return random.randint(1111,9999)
    
def mail1():
    def otp_mail():
        global num
        num=rand()
        #print(num)
        ma=m_idm.get()
        otp_verify.mail_verify(str(num),ma)
        print(num)
        
    def login():
        root1.destroy()
        signin.sin()
        
    def vrf_mail():
        #print(int(otpm.get()))
        global vnum_mail
        if(int(otpm.get())== num):
            vnum_mail=1
            verify=Label(root1,text="✅",padx=5,fg="green").grid(row=3,column=7)
        else:
            verify=Label(root1,text="❎",padx=5,fg="red").grid(row=3,column=7)

    def reg_mail():        
        na=u_namem.get()
        ma=m_idm.get()
        pa=e_passm.get()
        cpa=c_passm.get()

        if(database.check(na)):
            reponse=messagebox.showerror("ERROR","UserName already taken")
        else:
            if(vnum_mail==0):
                reponse=messagebox.showerror("ERROR","Verify your mail-ID")
            else:
                if(pa==cpa):
                    u_namem.delete(0, END)
                    m_idm.delete(0, END)
                    otpm.delete(0, END)
                    e_passm.delete(0, END)
                    c_passm.delete(0, END)
                    messagebox.showinfo("REGISTRATION", "Registered Sucessfully")
                    database.add(na,ma,pa)
                else:
                    reponse=messagebox.showerror("ERROR","PassWord does not match")
        #database.add(na,ma,pa)
        #print(na,ma,pa)
 
        
            
        
    #root.destroy()
    root1=Tk()
    root1.geometry("570x370")
    root1.title("SIGNUP")
    root1.iconbitmap(default='image/dragon.ico')
    root1.resizable(False, False)
    
    #label
    Label(root1,text=" ").grid(row=0,column=0,pady=1)
    Label(root1,text="         Enter UserName ",font=(" Times New Roman",10)).grid(row=1,column=0,pady=15) 
    Label( root1,text="    Enter Mail ID  ",font=(" Times New Roman",10)).grid(row=2,column=0,pady=15)
    Label( root1,text="Enter OTP  ",font=(" Times New Roman",10)).grid(row=3,column=0,pady=15)
    Label( root1,text="        Enter Password  ",font=(" Times New Roman",10)).grid(row=4,column=0,pady=15)
    Label( root1,text="          Confirm Password  ",font=(" Times New Roman",10)).grid(row=5,column=0,pady=15)

    #entry
    global otpm
    global u_namem
    global m_idm
    global e_passm
    global c_passm
    u_namem=Entry(root1,width=30,font=("times new roman",13))
    u_namem.grid(row=1,column=1,padx=10,columnspan=5)
    m_idm=Entry(root1,width=30,font=("times new roman",13))
    m_idm.grid(row=2,column=1,columnspan=5)
    otpm=Entry(root1,width=30,font=("times new roman",13))
    otpm.grid(row=3,column=1,columnspan=5)
    e_passm=Entry(root1,width=30,font=("times new roman",13),show='*')
    e_passm.grid(row=4,column=1,columnspan=5)
    c_passm=Entry(root1,width=30,font=("times new roman",13),show='*')
    c_passm.grid(row=5,column=1,columnspan=5)

    #button
    Button(root1,text="Get otp",command=otp_mail).grid(row=2,column=6,padx=10)
    Button(root1,text="Verify",padx=5,command=vrf_mail).grid(row=3,column=6,padx=10)
    reg=Button(root1,text="Register",command=reg_mail,padx=15,pady=5).grid(row=6,column=2,pady=20)
    login=Button(root1,text="Login",command=login,padx=15,pady=5).grid(row=6,column=1,pady=20)
    
    
    
    

def num1():
    def otp_num():
        global num
        num=rand()
        print(num)
        ma=m_idn.get()
        #otp_verify.number_verify(str(num),str(ma))
        
        
    def vrf_num():
        #print(int(otpm.get()))
        global vnum_num
        if(int(otpn.get())== num):
            verify=Label(root1,text="✅",padx=5,fg="green").grid(row=3,column=7)
            vnum_num=1
        else:
            verify=Label(root1,text="❎",padx=5,fg="red").grid(row=3,column=7)
            vnum_num=0
            
    def login():
        root1.destroy()
        signin.sin()
        
    def reg_num():        
        na=u_namen.get()
        ma=m_idn.get()
        pa=e_passn.get()
        cpa=c_passn.get()

        if(database.check(na)):
            reponse=messagebox.showerror("ERROR","UserName already taken")
        else:
            if(vnum_num==0):
                reponse=messagebox.showerror("ERROR","Verify your mail-ID")
            else:
                if(pa==cpa):
                    u_namen.delete(0, END)
                    m_idn.delete(0, END)
                    otpn.delete(0, END)
                    e_passn.delete(0, END)
                    c_passn.delete(0, END)
                    messagebox.showinfo("INFO", "Registered Sucessfully")
                    database.add(na,ma,pa)
                else:
                    reponse=messagebox.showerror("ERROR","PassWord does not match")

    #root.destroy()
    root1=Tk()
    root1.geometry("600x370")
    root1.title("signup")
    root1.iconbitmap(default='image/dragon.ico')
    root1.resizable(False, False)
    
    #label
    Label(root1,text=" ").grid(row=0,column=0,pady=1)
    Label(root1,text="         Enter UserName ",font=(" Times New Roman",10)).grid(row=1,column=0,pady=15) 
    Label( root1,text="               Enter Mobile number  ",font=(" Times New Roman",10)).grid(row=2,column=0,pady=15)
    Label( root1,text="Enter OTP  ",font=(" Times New Roman",10)).grid(row=3,column=0,pady=15)
    Label( root1,text="        Enter Password  ",font=(" Times New Roman",10)).grid(row=4,column=0,pady=15)
    Label( root1,text="           Confirm Password  ",font=(" Times New Roman",10)).grid(row=5,column=0,pady=15)

    #entry
    global u_namen
    global m_idn
    global otpn
    global e_passn
    global c_passn
    u_namen=Entry(root1,width=30,font=("times new roman",13))
    u_namen.grid(row=1,column=1,padx=10,columnspan=5)
    m_idn=Entry(root1,width=30,font=("times new roman",13))
    m_idn.grid(row=2,column=1,columnspan=5)
    otpn=Entry(root1,width=30,font=("times new roman",13))
    otpn.grid(row=3,column=1,columnspan=5)
    e_passn=Entry(root1,width=30,font=("times new roman",13),show='*')
    e_passn.grid(row=4,column=1,columnspan=5)
    c_passn=Entry(root1,width=30,font=("times new roman",13),show='*')
    c_passn.grid(row=5,column=1,columnspan=5)

    #button
    otp=Button(root1,text="Get otp",command=otp_num).grid(row=2,column=6)
    verify=Button(root1,text="Verify",padx=5,command=vrf_num).grid(row=3,column=6,padx=10)
    reg=Button(root1,text="Register",command=reg_num,padx=15,pady=5).grid(row=6,column=2,pady=20)
    clear=Button(root1,text="Login",command=login,padx=15,pady=5).grid(row=6,column=1,pady=20)


def sup():
    global root
    root= Tk()
    root.geometry("350x350")
    root.title("Signup")
    root.iconbitmap(default='image/dragon.ico')
    
    #functions
    def mail():
        if(r.get()):
            root.destroy()
            mail1()
        else:
            reponse=messagebox.showerror("ERROR","Accept Terms & Conditions")
            #Label(root,text=reponse).grid(row=9,column=7)
  
    def num():
        if(r.get()):
            root.destroy()
            num1()
        else:
            reponse=messagebox.showerror("ERROR","Accept Terms & Conditions")
            Label(root,text=reponse).grid(row=9,column=7)
             
    #labels
    name=Label( root,text="GET STARTED",font=(" Times New Roman",14)).grid(row=0,column=0,padx=100,pady=30,columnspan=20)   
    Label(root,text =" I agree to the Terms & Conditions ",fg='grey').grid(row=3,column=0,pady=90,padx=30,columnspan=20)

    #BUTTONS
    google=Button(root,text="Using Google",height=2,padx=25,command=mail).grid(row=1,column=0,padx=30,pady=10,columnspan=20)
    phone=Button(root,text="Using mobile number",height=2,padx=4,command=num).grid(row=2,column=0,padx=30,pady=20,columnspan=20)


    #checkbutton
    r=IntVar()
    Checkbutton(root,variable=r).grid(row=3,column=0,padx=61,pady=79,columnspan=5,rowspan=4)




#sup()
#mail1()
#num1()
