from tkinter import *
 
root = Tk()

root.geometry('700x400')
l=Label(root,text="Password encrypto")
l.place(x=260,y=20)
la=Label(root,text="WELCOME!")
lab=Label(root,text="While you take care of your business, we take care of your Passwords.\nNever fear forgetting your passwords or getting hacked.\nSleep sound with trust")
la.place(x=280,y=45)
lab.place(x=150,y=70)
root.wm_iconbitmap('h.ico')
root.wm_title('Password encrypto')
root.mainloop()