import random

print ("lab")
g = int(input("Your g: "))
m = int(input("Your m: "))
pr = float(input("Your pr: "))
print ("Your g: ", bin(g))
print ("Your m: ", bin(m))
k = 4
c = 0


#KODER
print ("\nKODER\n")
print("g = ", bin(g))
print("m = ", bin(m))
#c0 = m(x)*x^deg(g(x))
#deg(g(x)) in bin
degg01 = bin(int(g))[2:]
dlinag = len(list(bin(int(g))[2:]))
#print ("dlinag = ", dlinag)
degg = dlinag - 1
print ("degg = ", degg)
c0 = m << degg
print ("c0 = ", bin(c0))
m = c0


#for_XOR
sdvig = len(list(bin(m))) - len(list(bin(g)))
def stepenc0 (c0):
	degc0 = len(list(bin(c0))) - 3
	#print ("degc0 = ", degc0)
	return degc0


#XOR
def xorim(c0, g, sdvig):
	gnew = g << sdvig
	c0 = c0 ^ gnew
	#res = c0
	#print ("resxor = ", bin(c0))
	# call deg c0
	degc0 = stepenc0 (c0)
	
	if degc0 >= degg:
		sdvig = degc0 - degg
		#gnew = g << sdvig
		c0 = xorim (c0, g, sdvig)
	#print ("c = c0 mod g = ", c0)
	return c0

c = xorim(c0, g, sdvig)

print ("c = ", bin(c))
a = c0 + c
print ("a = ", bin(a))
#KANAL
print ("\nKANAL\n")
#e
n = len(list(bin(a))) - 2
i = 0
err = list(bin(a))
del err[0]
del err[1]
for i in range(n):
	chislo = random.random() # [0..1]
	if chislo < pr:
		err[i] = '1'
	else:
		err[i] = '0'
print ("e = ", err)
#b = a + e
b01 = list(bin(a))
#print ("b01 = ", b01)
del b01[0]
del b01[0]
print ("a = ", b01)

for i in range(n):
	if err[i] == '1':
		if b01[i] == '1':
			b01[i] = '0'
		else:
			b01[i] = '1'

print ("b = ", b01)

#num from list b01
n = len(b01)
b = 0
for i in range(n):
	if b01[i] == '1':
		b = b + 2 ** (n - 1 - i)
# end creat b

#DEKODER
print ("\nDEKODER\n")
#print ("b = ", b)
print ("b = ", bin(b))

#S(x) = b(x) mod g(x)

#for_XOR
sdvig = len(list(bin(b))) - len(list(bin(g)))


#XOR
s = xorim(b, g, sdvig)
print("s = ", bin(s))

if s == 0:
	print ("no error")
	decoder = "no error"
	gnew = g << sdvig
	md = b >> (len(list(bin(g))) - 3)
	print("Your message: ", md)
else: 
	print ("were errors in the KANAL")
	decoder = "were errors in the KANAL"

#WRITE RESULT
#otvet = input("save?")
#if otvet == 'y':
	#f = open('test.txt','w')
	#f.write('g: ' + bin(g) + '\n')
	#f.write('m: ' + bin(m) + '\n')
	#f.write('s: ' + bin(s) + '\n')
	#f.write('decoder: ' + decoder + '\n')

