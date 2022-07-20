import sqlite3
con=sqlite3.connect("theatre.db")
c=con.cursor()

# **FOR REFERENCE**
#con.commit()
#c.execute('''DELETE FROM login WHERE uname="sree";''')
#c.execute(""" create table login(uname text,mailid text,password varchar)""")
#c.execute("""create table JOHN_WICK(seat varchar)""")

#c.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
#myresult = c.fetchall()
#for x in myresult:
#    print(x)
#con.commit()

#Listed Movies : [AVATAR,INCEPTION,JOHN_WICK,MALEFICENT]

def show(movie):
    con=sqlite3.connect("theatre.db")
    c=con.cursor()
    c.execute("select * from %s"%(movie))
    r=c.fetchall()
    for i in r:
        print(i)
    con.commit()
    con.close()

def delseat(movie):
    con=sqlite3.connect("theatre.db")
    c=con.cursor()
    c.execute("""delete from %s"""%(movie))
    con.commit()
    con.close()

def filledseat(movie):
    se=[]
    con=sqlite3.connect("theatre.db")
    c=con.cursor()
    c.execute("select seat from %s"%(movie))
    r=c.fetchall()
    for i in r:
        se.append(str(i[0]))
    return se

def addseat(movie,seats):
    con=sqlite3.connect("theatre.db")
    c=con.cursor()
    for i in seats:
        c.execute("""insert into %s values ('%s')"""%(movie,i))
    con.commit()
    con.close()

def add(uname,mailid,password):
    con=sqlite3.connect("theatre.db")
    c=con.cursor()
    c.execute("insert into login values(?,?,?)",(uname,mailid,password))
    con.commit()
    con.close()
    
def check(name):
    con=sqlite3.connect("theatre.db")
    c=con.cursor()
    r=c.execute("select uname from login where uname=(?)",(name,))
    for i in r:
        if name in i:
            return 1
    return 0
    con.commit()
    con.close()

def check_p(name,passw):
    con=sqlite3.connect("theatre.db")
    c=con.cursor()
    r=c.execute("select password from login where uname=(?)",(name,))
    for i in r:
        #print(i)
        if passw in i:
            return 1
    return 0
    con.commit()
    con.close()
    
