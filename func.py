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

####################################################################################
################################# _____.__         #################################
#################################_/ ____\__| ____  #################################
#################################\   __\|  |/    \ #################################
################################# |  |  |  |   |  \#################################
################################# |__|  |__|___|  /#################################
################################FIN             \/ #################################
####################################################################################
