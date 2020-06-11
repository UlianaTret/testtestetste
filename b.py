import random

print ("lab")
otvet = int(input("g and m in dec-2 or bin-1? "))
def notstr(k):
	n = len(k)
	b = 0
	for i in range(n):
		if k[i] == '1':
			b = b + 2 ** (n - 1 - i)
	return b

if otvet == 1:
	g = input("Your g: ")
	g = notstr(list(g))
	m = input("Your m: ")
	m = notstr(list(m))
else:
	g = int(input("Your g: "))
	m = int(input("Your m: "))

pr = float(input("Your pr: "))
l = int(input("Your l: "))
k = int(input("Your k: "))
c = 0

#KODER
print ("\nKODER\n")
print("g = ", bin(g))
print("m = ", bin(m))
#c0 = m(x)*x^deg(g(x))
#deg(g(x)) in bin
degg01 = bin(int(g))[2:]
dlinag = len(list(bin(int(g))[2:]))
degg = dlinag - 1
print ("degg = ", degg)
r = degg
n = k + r + l
c0 = m << degg
print ("c0 = ", bin(c0))
m = c0

#for_XOR
sdvig = len(list(bin(m))) - len(list(bin(g)))
def stepenc0 (c0):
	degc0 = len(list(bin(c0))) - 3
	return degc0

#XOR
def xorim(c0, g, sdvig):
	gnew = g << sdvig
	c0 = c0 ^ gnew
	degc0 = stepenc0 (c0)
	
	if degc0 >= degg:
		sdvig = degc0 - degg
		c0 = xorim (c0, g, sdvig)
	return c0

c = xorim(c0, g, sdvig)
print ("c = ", bin(c))
a = c0 + c
print ("a = ", bin(a))

#ALL EEEE

print("\ne c A:")
def knoww(num):
	forwg = bin(num)
	i = 0
	wres = 0
	for i in range(len(forwg)):
		if forwg[i] == '1':
			wres += 1
	return wres
koda = 1
minw = 10000
for i in range((2 ** k) - 1):
	koda00 = koda << r
	sdvig = len(list(bin(koda00))) - len(list(bin(g)))
	Sa = xorim(koda00, g, sdvig)
	wordA = koda00 + Sa
	wWordA = knoww(wordA)
	if wWordA < minw:
		minw = wWordA
	koda += 1
	
def dobavit00(num, dlinae):
	e = str(bin(num))
	e = e[2:]
	#print (e)
	while len(e) != dlinae:
		e = '0' + e
	return (e)

# d - 1
d = minw - 1
print("d - 1 = ", d)
#gen e
kode = 1
dlinae = l + k + r
ekl = l + k
for i in range((2 ** ekl) - 1):
	kode00 = kode << r
	sdvig = abs(len(list(bin(kode00))) - len(list(bin(g))))
	Sekot = xorim(kode00, g, sdvig)
	wordAe = kode00 + Sekot
	wWordAe = knoww(wordAe)
	if wWordAe < minw:
		eca = dobavit00(wordAe, dlinae)
		print(eca)
	kode += 1
########


#KANAL
print ("\nKANAL\n")
#e
n = len(list(bin(a))) - 2
i = 0
j = 0
err = [] #empty
for j in range(l):
	err.append('0')

for i in range(n):
	chislo = random.random() # [0..1]
	if chislo < pr:
		err.append('1')
	else:
		err.append('0')
print ("e = ", err)

#add 00 a
i = 0
anew = list(bin(a))
del anew[0]
del anew[0]
for i in range(l):
	anew.insert(0, '0')

#b = a + e
b01 = anew
print ("a = ", b01)
for i in range(n):
	if err[i] == '1':
		if b01[i] == '1':
			b01[i] = '0'
		else:
			b01[i] = '1'
print ("b = ", b01)
#num from list b01
b = notstr(b01)


#DEKODER
print ("\nDEKODER\n")
n = l + k + r
bk = dobavit00(b, n)
print ("b = ", bk)

#S(x) = b(x) mod g(x)
sdvig = len(list(bin(b))) - len(list(bin(g)))
s = xorim(b, g, sdvig)
print("\ns = ", bin(s))
if s == 0:
	print ("no error")
	gnew = g << sdvig
	md = b >> (len(list(bin(g))) - 3)
	print("Your message: ", md)
	print("Your message: ", bin(md))
else: 
	print ("were errors in the KANAL")