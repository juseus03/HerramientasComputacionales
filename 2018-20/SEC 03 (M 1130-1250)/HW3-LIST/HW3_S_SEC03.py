#Punto 1
input1 = "abcdyjavierlkjmn"
ind = input1.index("javier")
print input1[ind:ind+6],"se encuentra en la posicion",ind,"de",input1

#Punto 2
#a
h=0.01
t=[]
y=[]
v0=1
g=9.8

#b
for i in range(1,201):
    t.append(1+i*h)
#c
for i in range(len(t)):
    y_t=v0*t[i]-0.5*g*(t[i]**2)
    y.append(y_t)

#d
print "-----------------"
print "t,y"
print "-----------------"
for i in range(len(t)):
    print t[i],",",y[i]
