#Punto 1
lista=[1,2,3,-5,-6,10]

#a
res=0
for num in lista:
    res+=num
print "sum(",lista,")=",res

#b
res=1
for num in lista:
    res*=num
print "prod(",lista,")=",res

#Punto 2
input1="(a+b" #"(a+b*(c/d)\%(f+g))"
cAbiertos = 0
cCerrados = 0
#Cuenta la cantidad de parentesis
for c in input1:
    if(c=="("):
        cAbiertos+=1
    elif(c==")"):
        cCerrados+=1
if(cAbiertos==cCerrados):
    print "La sintaxis es correcta"
else:
    print "La sintaxis es incorrecta"
