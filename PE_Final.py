from tkinter import filedialog
from tkinter import *
import mysql.connector
import time
from cryptosteganography import CryptoSteganography

root = Tk()
root.geometry('700x400')


#Decryption part


def callbackd(sv):
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
		llaaa.place(x=100,y=210)
		root.after(3000, root.destroy)

def ret():
	sv = StringVar()
	sv.trace("w", lambda name, index, mode, sv=sv: callbackd(sv))
	lla=Label(root,text="master key:")
	lla.place(x=100,y=160)
	entr=Entry(root, textvariable=sv)
	entr.place(x=170,y=157)
	bb=Button(root,text="submit", command=pr)
	bb.place(x=150,y=185)

def filed():
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

def dec():
	b1.destroy();
	b2.destroy();
	l.destroy()
	la.destroy()
	lab.destroy()
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="rishi1008",database="rishi")
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM huta")
	myresult = mycursor.fetchall()
	global we,us
	for x in myresult:
		we=list(x[0].split(" "))
		us=list(x[1].split(" "))    
	labe=Label(root,text="select an image")
	labe.place(x=100,y=30)
	btn=Button(root,text="Browse", command=filed)
	btn.place(x=220,y=27)






#encryption part


def callback(sv):
	global mas
	mas = sv.get()

def insert():
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="rishi1008",database="rishi")
	cursor = mydb.cursor()
	q1="delete from huta"
	q="insert into huta values('"+e.get()+"','"+en.get()+"')";
	cursor.execute(q1)
	cursor.execute(q)
	mydb.commit()
	crypto_steganography = CryptoSteganography(mas)
	crypto_steganography.hide(filename, 'output_im.png', ent.get())
	res_label = Label(root,text="process completed!")
	res_label.place(x=120,y=300,width=200,height=50)
	root.after(2000, root.destroy)


def file(event=None):
	global filename
	sv = StringVar()
	sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
	filename = filedialog.askopenfilename()
	ll=Label(root,text="selected file "+filename)
	ll.place(x=100,y=210)
	lla=Label(root,text="master key:")
	lla.place(x=100,y=235)
	entr=Entry(root, textvariable=sv)
	entr.place(x=170,y=232)
	bt=Button(root, text="submit", command=insert)
	bt.place(x=150,y=260)

def encr():
	s=variable.get()
	clear()
	st="enter "+str(s)+" website(s) seperated by space:"
	l=Label(root, text=st)
	l.place(x=100,y=20)
	la=Label(root, text="enter usernames seperated by space")
	la.place(x=100,y=85)
	lab=Label(root, text="enter passwords seperated by space")
	lab.place(x=100,y=135)
	labe=Label(root,text="select an image")
	labe.place(x=100,y=185)
	llaabb=Label(root,text="Wait for a while to generate the encrypted image, Don't close or move the window!")
	llaabb.place(x=100,y=280)
	
	global e,en,ent
	e=Entry(root);
	e.place(x=110,y=45,width=300,height=40)
	en=Entry(root)
	en.place(x=110,y=110,width=300,height=20)
	ent=Entry(root)
	ent.place(x=110,y=160,width=300,height=20)
	btn=Button(root,text="Browse", command=file)
	btn.place(x=220,y=182)


def clear():
	lbl.destroy()
	b.destroy()
	w.destroy()


def enc():
	b1.destroy();
	b2.destroy();
	l.destroy()
	la.destroy()
	lab.destroy()
	global lbl, variable, b, w;
	

	
	lbl = Label(root, text="number of entries")
	lbl.place(x=100,y=30)

	variable = StringVar(root)
	variable.set("1") # default value

	w = OptionMenu(root, variable, "1", "2", "3", "4", "5")
	w.pack()
	w.place(x=210,y=27)
	b=Button(root,text='Enter Data',command=encr)
	b.place(x=220,y=70)



def home():
	global b1,b2,l,la,lab
	b1=Button(root, text="ENCRYPT", command=enc)
	b1.place(x=250, y=150)
	b2=Button(root, text="DECRYPT", command=dec)
	b2.place(x=350, y=150)
	l=Label(root,text="Password encrypto")
	l.place(x=270,y=20)
	la=Label(root,text="WELCOME!")
	lab=Label(root,text="While you take care of your business, we take care of your Passwords.\nNever fear forgetting your passwords or getting hacked.\nSleep sound with trust")
	la.place(x=290,y=45)
	lab.place(x=150,y=70)
	root.wm_iconbitmap('h.ico')
	root.wm_title('Password encrypto')

home()

root.mainloop()