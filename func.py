import pygame
import random
import time
import sys
import os
import ConfigParser
ANCHO=800
ALTO=600
Config = ConfigParser.ConfigParser()
curdir = os.getcwd()+"/sources"
dirimg = curdir + "/enviroment/levels/images/"
dirsonido = curdir + "/enviroment/levels/sounds/"

keys = {'a' : 97,'b' : 98,'c' : 99,'d' : 100,'e': 101,'f' : 102,'g' : 103,'h' : 104,'i' : 105,'j' : 106,'k' : 107
,'l' : 108,'m' : 109,'n' : 110,'o' : 111,'p' : 112,'q' : 113,'r' : 114,'s' : 115,'t' : 116,'u' : 117,'v' : 118,'w' : 119
,'x' : 120,'y' : 121,'z' : 122,'0' : 48,'1': 49,'2' : 50,'3' : 51,'4' : 52,'5' : 53,'6' : 54,'7' : 55,'8' : 56,'9' : 57
,"'" : 39,',' : 44,'-' : 45,'.' : 46,'/' : 47,':' : 58,'=' : 61,'[' : 91,"\\" : 92,']' : 93,'`' : 96,'ESPACIO' : 32,'ESCAPE' : 27,
'ENTER': 13,'FLECHA IZQ' : 276,'FLECHA DERE' : 275,'FLECHA ARRIB' : 273,'FLECHA ABAJ' : 274}


# Colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
AZUL = (0,0,255)
ROJO = (255,0,0)
VERDE = (0,255,0)
AMARILLO = (255,255,0)

###########################################################################################################################################
#FUNCIONES#################################################################################################################################
#  _________                   .__                    .___         _____                   .__                             ################
# /   _____/ ____   ____  ____ |__| ____   ____     __| _/____   _/ ____\_ __  ____   ____ |__| ____   ____   ____   ______################
# \_____  \_/ __ \_/ ___\/ ___\|  |/  _ \ /    \   / __ |/ __ \  \   __\  |  \/    \_/ ___\|  |/  _ \ /    \_/ __ \ /  ___/################
# /        \  ___/\  \__\  \___|  (  <_> )   |  \ / /_/ \  ___/   |  | |  |  /   |  \  \___|  (  <_> )   |  \  ___/ \___ \ ################
#/_______  /\___  >\___  >___  >__|\____/|___|  / \____ |\___  >  |__| |____/|___|  /\___  >__|\____/|___|  /\___  >____  >################
#        \/     \/     \/    \/               \/       \/    \/                   \/     \/               \/     \/     \/ ################
###########################################################################################################################################
###########################################################################################################################################
def lifebars(player, surface, pos):
    if(player.getLife() > 75):
        color = VERDE
    elif(player.getLife() > 50):
        color = AMARILLO
    else:
        color = ROJO
    pygame.draw.rect(surface, color, (pos[0],pos[1],player.getLife(),10))
    #pygame.display.update()


def checkCollision(sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    if col == True:
        return True
    else:
        return False


#Seccion donde saco el numero o la letra de las letras del teclado
def retornarkeyascii(letra):
    for i in keys:
        if i==letra:
            return keys[i] #retorno el id de la tecla por ejemplo letra=a el valor retornado es 97

def retornarletra(numero):
    for i in keys:
        if keys[i] == numero:
            return i #retorno la letra por ejemplo numero = 97 la letra retornada es a
#fin seccion

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

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

#Funcion para verificar que las imagenes se cargan correctamente
def load_image(nombre_a, dir_img, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_img, nombre_a)
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

#Carga los sonidos verificando la ruta
def load_sound(nombre_s,dir_son):
    ruta = os.path.join(dir_son, nombre_s)
    try:
        sound = pygame.mixer.Sound(ruta)
    except:
        print "Error, no se puede cargar el sonido, verifique el formato: ", ruta
        sys.exit(1)
    return sound

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
####################################################################################
################################# _____.__         #################################
#################################_/ ____\__| ____  #################################
#################################\   __\|  |/    \ #################################
################################# |  |  |  |   |  \#################################
################################# |__|  |__|___|  /#################################
################################FIN             \/ #################################
####################################################################################
