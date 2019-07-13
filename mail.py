from tkinter import *
import smtplib

def getvalue():
    global email,password,reciever
    email=u_email.get()
    password=u_password.get()
    reciever=u_reciever.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email,reciever, 'Hello')
    print('Mail sent')


#Window
window=Tk()
window.title('Mailing System')
window.geometry('600x400')
window.maxsize(600,400)
window.minsize(600,400)

#Heading
heading=Label(window,text="Mailing System",font='none 14 bold')
heading.grid(row=0,column=100,padx=50)

#email and password
e=Label(window,text="Email")
p=Label(window,text="password")

r=Label(window,text="reciever")
e.grid(row=1,column=0,sticky=W,padx=10)
p.grid(row=2,column=0,sticky=W,padx=10)
r.grid(row=3,column=0,sticky=W,padx=10)

#entry
u_email=Entry(window,width=20)
u_password=Entry(window,width=20)
u_reciever=Entry(window,width=20)
u_email.grid(row=1,column=1,sticky=W)
u_password.grid(row=2,column=1,sticky=W)
u_reciever.grid(row=3,column=1,sticky=W)

#button
button=Button(window,text='Sumbit',width=6,command=getvalue)
button.grid(row=4,column=0,sticky=W,pady=10,padx=10)



#Main Loop
window.mainloop()