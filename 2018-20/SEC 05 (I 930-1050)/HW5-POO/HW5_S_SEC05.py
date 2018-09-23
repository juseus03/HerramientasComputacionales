#Clase modela el circulo
class Circulo:
  pi=3.14159  #Variable de la clase para modelar pi

  def __init__(self,x0,y0,r0):#Metodo constructor
      self.x = x0
      self.y = y0
      self.R = r0

  def darArea(self):
      return self.pi*self.R**2
  
  def darArco(self,theta):
      return theta*self.R
  
  def moverX(self,x0):
      self.x = x0

  def moverY(self,y0):
      self.y = y0
      
  
  def imprimir(self):
      print "(X,Y)=(",self.x,",",self.y,") y R=",self.R

#Punto 2
nPasosX = 100
nPasosY = 50
x0,y0 = 3,9
R=3
circulo1 = Circulo(x0,y0,R)
circulo1.imprimir()

##En este caso primero se hacen los pasos en Y y luego en la coordenada X
for y in range(1,nPasosY+1):
    circulo1.moverY(y0-y)
    circulo1.imprimir()
for x in range(1,nPasosX+1):
    circulo1.moverX(x0+x)
    circulo1.imprimir()

#Bono
nPasos = 100
h = 2*3.14159/nPasos
i = 0

while(i<=nPasos):
    theta = h*i
    arco = circulo1.darArco(theta)
    print "theta = ",theta," , arco = ",arco
    i+=1
