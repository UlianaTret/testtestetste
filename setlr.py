import random
import math
import matplotlib.pyplot as plt
import numpy as np
M = int(input("how subscribers = ")) #subscribers
reqs = 50000
i = 0
t_work = 0
w_interval = M
d = []
nl = []
req_user = []
while i<M:
	req_user.append(0)
	i +=1

def genT (t, l):
	u = random.random()
	t = t-math.log(u)/l
	t = round(t, 1)
	t = round(t, 1)
	return t

def creat_queue(users, t, w_interval):
	n = random.randint(1, M) - 1
	users.append([n, t, random.randint(0, w_interval-1)])# for n user add task t_enter and t_waiting
	req_user[n] +=1
	return users

def creart_users_queue(l, reqs):
	users = []
	t = 0
	while reqs != 0:
		t = genT(t, l)
		users = creat_queue(users, t, w_interval)
		reqs -=1
	users = sorted(users, key=lambda us:us[0])
	return users, req_user

################################################################################
def dec_time(users, t_work, req_user):
	i = 0
	j = 0
	while i < len(users):
		if users[i][1] < t_work and users[i][2] !=0:
			users[i][2] -=1
		i +=req_user[j]
		j +=1
	return users

def find_n(users, req_user):
	i = 0
	n = 0
	j = 0
	while i < len(users):
		if users[i][2]==0:
			n +=1
		i +=req_user[j]
		j +=1
	return n

#success
def success_w(users,d, t_work, send_reqs):
	i = 0
	j = 0
	suc = 0
	while suc != 1 and i < len(users):
		if users[i][2] == 0 and users[i][1] <= t_work and len(users[i]) != 0:
			d.append(t_work-users[i][1]+1)
			req_user[users[i][0]] -=1
			users.pop(i)
			suc = 1
		i +=1
	send_reqs +=1
	return users, send_reqs, t_work

#conflict
def conflict_w(M,W):
	new_W1 = 2*M
	new_W2 = 2*W
	if new_W1 <= new_W2:
		new_w = new_W1
	else: new_w = new_W2
	return new_w

#empty
def empty_w(M,W):
	new_w = round(W/2, 0)
	if new_w <= 1:
		new_w = 1
	return new_w

def new_time(users, w_interval):
	i = 0
	while i < len(users):
		if len(users[i]) != 0:
			if users[i][2] == 0 or users[i][1] > t_work:
				users[i][2] = random.randint(1, w_interval)-1
		i +=1
	return users

def listen_kanal(users, w_interval, t_work, send_reqs):
	if n == 1: #success
		users, send_reqs, t_work = success_w(users,d, t_work, send_reqs)
	if n >= 2: #conflict
		w_interval = conflict_w(len(users),w_interval)
		users = new_time(users, w_interval)
	if n == 0: #empty
		w_interval = empty_w(len(users),w_interval)
		users = new_time(users, w_interval)
	return users, w_interval, send_reqs, t_work

def middle(mas):
	i = 0
	n = 0
	while i < len(mas):
		n +=mas[i]
		i +=1
	return (n)

def check_queue(queue, t_work):
	n = 0
	i = 0
	while i < len(queue):
		if queue[i][1] < t_work and queue[i][2]==0:
			n += 1
		i +=1
	return n

MN = []
MN1 = []
MD = []
lv = []
l = 0.09
while l < 1:
	n = 0
	print (l)
	send_reqs = 0
	t_work = 0
	users, req_user = creart_users_queue(l, reqs)
	d = []
	nl = []
	nl1 = []
	while send_reqs < reqs:
		n = 0
		n = find_n(users, req_user)#raedy users for sending
		nl.append(n)
		n1 = check_queue(users, t_work)#ready message for sending
		nl1. append(n1)
		t_work +=1
		users, w_interval, send_reqs, t_work = listen_kanal(users, w_interval, t_work, send_reqs)
		users = dec_time(users, t_work, req_user)
	MD.append(middle(d)/len(d))
	MN.append(middle(nl)/t_work)
	MN1.append(middle(nl1)/t_work)
	lv.append(send_reqs/t_work)
	l +=0.1

print ("MD = ", MD)
print ("MN = ", MN)
print ("MN1 = ", MN1)

#plor grafs
def plot_MD(MD):#MD
	fig, ax = plt.subplots()
	l = np.linspace(0, 10, num = 10, endpoint=False)
	if M == 1:
		y = (2-l/10)/(2*(1-l/10)) + 0.5 #sinh teor blue
		ax.plot(l/10,y, 'c-') #sinh teor blue
	ax.plot(l/10,MD, 'm-') #practic purple
	plt.title("MD")
	plt.show()

def plot_MN(MN):#MN of users or queue
	fig, ax = plt.subplots()
	l = np.linspace(0, 10, num = 10, endpoint=False)
	if M == 1:
		y = (l/10*(2-l/10))/(2*(1-l/10)) #sinh teor blue
		ax.plot(l/10,y, 'c-') #sinh teor blue
		ax.plot(l/10,MN1, 'm-') #practic purple
	else:
		ax.plot(l/10,MN, 'm-') #practic purple
	plt.title("MN")
	plt.show()

def plot_l(lv):
	fig, ax = plt.subplots()
	l = np.linspace(0, 10, num = 10, endpoint=False)
	ax.plot(l/10,lv, 'm-') #practic purple
	plt.title("l(l)")
	plt.show()

plot_MD(MD)
plot_MN(MN)
if M != 1:
	plot_l(lv)