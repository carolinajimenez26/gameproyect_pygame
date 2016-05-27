import pygame
import random
import time
import sys
import os

curdir = os.getcwd()+"/sources"

#Colores RGB#
rojo=(255,0,0)
azul=(0,0,255)
blanco=(255,255,255)
verde=(0,255,0)
verdefosforecente=(4,255,13)
naranja=(252,178,81)
negro=(0,0,0)
cyan=(0,255,255)
amarillo = (255,255,0)
#Fin definicion de colores

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

class mainsplash(pygame.sprite.Sprite): #Hereda de la clase sprite
    #cargar_fondo('zombie1.png',ancho,alto)
    def __init__(self):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image("o_7ecb0b0ccb0a3aa5-0.jpg", curdir+"/enviroment/main", alpha=False)
        self.carrusel=[]
        self.index=0
    	self.rect = self.image.get_rect()

    def setindex(self,value):
        self.index=value
    def getindex(self):
        return self.index
    def load(self):
        for i in range(0,729):
            self.carrusel.append(load_image(("o_7ecb0b0ccb0a3aa5-"+str(i)+".jpg"),curdir+"/enviroment/main", alpha=False))
        self.setindex(len(self.carrusel)-1)

    def update(self):
        if(self.getindex()<=(len(self.carrusel)-1)):
            self.image=self.carrusel[self.index]
            self.index=self.index+1
        else:
            self.index=0
