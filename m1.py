import math
import matplotlib.pyplot as plt
import numpy as np
v0 = float(input("    V0: "))
hg = float(input("h goal: "))
hb = float(input("h ball: "))
s = float(input("     s: "))
g= 9.8
da = 0
def popal(an,t):
	print("popal")
	print("alfa: ", an*180/math.pi)
	tn=s/(v0 * math.cos(an))
	fig, ax = plt.subplots()
	x = np.linspace(0, tn, 100)
	y = (v0 * x * math.sin(an))-((g*x*x)/2)
	ax.plot(x,y)
	plt.show()


if v0*s == 0:
	print ("miss: your ball fell down")
else:
	h = math.fabs(hg - hb)
	alf = math.atan(h/s)
	alfa = 0
	da = 0
	size = float(input("size goal: "))
	while alfa <= 1.57:
		t = s/(v0 * math.cos(alfa))
		x = v0 * t * math.cos(alfa)
		y = v0 * t * math.sin(alfa)-((g*t*t)/2)
		if (y>=h-(size/2))&(y<=h+(size/2))&(x==s):
			popal(alfa, t)
			an = alfa
			da = 1
		alfa = alfa + 0.0174533/2

if da == 0:
	print ("you'll never reach the goal")