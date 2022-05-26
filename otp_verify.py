import smtplib
from twilio.rest import Client

def mail_verify(otp,ma):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("cinemabufferv.0@gmail.com", "eccohbbjewsoiewn")
    message = "Subject:OTP Verification\n\nDear Customer,\n"+otp+" is your one time password(OTP)"
    #print(otp)
    s.sendmail("python6381@gmail.com", ma,message)
    s.quit()
    print("mail done")

def number_verify(otp,num):
    account_sid = "AC3fc04fc188d73b2aef88bee8a6362513"
    auth_token  = "ec25c152d9fa12358186bc1f1ed70591"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+91"+num, 
        from_="+15716014300",
        body="YOUR OTP IS : "+otp)
    print(message.sid)
    print("number done")

s=3765
#number_verify(s)
#ot="your otp is :"
#print(ot)
#mail_verify(str(s),"sairam9488144883@gmail.com")


