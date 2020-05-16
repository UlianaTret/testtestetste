import random
import math
import matplotlib.pyplot as plt
import numpy as np
reqs = int(input("how requests = ")) #requests

def for_oc_y(mass,k):
	y = []
	i = 0
	while i < len(mass):
		y.append(mass[i][k])
		i += 1
	return y

def graf_M_D(ND_sin, D_asin):
	fig, ax = plt.subplots()
	l = np.linspace(0, 10, num = 10, endpoint=False)
	y = (2-l/10)/(2*(1-l/10)) + 0.5 #sinh teor blue
	y1 = (2-l/10)/(2*(1-l/10)) #asinh teor yellow
	ax.plot(l/10,y, l/10,y1)
	k = 0
	y2 = for_oc_y(ND_sin,k)
	y3 = D_asin
	ax.plot(l/10,y, 'c-') #sinh teor blue
	ax.plot(l/10,y1, 'y-') #asinh teor yellow
	ax.plot(l/10,y2, 'm-') #practic sinh purple
	ax.plot(l/10,y3, 'r-') #practic asinh red
	plt.show()

def graf_M_N(ND_sin):
	fig, ax = plt.subplots()
	l = np.linspace(0, 10, num = 10, endpoint=False)
	y = (l/10*(2-l/10))/(2*(1-l/10)) #sinh teor black
	k = 1
	y1 = for_oc_y(ND_sin,k)
	ax.plot(l/10,y, 'k-') #black
	ax.plot(l/10, y1, 'm-') #purple
	plt.show()

def genT (l, reqs):
	T = 0
	i = 0
	line_t = []
	while i < reqs:
		u = random.random() #[0..1]
		T = T-math.log(u)/l
		T = round(T, 2)
		T = round(T, 2)
		line_t.append(T)
		i += 1
	return line_t

def M_D (d, reqs):
	i = 0
	sumD = 0
	while i < len(d):
		sumD += d[i]
		i += 1
	#print ("M[d] = ", sumD/reqs)
	return (sumD/reqs)

def M_N(n_reqs, t_work):
	i = 0
	sum_reqs = 0
	while i < len(n_reqs):
		sum_reqs += n_reqs[i]
		i +=1
	#print ("M[N] = ", sum_reqs/t_work)
	return (sum_reqs/t_work)

def check_queue(queue, t_work):
	n = 0
	if len(queue) != 0 :
		i = 0
		while i < len(queue):
			if queue[i] < t_work:
				n += 1
			i += 1
	else: n = 0
	return n

def sinsys (reqs, l, line_t):#####synchronous system#####
	T = 0
	t_work = 0
	queue = [] #queue sin system
	d = []
	n_reqs =[]
	areqs = reqs
	send_reqs = 0
	j = 0
	mass_ND = []
	while send_reqs != reqs:
		if areqs != 0:
			queue.append(line_t[j])
			areqs -= 1
			j += 1
		if queue[0] <= t_work:
			#print ("send in win: "+str(t_work)+" | "+str(queue[0]))
			t_work += 1
			send_reqs += 1
			d.append(t_work - queue[0])
			queue.pop(0)
		else:
			#print("   not send: "+str(t_work)+" | ")
			t_work += 1
		n_reqs.append(check_queue(queue, t_work))
	mass_ND.append(M_D (d, reqs))
	mass_ND.append(M_N(n_reqs, t_work))
	return mass_ND

def asinsys(reqs, line_t): #####asynchronous system#####
	d = []
	send_reqs = 0
	i = 0
	t = line_t[0]
	aqueue = [] #queue asin system
	while send_reqs != reqs:
		if line_t[i] <= t:
			aqueue.append(line_t[i])
			t += 1
			#print ("send: "+str(aqueue[0])+" | "+str(round(t, 2)))# +" | "+str(aqueue))
			i += 1
			d.append(round((t-line_t[i-1]), 2))
			aqueue.pop(0)
			send_reqs += 1
		else:
			t += 0.001
	return (M_D(d, reqs))

#plot grafs
l = 0.009
ND_sin = []
D_asin = []
line_t = genT (l, reqs)
while l < 1:
	line_t = genT (l, reqs)
	ND_sin.append(sinsys(reqs, l, line_t))
	D_asin.append(asinsys(reqs, line_t))
	l +=0.1
graf_M_N(ND_sin) #call graf MN
graf_M_D(ND_sin, D_asin)#call graf MD