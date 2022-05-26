import sqlite3
#con=sqlite3.connect("theatre.db")
#c=con.cursor()
#c.execute('''DELETE FROM login WHERE uname="sree";''')
#con.commit()

#c.execute(""" create table login(uname text,mailid text,password varchar)""")
#print("created")


def add(uname,mailid,password):
    con=sqlite3.connect("theatre.db")
    c=con.cursor()
    c.execute("insert into login values(?,?,?)",(uname,mailid,password))
    con.commit()
    con.close()

    
def show():
    con=sqlite3.connect("theatre.db")
    c=con.cursor()
    c.execute("select * from login")
    r=c.fetchall()
    return r


def show1(name):
    con=sqlite3.connect("theatre.db")
    c=con.cursor()
    r=c.execute("select uname from login where uname=(?)",(name,))
	    #r=c.fetchone
    for i in r:
        print(i)
        if name in i:
            print("yes")
        else:
            print("no")
    #return r


def check(name):
    con=sqlite3.connect("theatre.db")
    c=con.cursor()
    r=c.execute("select uname from login where uname=(?)",(name,))
    for i in r:
        #print(i)
        if name in i:
            return 1
    return 0

def check_p(name,passw):
    con=sqlite3.connect("theatre.db")
    c=con.cursor()
    r=c.execute("select password from login where uname=(?)",(name,))
    for i in r:
        #print(i)
        if passw in i:
            return 1
    return 0
    
#print(show())
#show1("saba")
#print(check("sai"))
