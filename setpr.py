import random
import math
l = float(input("Your lambda = ")) #lambda
reqs = int(input("how requests = ")) #requests
N_cr = (l*(2-l))/(2*(1-l))
d_sin = N_cr/l + 0.5
d_asin = N_cr/l
print("M[N]_sin = ", round(N_cr, 2))
print("d_sin = ", round(d_sin, 2))
print("d_asin = ", round(d_asin, 2))

def genT (l, T):
	u = random.random() #[0..1]
	T = T-math.log(u)/l
	T = round(T, 2)
	T = round(T, 2)
	return T

def M_D (d, reqs):
	i = 0
	sumD = 0
	while i < len(d):
		sumD += d[i]
		i += 1
	print ("M[d] = ", sumD/reqs)

def M_N(n_reqs, t_work):
	i = 0
	sum_reqs = 0
	while i < len(n_reqs):
		sum_reqs += n_reqs[i]
		i +=1
	print ("M[N] = ", sum_reqs/t_work)

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
print("#####synchronous system#####")
T = 0
t_work = 0
queue = [] #queue sin system
aqueue = [] #queue asin system
line_t = []
d = []
n_reqs =[]
areqs = reqs
send_reqs = 0
while send_reqs != reqs:
	if areqs != 0:
		T = genT (l, T)
		queue.append(T)
		areqs -= 1
	if queue[0] <= t_work:
		print ("send in win: "+str(t_work)+" | "+str(queue[0]))
		t_work += 1
		send_reqs += 1
		d.append(t_work - queue[0])
		line_t.append(queue[0])
		queue.pop(0)
	else:
		print("   not send: "+str(t_work)+" | ")
		t_work += 1
	n_reqs.append(check_queue(queue, t_work))
#print ("n_reqs", n_reqs)
M_D (d, reqs)
M_N(n_reqs, t_work)
print("\n#####asynchronous system#####")
d = []
send_reqs = 0
i = 0
t = line_t[0]
while send_reqs != reqs:
	if line_t[i] <= t:
		aqueue.append(line_t[i])
		t += 1
		print ("send: "+str(aqueue[0])+" | "+str(round(t, 2)))# +" | "+str(aqueue))
		i += 1
		d.append(round((t-line_t[i-1]), 2))
		aqueue.pop(0)
		send_reqs += 1
	else:
		t += 0.001
M_D (d, reqs)