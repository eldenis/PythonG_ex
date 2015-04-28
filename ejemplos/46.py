#create_line(x1,y1,x2,y2)
L1=100
L2=900

create_line(L1,L2,L2,L2)#Horizontal superior
create_line(L2,L1,L1,L1)#Horizontal inferior
create_line(L1,L2,L1,L1)#vertical  Izquierda
create_line(L2,L2,L2,L1)#vertical    derecha

create_line(L2,L1,L1,L2)#Diagonal  principal
create_line(L1,L1,L2,L2)#diagonal secundaria
