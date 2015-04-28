from math import sin, cos, pi
# Paisaje
altura_paisaje = 400
anchura_paisaje =400
window_coordinates(0, 0, anchura_paisaje, altura_paisaje)
window_size(500,500)

# Gravedad
g = 0.00001

# Nave
tamanyo_nave = 10
x = anchura_paisaje / 2
y = altura_paisaje - 100
vy = 0
impulso_y = 2*g
impulso_x = 0.00001
vx = 0
nave = create_filled_rectangle(x, y, x+tamanyo_nave, y+tamanyo_nave, 'blue')

# Plataforma
px = anchura_paisaje / 2
py = 0
vpx = .05
anchura_plataforma = 40
altura_plataforma = 3

plataforma = create_rectangle(px, py,
            px+anchura_plataforma, py+altura_plataforma, 'red')

# Tanque de combustible
fuel = 1000
consumo = 0.1
create_rectangle(0,altura_paisaje, 10, altura_paisaje-100, 'black')
lleno = create_filled_rectangle(1,altura_paisaje, 9, altura_paisaje-fuel/10, 'green')

create_text(25, altura_paisaje-8, '0%', 10, 'W')
create_text(30, altura_paisaje-95, '100%', 10, 'W')
# Dial de velocidad
create_circle(anchura_paisaje-50, altura_paisaje-50, 50, 'black')

#PEDIR AL USUARIO DIFICULTAD
print "Dificultad del juego?\n"
print "F. FACIL"
print "M. MEDIO"
print "D. DIFICIL"

dif =""
while dif not in ['F','f','D','d','m','M']:
  dif=raw_input("Seleccion:")
#CAMBIOS DE DIFICULTAD
if dif in ['f','F']:
  consumo = 0.08
  vpx = .04
  g = 0.000008
  plat_viej=plataforma
  anchura_plataforma = 60
  plataforma = create_rectangle(px, py,
            px+anchura_plataforma, py+altura_plataforma, 'red')
  erase(plat_viej)
  
elif dif in ['d','D']:
  g = 0.000013
  consumo = 0.2
  vpx = .10
  plat_viej=plataforma
  anchura_plataforma = 30
  plataforma = create_rectangle(px, py,
            px+anchura_plataforma, py+altura_plataforma, 'red')
  erase(plat_viej)


#FIN DE CAMBIOS DE DIFICULTAD


for i in range(0, 360, 10):
  create_line(anchura_paisaje-50 + 40 * sin(i*pi/180), \
            altura_paisaje-50 + 40 * cos(i*pi/180), \
            anchura_paisaje-50 + 50 * sin(i*pi/180), \
            altura_paisaje-50 + 50 * cos(i*pi/180))

  if i % 30 == 0:
    create_text(anchura_paisaje-50 + 30 * sin(i*pi/180), \
          altura_paisaje-50 + 30 * cos(i*pi/180), str(i), 5, 'CENTER')

aguja = create_line(anchura_paisaje-50, altura_paisaje-50, \
        anchura_paisaje-50 + 50 * sin(0*pi/180), \
        altura_paisaje-50 + 50 * cos(0*pi/180), 'blue')

# Simulacion
while y > 0 and y < altura_paisaje and x > 0 and x < anchura_paisaje - tamanyo_nave:
  vy -= g
  if keypressed(1) == 'Up' and fuel > 0:
    vy += impulso_y
    fuel -= consumo
  elif keypressed(1) == 'Left' and fuel > 0:
    vx -= impulso_x
    fuel -= consumo
  elif keypressed(1) == 'Right' and fuel > 0:
    vx += impulso_x
    fuel -= consumo
  y += vy
  x += vx
  px += vpx
  if px <= 0 or px >= anchura_paisaje - anchura_plataforma:
    vpx = -vpx
  move(nave, vx, vy)
  move(plataforma, vpx, 0)
  viejo_lleno = lleno
  if fuel>250:
    lleno = create_filled_rectangle(1,altura_paisaje, 9, altura_paisaje-fuel/10, 'green')    
  else:      
    lleno = create_filled_rectangle(1,altura_paisaje, 9, altura_paisaje-fuel/10, 'red')
  erase(viejo_lleno)
  vieja_aguja = aguja
  aguja = create_line(anchura_paisaje-50, altura_paisaje-50, \
          anchura_paisaje-50 + 50 * sin(1000*vy*pi/180), \
          altura_paisaje-50 + 50 * cos(1000*vy*pi/180), 'blue')
  erase(vieja_aguja)

msg_x = anchura_paisaje/2
msg_y1 = altura_paisaje/2
msg_y2 = altura_paisaje/3
if y >= altura_paisaje:
  create_text(msg_x, msg_y1, 'Perdiste', 24, 'CENTER')
  create_text(msg_x, msg_y2, ' ?Rumbo a las estrellas?', 12, 'CENTER')
elif y <= 0 and vy < -0.1:
  create_text(msg_x, msg_y1, 'Perdiste', 24, 'CENTER')
  create_text(msg_x, msg_y2, 'Te has estrellado.', 12, 'CENTER')
elif y <= 0 and \
  abs((px+anchura_plataforma/2)-(x+tamanyo_nave/2)) >= anchura_plataforma/2:
  create_text(msg_x, msg_y1, 'Perdiste', 24, 'CENTER')
  create_text(msg_x, msg_y2, ' !Que mala punteria!', 12, 'CENTER')
elif x <= 0 or x >= anchura_paisaje - tamanyo_nave:
  create_text(msg_x, msg_y1, 'Perdiste', 24, 'CENTER')
  create_text(msg_x, msg_y2, 'Chocaste con la pared.', 12, 'CENTER')
else:
  create_text(msg_x, msg_y1, 'Ganaste', 24, 'CENTER')
  create_text(msg_x, msg_y2, ' !Enhorabuena, piloto!', 12, 'CENTER')