from objetos import *
from niveles import *
import inputbox
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
