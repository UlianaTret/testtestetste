from tkinter import *
import math
import random

#criptlr2.py

def icheckkkk():
	sec_kd = int(edit1.get())
	sec_kn = int(edit11.get())
	mass_ck = []
	mass_ck.append(sec_kd)
	mass_ck.append(sec_kn)
	n = mass_ck[1]
	p = 2
	q = 0
	while p < n:
		if n%p == 0:
			n/=p
			if n ==1:
				q = mass_ck[1]/p
		else:
			p += 1
	q = int(mass_ck[1]/p)
	print("p = ", p)
	print("q = ",q)
	l = (p-1)*(q-1)
	e = 1
	while (e*mass_ck[0])%l != 1:
		e += 1
	mass_ok = [e, mass_ck[1]]
	
	print ("mass_ok = ", mass_ok)
	print ("mass_ck = ", mass_ck)
	mess = int(edit2.get())
	salt = int(edit3.get())
	
	##################################################
	cr_mess = (salt**mass_ok[0])%mass_ok[1] #3
	
	#signature
	sign = (cr_mess**mass_ck[0])%mass_ck[1] #4
	print ("sign = ", sign)
	
	#without salt
	reverse_salt = 1
	while (reverse_salt*salt)%n !=1:
		reverse_salt+=1
	print("reverse_salt", reverse_salt)
	sign_mess = (sign*reverse_salt)%mass_ok[1]
	
	#check sign with use open key
	check_sing = (sign_mess**mass_ok[0])%mass_ok[1]
	if check_sing == sign_mess:
		ok_sign = 'signature is right'
		#t8.config(text = 'signature is right')
	
	t4.config(text = 'message with salt & open_key:'+str(cr_mess))
	t5.config(text = 'signature critp message:'+str(sign))
	t6.config(text = 'sign message:'+str(sign_mess))
	t7.config(text = ok_sign)

##########dialog_windows##########################
win = Tk()
win.geometry('300x350')

t1 = Label(win, text = 'secret_key (d = ):', fg = 'black')
t1.config(font=('courier new', 15))
t1.pack()
edit1 = Entry (win, width = 20, bg = 'Lavender')
edit1.pack()

t11 = Label(win, text = 'secret_key (n = ):', fg = 'black')
t11.config(font=('courier new', 15))
t11.pack()
edit11 = Entry (win, width = 20, bg = 'Lavender')
edit11.pack()

t2 = Label(win, text = 'message:', fg = 'black')
t2.config(font=('courier new', 15))
t2.pack()
edit2 = Entry (win, width = 20, bg = 'Lavender')
edit2.pack()

t3 = Label(win, text = 'salt:', fg = 'black')
t3.config(font=('courier new', 15))
t3.pack()
edit3 = Entry (win, width = 20, bg = 'Lavender')
edit3.pack()

but = Button(win, text = 'get signature', command = icheckkkk)
but.config(font=('courier new', 10))
but.pack()

t4 = Label(win, text = '', fg = 'black')
t4.config(font=('courier new', 10))
t4.pack()

t5 = Label(win, text = '', fg = 'black')
t5.config(font=('courier new', 10))
t5.pack()

t6 = Label(win, text = '', fg = 'black')
t6.config(font=('courier new', 10))
t6.pack()

t7 = Label(win, text = '', fg = 'black')
t7.config(font=('courier new', 10))
t7.pack()

t8 = Label(win, text = '', fg = 'black')
t8.config(font=('courier new', 10))
t8.pack()

t9 = Entry(win,fg = 'black', show = '*')
t9.config(font=('courier new', 10))
t9.pack()
win.mainloop()