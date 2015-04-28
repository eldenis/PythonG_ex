#Introducir por teclado el numero de personas con cada una
#de las calificaciones a continuacion
#Suspenso (Sus), Aprobado (Apr), Notable (Not), Sobresaliente (Sob)
#Y mostrar un grafico de barras que represente la informacion

window_size(500,500)
window_coordinates(0,0,100,120)

suspensos=int(raw_input("Introduzca el numero de estudiantes suspensos: "))
aprobados=int(raw_input("Introduzca el numero de estudiantes aprobados: "))
notables=int(raw_input("Introduzca el numero de estudiantes notables: "))
sobresalientes=int(raw_input("Introduzca el numero de estudiantes sobresalientes: "))

valores=[suspensos,aprobados,notables,sobresalientes]
nombres=["Sus","Apr","Not","Sob"]
total=0
for v in valores: total+=v

y=10
x=19
dl=10
cont=1

for v in valores:
  val=(float(v)*100)/float(total)
  create_line(x*cont,y,x*cont,y+val)
  create_line(x*cont+dl,y,x*cont+dl,y+val)
  create_line(x*cont+dl,y,x*cont,y)
  create_line(x*cont+dl,y+val,x*cont,y+val)
  create_text(x*cont+5,y-2,nombres[cont-1],8)
  create_text(x*cont+5,val+y+2,"%0.2f%%"%val,8)
  cont+=1