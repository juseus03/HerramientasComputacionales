#Punto 1
a = "demencia"
aInv = a[::-1]
print "Al invertir",a,"se obtiene",aInv

#Punto 2
b = "Hola, como estas"
bSplit = b.split()

bInv = "X" #Marca al incio del mensaje
for palabra in bSplit:
    bInv +=palabra[::-1]+" "    #Inversion
bInv += "X" #Marca al final del mensaje
print "Al invertir",b,"se obtiene",bInv

#Punto 3
c = "El castigo mas justo es aquel que uno mismo se impone"
cSplit = c.split()

cInv = "X" #Marca al incio del mensaje
for palabra in cSplit:
    cInv +=palabra[::-1]+" "    #Inversion
cInv += "X" #Marca al final del mensaje

print "msjOrig:",c
print "msjCod:",cInv

#Punto 4

fileRead = open("text4.txt","r")    #Archivo de lectura
inlines = fileRead.readlines()

fileWrite = open("rText4.txt","w")

#Decodificacion
msj = ""
for line in inlines:
    lsplit = line.split()
    for palabra in lsplit:
        pal =palabra[::-1]
        if(pal=="X"):   #Limpiar las marcas del mensaje
            break
        elif(pal[-1]=="X"):
            msj+=pal[:-1]+" "
        else:
            msj+=pal+" "
    msj+="\n"

#Escribe el mensaje en el archivo de texto
fileWrite.writelines(msj)    
fileWrite.close()
