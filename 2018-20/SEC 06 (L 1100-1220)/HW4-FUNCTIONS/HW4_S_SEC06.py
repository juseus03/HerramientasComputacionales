#Punto 1a
def sumaPares(num):
    sum=[]
    if(len(num)==1):
        return num
    else:
        for i in range(len(num)):
            if(i+1<len(num)):
                sum.append(int(num[i])+int(num[i+1]))
        return sum

num=[1,2,3,4]
print "La suma por pares de",num,"es: ",sumaPares(num)

#Punto 1b
def Pascal(n):
    if(n==0):   #Caso para n=0
        print 1
        return [1]
    elif(n==1): #Caso base
        print [1]
        print [1,1]
        return [1,1]
    else:   #Caso REcursivo
        res = [1]+sumaPares(Pascal(n-1))+[1]
        print res
        return res

#Llamado a la función
n=10
Pascal(n)
        
