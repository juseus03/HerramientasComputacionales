#Definicion de la clase
class Pelota:
  #Metodo constructor
  def __init__(self,v0,g):
    self.v0 = v0
    self.g = g
  def posActualY(self,t):
    return self.v0*t-0.5*self.g*t**2
  def mensaje(self):
    return "v0=",self.v0,"m/s y g=",self.g,"m/s2"

#Punto 2
t=[]
h=0.01
##i debe ir entre 0 y 201 para que t vaya de 1 a 3
for i in range(0,201):
  t.append(1+h*i)

#Punto 3
v0 = 3
g = 1.62 #Gravedad de la luna
p1 = Pelota(v0,g)
y=[] #Lista de posiciones de p1
for tt in t:
  y.append(p1.posActualY(tt))

#Bono
print "Para y(t)=v0*t-0.5*g*t**2 con",p1.mensaje(),"se obtiene:"
print "-----------------------"
print "t,y(t)"
print "-----------------------"
for i in range(0,len(t)):
  print t[i],",",y[i]