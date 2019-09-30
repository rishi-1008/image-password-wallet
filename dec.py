from tkinter import filedialog
from tkinter import *
from cryptosteganography import CryptoSteganography
import mysql.connector

root = Tk()

root.geometry('700x400')

mydb = mysql.connector.connect(host="localhost",user="root",passwd="rishi1008",database="rishi")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM huta")
myresult = mycursor.fetchall()
global we,us
for x in myresult:
	we=list(x[0].split(" "))
	us=list(x[1].split(" "))

def callback(sv):
	global mas
	mas = sv.get()

def pr():
	crypto_steganography = CryptoSteganography(mas)
	secret = crypto_steganography.retrieve(filename)
	if secret is None:
	    llaaa=Label(root,text="Sry!!")
	    llaaa.place(x=100,y=230)
	    root.after(3000, root.destroy)
	else:
		l=list(secret.split(" "))
		sep=we.index(var.get())
		llaaa=Label(root,text="Your password: "+l[sep])
		llaaa.place(x=100,y=230)
		root.after(3000, root.destroy)

def ret():
	sv = StringVar()
	sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
	lla=Label(root,text="master key:")
	lla.place(x=100,y=180)
	entr=Entry(root, textvariable=sv)
	entr.place(x=170,y=177)
	bb=Button(root,text="submit", command=pr)
	bb.place(x=150,y=205)

def file():
    global filename
    filename = filedialog.askopenfilename()
    ll=Label(root,text="selected file "+filename)
    ll.place(x=100,y=55)
    global var
    var=StringVar(root)
    var.set(we[0])
    llaa=Label(root,text="select a website")
    llaa.place(x=100,y=80)
    w=OptionMenu(root, var, *we)
    w.place(x=220,y=77)
    k=var.get()
    i=we.index(str(k))
    bb=Button(root,text="Enter master key", command=ret)
    bb.place(x=150,y=110)
    
labe=Label(root,text="select an image")
labe.place(x=100,y=30)
btn=Button(root,text="Browse", command=file)
btn.place(x=220,y=27)



root.mainloop()