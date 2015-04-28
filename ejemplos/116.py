#programa que permita operar con dos vectores
from math import sqrt,acos,pi

def menu():
  opc=0
  while (opc<1 or opc>9):
    clear_output()
    print "1) Introducir el primer vector"
    print "2) Introducir el segundo vector"
    print "3) Calcular la suma"
    print "4) Calcular la diferencia"
    print "5) Calcular el producto escalar"
    print "6) Calcular el producto vectorial"
    print "7) Calcular el angulo (en grados) entre ellos"
    print "8) Calcular la longitud"
    print "9) Finalizar\n"
    opc= int(raw_input("Opcion: "))
  return opc

def vector():
  vec=[]
  vec.append(float(raw_input("Introduzca x: ")))
  vec.append(float(raw_input("Introduzca y: ")))
  vec.append(float(raw_input("Introduzca z: ")))  
  return vec

def suma(v1,v2):
  return [v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2]]

def diferencia(v1,v2):  
  return [v1[0]-v2[0],v1[1]-v2[1],v1[2]-v2[2]]

def pescalar(v1,v2):
  return [v1[0]*v2[0],v1[1]*v2[1],v1[2]*v2[2]]  

def pvectorial(v1,v2):
  vtmp=[0,0,0]
  vtmp[0]=(v1[1]*v2[2])-(v1[2]*v2[1])
  vtmp[1]=(v1[2]*v2[0])-(v1[0]*v2[2])
  vtmp[2]=(v1[0]*v2[1])-(v1[1]*v2[0])  
  return vtmp

def angulo(v1,v2):
  partA=0.0;partB=0.0;partC=0.0;sol=0.0
  partA=(v1[0]+v2[0])+(v1[1]+v2[1])+(v1[2]+v2[2])
  partB=sqrt((v1[0]**2)+(v1[1]**2)+(v1[2]**2))
  partC=sqrt((v2[0]**2)+(v2[1]**2)+(v2[2]**2))  
  sol=partB*partC
  sol=partA/sol  
  sol=acos(sol)
  sol=180*sol
  return sol/pi

def longitud(v1):
  return sqrt((v1[0]**2)+(v1[1]**2)+(v1[2]**2))

#INICIO DEL PROGRAMA
v1=[1.0,2.0,3.0]
v2=[2.0,3.0,4.0]
opc=0
sel=0
while (opc !=9):
  opc=menu()
  
  if opc==1:
    v1=vector()


  elif opc==2:
    v2=vector()


  elif opc==3:    
    #SUMA
    print "El resultado de la suma fue:",suma(v1,v2)
    print "Presione enter ..."
    raw_input()
    


  elif opc==4:
    #DIFERENCIA
    sel=0
    while sel!=1 and sel!=2:
      print "1)Primer vector menos segundo vector"
      print "2)Segundo vector menos primer vector"
      sel=int(raw_input("\nSeleccion: "))      
    if sel !=2:      
      print "El resultado de la diferencia es:",diferencia(v1,v2)
    else:
      print "El resultado de la diferencia es:",diferencia(v2,v1)   
    print "Presione enter ..."
    raw_input()      
    


  elif opc==5:    
    #PRODUCTO ESCALAR
    print "El resultado del producto escalar fue:",pescalar(v1,v2)
    print "Presione enter ..."
    raw_input()    
    


  elif opc==6:
    #PRODUCTO VECTORIAL
    sel=0
    while sel!=1 and sel!=2:
      print "1)Primer vector menos segundo vector"
      print "2)Segundo vector menos primer vector"
      sel=int(raw_input("\nSeleccion: "))      
    if sel !=2:      
      print "El resultado del producto vectorial es:",pvectorial(v1,v2)
    else:
      print "El resultado del producto vectorial es:",pvectorial(v2,v1)   
    print "Presione enter ..."
    raw_input()      
    


  elif opc==7:    
    #ANGULO
    print "El resultado del angulo fue:",angulo(v1,v2)
    print "Presione enter ..."
    raw_input()        



  elif opc==8:
    #LONGITUD
    sel=0
    while sel!=1 and sel!=2:
      print "1)VECTOR 1"
      print "2)VECTOR 2"    
      sel=int(raw_input("\nSeleccion: "))      
    if sel !=2:      
      print "La longitud del vector es:",longitud(v1)
    else:
      print "La longitud del vector es:",longitud(v2)
    print "Presione enter ..."
    raw_input()        


  elif opc==9:
    print "Adios...!"
    
