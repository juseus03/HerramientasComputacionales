#Clase roca
class Roca:
  def __init__(self,pTipo,pSubTipo,pTamano):
      self.tipo = pTipo
      self.subTipo = pSubTipo
      self.tamano = pTamano
  def darTipo(self):
    return self.tipo
  def darSupTipo(self):
    return self.subTipo
  def darTamano(self):
    return self.tamano
  def cambiarTipo(self,nTipo):
    self.tipo = nTipo

#Punto 2
totalRocas = 300
h=0.01
t=[]
for i in range(0,totalRocas):
  t.append(0.1+h*i)

#Punto 3
rocas=[]
for i in range(0,totalRocas):
  if(i<=totalRocas*0.5):
    if(i%2==0):
      rocas.append(Roca("Ignea","Volcanicas",t[i]))
    else:
      rocas.append(Roca("Ignea","Plutonicas",t[i]))
  elif(i<=totalRocas*0.8):
    rocas.append(Roca("Sedimentarias","N/A",t[i]))
  else:
    rocas.append(Roca("Metamorficas","N/A",t[i]))

#Bono
prIgnea,prSed,prMet = 0,0,0
contIgnea,contSed,contMet = 0,0,0
##Cuenta y acumula los tamanos de las rocas segun su tipo
for roca in rocas:
  if roca.darTipo()=="Ignea":
    prIgnea+=roca.darTamano()
    contIgnea+=1
  elif roca.darTipo()=="Sedimentarias":
    prSed+=roca.darTamano()
    contSed+=1
  else:
    prMet+=roca.darTamano()
    contMet+=1
##Calculo promedio
prIgnea=prIgnea/contIgnea
prSed=prSed/contSed
prMet=prMet/contMet

##Mensaje
if(prIgnea>=prSed and prIgnea>=prMet):
  print "Tipo: Roca Ignea, Tamano Promedio=",prIgnea
elif(prSed>=prMet):
  print "Tipo: Roca Sedimentarias, Tamano Promedio=",prSed
else:
   print "Tipo: Roca Metamorficas, Tamano Promedio=",prMet
