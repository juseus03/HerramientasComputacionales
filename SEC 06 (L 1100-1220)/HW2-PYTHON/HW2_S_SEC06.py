def reverse(s):
    str=""
    for i in s:
    	str=i+str
    return str

#Punto 1abc
resp=""
a=131
ain=a
b=0

while(a>=1):
    b=a//2
    res=a%2
    resp+=str(res)
    print(a,b,res)
    a=b    
print ain,"en representacion binaria es ",reverse(resp)

#Punto 1d
resp=""
a=2005
ain=a
b=0

while(a>=1):
    b=a//2
    res=a%2
    resp+=str(res)
    print(a,b,res)
    a=b    
print ain,"en representacion binaria es ",reverse(resp)

#Punto 2
#2a
c = 2.0
d = 3.0

print "El valor de c es ",c, " y el valor de d es ",d

#2b
vdiv = int(c/d)
print "La division entera entre c//d es ", vdiv

#2c
div = d/c
int_div = int(d/c)
resid=div-int_div

print "El residuo de d/c es ", resid
