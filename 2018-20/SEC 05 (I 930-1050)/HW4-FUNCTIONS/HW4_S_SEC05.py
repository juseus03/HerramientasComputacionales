#Punto 1
codigo = "for(int i = 0; i<100; i++){if(lista[i]<=3){print(i)};else{print(0);}}"

def filtro(inp):
    res=""
    for c in inp:
        if(c=="{" or c=="}"):
            res+=c
    return res

#Punto 2
def borrar(inp):
    resp=""
    pos = inp.find("{}")
    if(pos == -1):
        return inp
    else:
        for i in range(len(inp)):
            if(i!=pos and i!=pos+1):
                resp+=inp[i]
        return resp

#Punto 3
def recursive_borrar(inp):
    resp = ""
    pos = inp.find("{}")
    if(pos == -1):
        return inp
    else:
        for i in range(len(inp)):
            if(i!=pos and i!=pos+1):
                resp+=inp[i]
        return recursive_borrar(resp)

#Resultado final
fcod=filtro(codigo)
if(recursive_borrar(fcod)==""):
    print "El programa revisado es correcto"
else:
    print "El programa revisado es incorrecto"
