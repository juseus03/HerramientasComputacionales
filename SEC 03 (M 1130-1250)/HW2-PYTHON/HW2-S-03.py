#Punto 1
a=100 #Limite superior
n=1 #Limite inferior

print "Divisores de ",a,":" #Mensaje inicial

while(n<=a):
    if(a%n==0):
        print n
    n+=1

#Punto 2
#2a y 2b
def divisores(x,p): #Funcion que calcula e imprime los divisores de un numero x
    if(p):
        print "Divisores de ",x,":"
    suma = 0
    n=1
    while(n<x):
        if(x%n==0):
            if(p):
                print n
            suma+=n
        n+=1
    return suma
    
a=220
b=284

sumaA=divisores(a,True) 
sumaB=divisores(b,True)

if(sumaA==b and sumaB==a):  #Verifica si a y b son numeros amigos
    print "Los numeros ",a," y ",b," son numeros amigos"
else:
    print "Los numeros ",a," y ",b," no numeros amigos"


#2c
a=1184
b=1210

sumaA=divisores(a,False)
sumaB=divisores(b,False)

if(sumaA==b and sumaB==a):  #Verifica si a y b son numeros amigos
    print "Los numeros ",a," y ",b," son numeros amigos"
else:
    print "Los numeros ",a," y ",b," no numeros amigos"
