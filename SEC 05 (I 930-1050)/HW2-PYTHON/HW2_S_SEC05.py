#Punto 1
a = 20
n = 1

while(n<=a):
    k=1
    esPrimo = True
    while(k<=n):
        if(n%k==0 and (n!=k and k!=1)):
            esPrimo = False
            break
        k+=1
    if(esPrimo):
        print n
    n+=1

#Punto 2
n=12
pasos = 0
print "Secuencia para ",n,":"
print n
while(n>1):
    pasos+=1
    if(n%2==0):
        n=n/2
    else:
        n=3*n+1
    print n 
print "El numero de pasos es ",pasos

#2c
def siracusa(x):
    pasos=0
    while(x>1):
        pasos+=1
        if(x%2==0):
            x=x/2
        else:
            x=3*x+1
    return pasos

n1=19
n2=27
n3=100
print "Para n=",n1," el numero de pasos es ",siracusa(n1)
print "Para n=",n2," el numero de pasos es ",siracusa(n2)
print "Para n=",n3," el numero de pasos es ",siracusa(n3)
    
