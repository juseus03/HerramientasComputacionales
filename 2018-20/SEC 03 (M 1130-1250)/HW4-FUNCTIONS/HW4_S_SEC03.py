#Punto 1
def mcd(m,n):
    r = m%n
    if(r==0):   #Caso base
        return n
    else:
        return mcd(n,r)

m=60
n=40
print "MCD de m=",m,"y n=",n,"es:",mcd(m,n)

#Punto 2
def sumDig(num):
    numStr=str(num)   #COnversion del numero a string
    if(len(numStr)==1):
        return num
    else:
        return int(numStr[0])+sumDig(int(numStr[1:]))
    
input = 2002
print "El input es",input
print "El resultado es", sumDig(input)

        
