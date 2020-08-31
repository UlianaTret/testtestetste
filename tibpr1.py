import math
e = int(input("e = "))
p = int(input("p = "))
q = int(input("q = "))
l = (p-1)*(q-1)
n = p*q
d = 0
while (e*d)%l != 1:
	d += 1
print ("find d = ", d)

m = int(input("m = "))
cr_m = (m**e)%n
print ("cript message: ", cr_m)
decr_m = (cr_m**d)%n
print ("decript message: ", decr_m)