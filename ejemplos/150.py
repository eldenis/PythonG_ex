from modulepythong import *
#VARIABLES DE AMBIENTE
tamamb=500
window_size(500,500)
window_coordinates(0,0,tamamb,tamamb)

#datos de barrita
b_anch=80
b_alt=10
x=(tamamb/2)-(b_anch/2)
y=35
impulso_x=0.035

#DATOS DE BOLITA
velx=0.02
vely=0.01
radio=5
color="white"
bolx=240
boly=400
dirx=0#dirx indica la direccion a la que se dirige la bola horizontalmente 0 hacia izquierda, 1 hacia derecha
diry=0#diry indica la direccion a la que se dirige la bola verticalmente 0 para abajo, 1 para arriba

#datos de juego
perdio=False

#ELEMENTOS DE AMBIENTE
tambar=5
tamtec=10#tamaño del techo
limizqbar=tambar+1
limderbar=tamamb-tambar-b_anch-1
limizqbol=limizqbar+3
limderbol=limderbar+75
limsupbol=tamamb-tamtec-5
liminfbol=b_alt+15
create_filled_rectangle(0,0,tamamb,tamamb,'black','black')
create_filled_rectangle(0,tamamb,tambar,0,'purple','purple')
create_filled_rectangle(tamamb,tamamb,tamamb-tambar,0,'purple','purple')
create_filled_rectangle(0,tamamb,tamamb,tamamb-tamtec,'white','red')

barrita= create_filled_rectangle(x,y,x+b_anch,y-b_alt,'blue','blue')
bolita=create_filled_circle(bolx,boly,radio,color)    

print "Presione la tecla Escape para salir"

while (keypressed(1) != 'Escape') and (perdio==False):

  if keypressed(1) =='Left':  
    if x>limizqbar:
      move(barrita,-impulso_x,0)
      x-=impulso_x

  if keypressed(1) =='Right':  
    if x<limderbar:
      move(barrita,impulso_x,0)
      x+=impulso_x

      
  if dirx==0:
    #va hacia la izquierda
    if diry==0:      
      #va pa abajo
      move(bolita,-velx,-vely)
      bolx-=velx
      boly-=vely
    else:
      #va pa arriba
      move(bolita,-velx,vely)
      bolx-=velx
      boly+=vely
  else:
    #va hacia la derecha
    if diry==0:    
      #va pa abajo
      move(bolita,velx,-vely)
      bolx+=velx
      boly-=vely
    else:
      #va pa arriba
      move(bolita,velx,vely)
      bolx+=velx
      boly+=vely
  
  if bolx<=limizqbol:#choca con la pared izquierda
    dirx=1#cambiar la direccion a la derecha
  elif bolx>=limderbol:
    dirx=0#cambiar la direccion a la izquierda 

  if (boly>liminfbol) and (boly<=liminfbol+10):
    if (bolx>=x) and (bolx<=b_anch+x):
      diry=1

  if boly>=limsupbol:#choca con el techo
    diry=0    
  elif boly<=liminfbol:#paso por debajo de la barra
    perdio=True
   
  
if (perdio==True):
  erase (bolita)
  create_filled_rectangle(30,425,450,380,'lightblue')
  create_text(240,400,"LOSER!!!",20)

create_filled_rectangle(100,325,385,360,'yellow')
create_text(240,340,"Adios!!!")