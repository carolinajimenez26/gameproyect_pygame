from imports import *

def checkCollision(sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    if col == True:
        return True
    else:
        return False

def cargar_fondo(archivo, ancho, alto):
    imagen = pygame.image.load(archivo).convert_alpha()
    imagen_ancho, imagen_alto = imagen.get_size()
    #print 'ancho: ', imagen_ancho, ' xmax: ', imagen_ancho/ancho
    #print 'alto: ',imagen_alto, ' ymax: ', imagen_alto/alto
    tabla_fondos = []

    for fondo_x in range(0, imagen_ancho/ancho):
       linea = []
       tabla_fondos.append(linea)
       for fondo_y in range(0, imagen_alto/alto):
            cuadro = (fondo_x * ancho, fondo_y * alto, ancho, alto)
            linea.append(imagen.subsurface(cuadro))
    return tabla_fondos


def Bresenhamrecta(p): #algoritmo para dibujar rectas

    x0 = p[0][0]
    y0 = p[0][1]
    x1 = p[1][0]
    y1 = p[1][1]
    res = []
    dx = (x1 - x0)
    dy = (y1 - y0)
    #determinar que punto usar para empezar, cual para terminar
    if (dy < 0) :
        dy = -1*dy
        stepy = -1
    else :
        stepy = 1
    if (dx < 0) :
        dx = -1*dx
        stepx = -1
    else :
        stepx = 1
    x = x0
    y = y0
    #se cicla hasta llegar al extremo de la linea
    if(dx>dy) :
        p = 2*dy - dx
        incE = 2*dy
        incNE = 2*(dy-dx)
        while (x != x1) :
            x = x + stepx
            if (p < 0) :
                p = p + incE
            else :
                y = y + stepy
                p = p + incNE
            p_new = [x, y]
            res.append(p_new)

    else :
        p = 2*dx - dy
        incE = 2*dx
        incNE = 2*(dx-dy)
        while (y != y1) :
            y = y + stepy
            if (p < 0) :
                p = p + incE
            else :
                x = x + stepx
                p = p + incNE

            p_new = [x, y]
            res.append(p_new)
    return res

def tras((x0,y0),(x,y)):
    x=x0+x
    y=y0-y
    return (x,y)

def CircunfPtoMedio((x0,y0),r):
	l=[]
	l2=[]
	l3=[]
	l4=[]
	l5=[]
	l6=[]
	l7=[]
	l8=[]
	x=0
	y=r
	d=5/4-r
	punto=tras((x0,y0),(x,y)) #X0+X Y0-Y
	l.append(punto)
	punto=tras((x0,y0),(x,-y))#X0+X Y0+Y
	l2.append(punto)
	punto=tras((x0,y0),(-x,y))#X0-X Y0-Y
	l3.append(punto)
	punto=tras((x0,y0),(-x,-y))#X0-X Y0+Y
	l4.append(punto)
	punto=tras((x0,y0),(y,x)) #X0+Y Y0-X
	l5.append(punto)
	punto=tras((x0,y0),(y,-x))#X0+Y Y0+X
	l6.append(punto)
	punto=tras((x0,y0),(-y,x))#X0-Y Y0-X
	l7.append(punto)
	punto=tras((x0,y0),(-y,-x))#X0-Y Y0+X
	l8.append(punto)
	#simetria(pantalla,(x0,y0),(x,y))

	while y>x:
		if d<0:
			d=d+x*2+3
			x=x+1
		else:
			d=d+2*(x-y)+5
			x=x+1
			y=y-1
		#simetria(pantalla,(x0,y0),(x,y))
		punto=tras((x0,y0),(x,y))
		l.append(punto)
		punto=tras((x0,y0),(x,-y))
		l2.append(punto)
		punto=tras((x0,y0),(-x,y))
		l3.append(punto)
		punto=tras((x0,y0),(-x,-y))
		l4.append(punto)
		punto=tras((x0,y0),(y,x))
		l5.append(punto)
		punto=tras((x0,y0),(y,-x))
		l6.append(punto)
		punto=tras((x0,y0),(-y,x))
		l7.append(punto)
		punto=tras((x0,y0),(-y,-x))
		l8.append(punto)
	l5.reverse()
	l2.reverse()
	l8.reverse()
	l3.reverse()
	res = l+l5+l6+l2+l4+l8+l7+l3
	return res

#Carga los sonidos verificando la ruta
def load_sound(nombre_s,dir_son):
    ruta = os.path.join(dir_son+"/sounds", nombre_s)
    try:
        sound = pygame.mixer.Sound(ruta)
    except:
        print "Error, no se puede cargar el sonido, verifique el formato: ", ruta
        sys.exit(1)
    return sound

#Funcion para verificar que las imagenes se cargan correctamente
def load_image(nombre_a, dir_img, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_img+"/images", nombre_a)
    try:
        image = pygame.image.load(ruta)
    except:
        print "Error, no se puede cargar la imagen: ", ruta
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha == True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

#Funcion para determianr si el usuario tiene el mouse encima de lso botones
def pres_boton(button_x,button_y,sprite):
    x_len = sprite.get_width()
    y_len = sprite.get_height()
    mos_x, mos_y = pygame.mouse.get_pos()
    if mos_x>button_x and (mos_x<button_x+x_len):
        x_inside = True
    else:
        x_inside = False
    if mos_y>button_y and (mos_y<button_y+y_len):
        y_inside = True
    else:
        y_inside = False
    if x_inside and y_inside:
        return True
    else:
        return False

#FIn funcion para determianr si el usuario tiene el mouse encima de lso botones

def lifebars(player, surface, pos):
    if(player.getLife() > 75):
        color = VERDE
    elif(player.getLife() > 50):
        color = AMARILLO
    else:
        color = ROJO
    pygame.draw.rect(surface, color, (pos[0],pos[1],player.getLife(),10))
    #pygame.display.update()
