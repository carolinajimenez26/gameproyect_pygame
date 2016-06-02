import pygame
import random
import time
import sys
import os
import ConfigParser
import inputbox
from niveles import *
# Dimensiones pantalla
ANCHO  = 800
ALTO = 600
#Imports del tkinter
from Tkinter import *
import tkMessageBox
from ttk import Frame, Button, Style
from PIL import Image, ImageTk
#Fin

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

Config = ConfigParser.ConfigParser()
curdir = os.getcwd()+"/sources"

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


#################################################################################################
# _________                   .__                       .__                                ######
# /   _____/ ____   ____  ____ |__| ____   ____     ____ |  | _____    ______ ____   ______######
# \_____  \_/ __ \_/ ___\/ ___\|  |/  _ \ /    \  _/ ___\|  | \__  \  /  ___// __ \ /  ___/######
# /        \  ___/\  \__\  \___|  (  <_> )   |  \ \  \___|  |__/ __ \_\___ \\  ___/ \___ \ ######
#/_______  /\___  >\___  >___  >__|\____/|___|  /  \___  >____(____  /____  >\___  >____  >######
#        \/     \/     \/    \/               \/       \/          \/     \/     \/     \/ ######
#################################################################################################
class window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent



class splashload():
    def __init__(self):
        self.correr=True
        if(self.correr):
            menu_e = pygame.display.set_mode((700, 700))
            pygame.display.set_caption("Loading files ", 'Spine Runtime')
            image = load_image("loading.jpg", curdir+"/enviroment/main", alpha=False)
            image = pygame.transform.scale(image,(700,700))
            menu_e.blit(image,(0,0))
            pygame.display.flip()
        else:
            print "Cerrado como tu gfa :v"
    def setcorrer(self):
        self.correr=False

class buttonz(pygame.sprite.Sprite):
    def __init__(self,img,img2):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img, curdir+"/enviroment/main", alpha=True)
        self.images = [load_image(img, curdir+"/enviroment/main", alpha=True),load_image(img2, curdir+"/enviroment/main", alpha=True)]
        self.index=0
        self.clicked=False
        self.mousepos=[]
    	self.rect = self.image.get_rect()

    def setclicked(self):
        self.clicked=True
    def getrect(self):
        print self.rect

    def setpos(self,pos):
        self.rect.x=pos[0]
        self.rect.y=pos[1]

    def getrect(self):
        return self.rect[2],self.rect[3]

    def getrectpos(self):
        return self.rect.x,self.rect.y

    def action(self):
        print "Empy button - Report bug"

    def update(self):
        x_len,y_len = self.getrect()
        button_x,button_y = self.getrectpos()
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
            if self.clicked:
                self.image=self.images[1]
                self.clicked=False
                self.action()
            else:
                self.image=self.images[1]
        else:
            self.clicked=False
            self.image=self.images[0]

class boton_inicio(buttonz):
    def __init__(self,img,img2):
        buttonz.__init__(self,img,img2)
    def action(self):
        print "boton"

class boton_tutorial(buttonz):
    def __init__(self,img,img2):
        buttonz.__init__(self,img,img2)
    def action(self):
        print "boton de tutorial"

class menu(window):
    def __init__(self, parent):
        window.__init__(self,parent)
        self.initUI()
    def save(self,derechas,izquierdas,saltos,disparos):
        derechas = retornarkeyascii(derechas)
        izquierdas = retornarkeyascii(izquierdas)
        saltos = retornarkeyascii(saltos)
        disparos = retornarkeyascii(disparos)
        if(not(derechas == None or izquierdas==None or saltos == None or disparos==None)):
            try:
                Config.set('Movimientos', 'derecha', derechas)
                Config.set('Movimientos', 'izquierda', izquierdas)
                Config.set('Movimientos', 'salto', saltos)
                Config.set('Movimientos', 'disparo', disparos)
                with open('config.ini', 'w') as configfile:
                    Config.write(configfile)
            except:
                print "Error en la escritura"
        else:
            print "error"
    def initUI(self):

        Config.read("config.ini")
        Config.sections()
        derecha = ConfigSectionMap("Movimientos")['derecha']
        izquierda = ConfigSectionMap("Movimientos")['izquierda']
        disparo = ConfigSectionMap("Movimientos")['disparo']
        salto = ConfigSectionMap("Movimientos")['salto']

        derecha=int(derecha)
        izquierda=int(izquierda)
        disparo=int(disparo)
        salto=int(salto)

        self.parent.title("Place of dead - [Configuration]")
        self.style = Style()
        #self.style.theme_use("default")
        self.style.configure('My.TFrame', background='gray')
        #Layouts
        frame1 = Frame(self)
        frame1.pack(fill=Y)
        frame2 = Frame(self)
        frame2.pack(fill=Y)
        frame3 = Frame(self)
        frame3.pack(fill=Y)
        frame4 = Frame(self)
        frame4.pack(fill=Y)
        frame5 = Frame(self)
        frame5.pack(fill=Y)
        frame6 = Frame(self)
        frame6.pack(fill=Y)

        self.pack(fill=BOTH, expand=1)
        self.labela = Label(frame2, text="Movimiento a la derecha: ")#, textvariable=self.var)
        self.labela.pack(side=LEFT)
        derechae = Entry(frame2,width=9)
        derechae.insert(END, str(retornarletra(derecha)))
        derechae.pack(side=LEFT,padx=1, pady=1, expand=True)

        self.labelb = Label(frame3, text="Movimiento a la derecha: ")#, textvariable=self.var)
        self.labelb.pack(side=LEFT)
        izquierdae = Entry(frame3,width=9)
        izquierdae.insert(END, str(retornarletra(izquierda)))
        izquierdae.pack(side=LEFT,padx=1, pady=1, expand=True)

        self.labelc = Label(frame4, text="Salto: ")#, textvariable=self.var)
        self.labelc.pack(side=LEFT)
        saltoe = Entry(frame4,width=9)
        saltoe.insert(END, str(retornarletra(salto)))
        saltoe.pack(side=LEFT,padx=1, pady=1, expand=True)

        self.labeld = Label(frame5, text="Ataque: ")#, textvariable=self.var)
        self.labeld.pack(side=LEFT)
        disparoe = Entry(frame5,width=9)
        disparoe.insert(END, str(retornarletra(disparo)))
        disparoe.pack(side=LEFT,padx=1, pady=1, expand=True)

        okButton = Button(frame6, text="Save", command=lambda: self.save(derechae.get(),izquierdae.get(),saltoe.get(),disparoe.get()))
        okButton.pack(side=RIGHT)

class boton_ajustes(buttonz):
    def __init__(self,img,img2,ventana,backgrounl,DIM):
        buttonz.__init__(self,img,img2)
        self.ventana=ventana
        self.backgrounl=backgrounl
        self.ANCHO = DIM[0]
        self.ALTO = DIM [1]
    def action(self):
        self.backgrounl.draw(self.ventana)
        self.ventana = pygame.display.set_mode((2, 2))
        #pr = self.ventana.subsurface([0,0,100,100]) #Dibuja una surface sobre la pantalla
        #pr.fill((255,255,255))
        pygame.display.flip()
        #inp = str(inputbox.ask(self.ventana, 'Movimiento a la derecha:'))
        #inp = str(inputbox.ask(self.ventana, 'Movimiento a la izquierda:'))
        #print inp
        root = Tk()
        root.geometry("480x350+300+300")
        app = menu(root)
        def on_closing():
            if tkMessageBox.askokcancel("Quit", "Guardaste los cambios antes de salir?"):
                root.destroy()
                self.ventana = pygame.display.set_mode((self.ANCHO, self.ALTO))
                pygame.display.flip()
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()

class boton_acercade(buttonz):
    def __init__(self,img,img2):
        buttonz.__init__(self,img,img2)
    def action(self):
        print "boton de creditos y mas"

class mainsplash(pygame.sprite.Sprite): #Hereda de la clase sprite
    #cargar_fondo('zombie1.png',ancho,alto)
    def __init__(self):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image("o_7ecb0b0ccb0a3aa5-0.jpg", curdir+"/enviroment/main", alpha=False)
        self.carrusel=[]
        self.index=0
    	self.rect = self.image.get_rect()

    def setpos(self):
        self.rect.x=0
        self.rect.y=0

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

####################################################################################
################################# _____.__         #################################
#################################_/ ____\__| ____  #################################
#################################\   __\|  |/    \ #################################
################################# |  |  |  |   |  \#################################
################################# |__|  |__|___|  /#################################
################################FIN             \/ #################################
####################################################################################


class Jugador(pygame.sprite.Sprite):

    # Atributos
    # velocidad del jugador
    vel_x = 0
    vel_y = 0
    imaged=[]
    imagei=[]
    # Lista de elementos con los cuales chocar
    nivel = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # creamos el bloque
        ancho = 40
        alto = 60
        matrizimg = cargar_fondo(curdir+"/enviroment/levels/images/maximus.png", 32,48)
    	self.image = matrizimg[0][1]
        self.imaged.append(self.image)
        self.image = matrizimg[1][1]
        self.imaged.append(self.image)
        self.image = matrizimg[2][1]
        self.imaged.append(self.image)
        self.image = matrizimg[3][1]
        self.imaged.append(self.image)
        self.image = matrizimg[0][2]
        self.imagei.append(self.image)
        self.image = matrizimg[1][2]
        self.imagei.append(self.image)
        self.image = matrizimg[2][2]
        self.imagei.append(self.image)
        self.image = matrizimg[3][2]
        self.imagei.append(self.image)
    	self.rect = self.image.get_rect()

        self.life = 100
        self.score = 0
        self.dir = 0 #0 derecha , 1 izquierda, 2 arriba, 3 abajo
        #imagenes para movimiento
        self.imagenar = [] #arriba
        self.imagena = [] #abajo
        self.enemigos = 0
        #speed
        self.increment_x = 6
        self.increment_y = 0
        self.cont=0


    def update(self):
        """ Mueve el jugador. """
        # Gravedad
        self.calc_grav()

        # Mover izq/der
        self.rect.x += self.vel_x

        # Revisar si golpeamos con algo (bloques con colision)
        bloque_col_list = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
        for bloque in bloque_col_list:
            # Si nos movemos a la derecha,
            # ubicar jugador a la izquierda del objeto golpeado
            if self.vel_x > 0:
                self.rect.right = bloque.rect.left
            elif self.vel_x < 0:
                # De otra forma nos movemos a la izquierda
                self.rect.left = bloque.rect.right

        # Mover arriba/abajo
        self.rect.y += self.vel_y

        # Revisamos si chocamos
        bloque_col_list = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
        for bloque in bloque_col_list:

            # Reiniciamos posicion basado en el arriba/bajo del objeto
            if self.vel_y > 0:
                self.rect.bottom = bloque.rect.top
            elif self.vel_y < 0:
                self.rect.top = bloque.rect.bottom

            # Detener movimiento vertical
            self.vel_y = 0

    def calc_grav(self):
        """ Calculamos efecto de la gravedad. """
        if self.vel_y == 0:
            self.vel_y = 1
        else:
            self.vel_y += .35

        # Revisamos si estamos en el suelo
        if self.rect.y >= ALTO - self.rect.height and self.vel_y >= 0:
            self.vel_y = 0
            self.rect.y = ALTO - self.rect.height

    def salto(self):
        """ saltamos al pulsar boton de salto """
        print "en salto"
        # Nos movemos abajo un poco y revisamos si hay una plataforma bajo el jugador
        self.rect.y += 2
        plataforma_col_lista = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
        self.rect.y -= 2

        # Si es posible saltar, aumentamos velocidad hacia arriba
        if len(plataforma_col_lista) > 0 or self.rect.bottom >= ALTO:
            self.vel_y = -10

    # Control del movimiento
    def ir_izq(self):
        """ Usuario pulsa flecha izquierda """
        if(self.cont<=3):
            self.cont+=1
        else:
            self.cont=0
        self.image=self.imagei[self.cont]
        self.vel_x = -self.increment_x

    def ir_der(self):
        """ Usuario pulsa flecha derecha """
        if(self.cont<=3):
            self.cont+=1
        else:
            self.cont=0
        self.image=self.imaged[self.cont]
        self.vel_x = self.increment_x

    def no_mover(self):
        """ Usuario no pulsa teclas """
        self.vel_x = 0

    def getLife(self):
    	return self.life

    def setLife(self,life):
    	self.life = life

    def crash(self):
        self.setLife(self.getLife() - 1) #quita una vida

    def getDir(self):
        return self.dir

    def setDir(self,dir):
        self.dir = dir

    def getMargen(self):
        return (self.rect[2],self.rect[3])#x,y

    def getPos(self):
    	return [self.rect.x,self.rect.y]

    def setPos(self,pos):
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]

    def setSpeed(self,speed):
        self.increment_x = speed

    def getScore(self):
        return self.score

    def crash(self):
        self.setLife(self.getLife() - 1) #quita una vida


class Weapon(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos): #img para cargar, y su padre(de donde debe salir la bala)
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.pos = pos
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.speed = 5

    def getRect(self):
    	return self.rect

    def getPos(self):
    	return [self.rect.x,self.rect.y]

    def setPos(self,pos):
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]

class Bullet(Weapon): #Hereda de la clase sprite
    def __init__(self, img_name, pos): #img para cargar, y su padre(de donde debe salir la bala)
    	Weapon.__init__(self, img_name, pos)
        self.magiciandir = 0 #dispara dependiendo de la posicion del magician

    def setDir(self,dir):
        self.magiciandir = dir

    def getDir(self):
        return self.magiciandir

    def update(self):
        if(self.magiciandir == 0): #derecha
            self.rect.x += self.speed
        if(self.magiciandir == 1):#izquierda
            self.rect.x -= self.speed
        if(self.magiciandir == 2):#arriba
            self.rect.y -= self.speed
        if(self.magiciandir == 3):#abajo
            self.rect.y += self.speed

class Enemy(pygame.sprite.Sprite): #Hereda de la clase sprite
    #cargar_fondo('zombie1.png',ancho,alto)
    def __init__(self, img_name, pos):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.pos = pos
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.jugador = (0,0)
        self.direccion = 0

    def getDir(self):
        return self.direccion

    def setDir(self, dir):
        self.direccion = dir

    def getRect(self):
    	return self.rect

    def getPos(self):
    	return [self.rect.x,self.rect.y]

    def setPos(self,pos):
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]

    def getMargen(self):
        return (self.rect[2],self.rect[3])

class Zombie1(Enemy):#Hereda de la clase Enemigo
    def __init__(self, img_name, pos):
        Enemy.__init__(self, img_name, pos)
        self.i = 1
        self.cont = 0
        self.reloj = 0
        self.life = 100
        self.speed = self.rect.x

    def move(self): #se mueve solo
        self.rect.x += self.i
        self.cont += 1
        if(self.cont == 380):
            self.cont = 0
            self.i *= -1

    def update(self):
        self.move()

    def getLife(self):
        return self.life

    def setLife(self,life):
        self.life = life

    def crash(self):
        self.setLife(self.getLife() - 1)

class Plataforma(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.pos = pos
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.name = img_name.split(".png")[0]

    def getName(self):
        return self.name
