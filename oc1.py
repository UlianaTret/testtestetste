import math
import random
print ("how many processes will there be?")
kolvo = int(input())
i = 0
bg = 0 #time of activation
tcpu = 0 #time work on task
pr = 0 #priority
alltask = [] #all tasks for cpu
list_cpu = [] #ready tasks
workcpu = 0 #cpu free
max_pr = 0 # max priority
need_time = 10 # max time of activation 1st task
while kolvo !=0: # write data about task
	print("\nwrite data about task No", i)
	bg = random.randint(1,5)
	print("moment b -> g: ", bg)
	tcpu = random.randint(1,10)
	print("time cpu to complete the task:", tcpu)
	print("rate the priority from 1 to 10")
	pr = int(input("priority: "))
	#save data
	task = [i, bg, 0, tcpu, pr, 0, 0]
	need_time = need_time + task[3] #the maximum processor time
	alltask.append(task)
	kolvo-=1
	i+=1
#print ("thats all\n",alltask)
tcpu = 0 #zero before work cpu
###########increment bg every task##############################################
def inc_task(alltask, tcpu):
	i = -1
	n = len(alltask) - 1
	while i < n:
		i += 1
		alltask[i][2] += 1
		if alltask[i][1] == alltask[i][2]:
			alltask[i][5] = 1 #ready task No i
	return alltask
##########creat queue of tasks##################################################
def queue_task(alltask):
	list_cpu.clear()
	i = -1
	n = len(alltask) - 1
	while i < n:
		i +=1
		if alltask[i][5] == 1 and alltask[i][6] == 0:
			list_cpu.append(alltask[i][0])
	return list_cpu
#######looking for a task with the max priority#################################
def find_max(alltask):
	iw = -1
	i = -1
	max_pr = 0
	n = len(alltask) - 1
	while i < n:
		i+=1
		if alltask[i][5] == 1:
			if alltask[i][4] > max_pr:
				iw = i
	return iw
######work cpu##################################################################
print ("t cpu", tcpu)
while tcpu <= need_time:
	#inc all task and find max priority from ready task
	alltask = inc_task(alltask, tcpu)
	if workcpu == 0:
		tcpu += 1
		iw = find_max(alltask) #looking for a task with max priority
		if iw != -1:
			workcpu = 1
	#to do ready task
	if workcpu == 1:
		alltask[iw][6] = 1 #remove task from queue_task
		while alltask[iw][3] != 0:# work with task
			list_cpu = queue_task(alltask)
			print ("t cpu", tcpu, ": in progress task No",alltask[iw][0], ", in queue", list_cpu)
			alltask[iw][3] -=1
			alltask = inc_task(alltask, tcpu)
			iwn = find_max(alltask)
			if iwn != iw:
				alltask[iw][6] = 0 #return task in queue_task
				alltask[iwn][6] = 1 #remove task from queue_task
				iw = iwn
			tcpu +=1
		tcpu-=1
		if alltask[iw][3] == 0: #remove done task
			alltask.pop(iw)
			kolvo -= 1
	else:
		print ("t cpu", tcpu)
	workcpu = 0 #nullify for next task
	max_pr = 0 #nullify for next task