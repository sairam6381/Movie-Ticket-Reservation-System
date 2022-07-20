import smtplib
from twilio.rest import Client

#INSTRUCTION : HERE YOU WANT TO FILL THE DETAILS CONTAINING ASTERISK(*) 

def mail_verify(otp,ma):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(*YOUR_MAILID*, *YOUR_PASSWORD*)
    message = "Subject:OTP Verification\n\nDear Customer,\n"+otp+" is your one time password(OTP)"
    print("OTP is : ",otp)
    s.sendmail(*YOUR_MAILID*, ma,message)
    s.quit()
    print("OTP Sent to Mail")

def number_verify(otp,num):
    account_sid = *YOUR Account SID*
    auth_token  = *YOUR Auth Token*
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+91"+num, 
        from_="+19379322457",
        body="YOUR OTP IS : "+otp)
    print("OTP Sent to Number")
