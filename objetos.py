from imports import *
from funciones import *

class Enemy(pygame.sprite.Sprite): #Hereda de la clase sprite
    #cargar_fondo('zombie1.png',ancho,alto)
    def __init__(self, img_name, pos, w, h):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.pos = pos
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.jugador = (0,0)
        self.direccion = 0
        self.WIDTH = w
        self.HIGH = h

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

    def moveLeft(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(x - increment_x >= 0):
            self.setPos([x - increment_x,y])
            self.dir = 1

    def moveRight(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(x + increment_x < self.WIDHT - self.rect[2]):
            self.setPos([x + increment_x,y])
            self.dir = 0

    def moveUp(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(y + increment_y >= 10):
            self.setPos([x,y - increment_y])
            self.dir = 2

    def moveDown(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(y + increment_y < self.HIGH - self.rect[3]): # si no se pasa de la pantalla
            self.setPos([x,y + increment_y])
            self.dir = 3

    def getMargen(self):
        return (self.rect[2],self.rect[3])

class Boss(Enemy):
    def __init__(self, img_name,pos,w,h):
        Enemy.__init__(self, img_name,pos,w,h)
        self.life = 1000
        self.speed = 5

    def getLife(self):
    	return self.life

    def setLife(self,life):
    	self.life = life

    def getSpeed(self):
        return self.speed

    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        self.moves = Bresenhamrecta([self.getPos(),pos])#carga los nuevos movimientos
        self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve
        if(self.i < len(self.moves)):
            self.setPos(self.moves[self.i])
            self.i += 1 #para que recorra el siguiente


class Vampire(Enemy):
    def __init__(self, img_name,table,pos,w,h):
        Enemy.__init__(self, img_name,pos,w,h)
        self.table = table
        self.life = 40
        self.speed = 10

    def getLife(self):
    	return self.life

    def setLife(self,life):
    	self.life = life

    def getSpeed(self):
        return self.speed

    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        self.moves = Bresenhamrecta([self.getPos(),pos])#carga los nuevos movimientos
        self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve
        if(self.i < len(self.moves)):
            self.setPos(self.moves[self.i])
            self.i += 1 #para que recorra el siguiente

class Zombie(Enemy):#Hereda de la clase Enemigo
    def __init__(self, img_name, pos, w, h):
        Enemy.__init__(self, img_name, pos, w, h)
        self.moves = [0 for x in range(w*h)] #movimientos que debe realizar
        self.i = 0

    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        self.moves = Bresenhamrecta([self.getPos(),pos])#carga los nuevos movimientos
        self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve
        if(self.i < len(self.moves)):
            self.setPos(self.moves[self.i])
            self.i += 1 #para que recorra el siguiente

class Player(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos,w, h):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
    	self.life = 100
        self.score = 0
        self.dir = 0 #0 derecha , 1 izquierda, 2 arriba, 3 abajo
        #imagenes para movimiento
        self.imaged = [] #derecha
        self.imagei = [] #izquierda
        self.imagenar = [] #arriba
        self.imagena = [] #abajo
        self.enemigos=0
        self.WIDTH = w
        self.HIGH = h
        #speed
        self.increment_x = self.getRect()[2] / 15
        self.increment_y = self.getRect()[3] / 15

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score += score

    def setSpeed(self, speed):
        self.increment_x = speed[0]
        self.increment_y = speed[1]

    def getRect(self):
    	return self.rect

    def getPos(self):
    	return [self.rect.x,self.rect.y]

    def setPos(self,pos):
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]

    def moveLeft(self):
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(x - self.increment_x >= 0):
            self.setPos([x - self.increment_x,y])
            self.dir = 1

    def moveRight(self):
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(x + self.increment_x < self.WIDTH - self.rect[2]):
            self.setPos([x + self.increment_x,y])
            self.dir = 0

    def moveUp(self):
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(y + self.increment_y >= 10):
            self.setPos([x,y - self.increment_y])
            self.dir = 2

    def moveDown(self):
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(y + self.increment_y < self.HIGH - self.rect[3]): # si no se pasa de la pantalla
            self.setPos([x,y + self.increment_y])
            self.dir = 3

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

class CircleBullet(Weapon): #Primero va a la izquierda y despues va todo a la derecha
    def __init__(self, img_name, pos, r,w,h): #img para cargar, y su padre(de donde debe salir la bala)
    	Weapon.__init__(self, img_name, pos)
        self.r = r #radio de la circunferencia
        self.i = 0
        self.moves = [0 for x in range(16)] #movimientos que debe realizar


    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        self.moves = CircunfPtoMedio(self.getPos(),self.r)#carga los nuevos movimientos
        self.order= sorted(self.moves, key=lambda tup: tup[1])
        self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve

        if(self.i < len(self.moves)):
            #print "self.moves_copy[self.i] : " , self.moves[self.i]
            self.setPos(self.moves[self.i])
            self.i += 1 #para que recorra el siguiente
            #print "i : " , self.i
        else :
            self.i = 0


class RectBullet(Weapon):
    def __init__(self, img_name, pos): #img para cargar, y su padre(de donde debe salir la bala)
    	Weapon.__init__(self, img_name, pos)
        self.i = 0
        self.moves = [] #movimientos que debe realizar

    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        self.moves = Bresenhamrecta([self.getPos(),pos])
        self.i = 0 #debe empezar a recorrerla desde cero
    def update(self): #se mueve
        if(self.i < len(self.moves)):
            self.setPos(self.moves[self.i])
            self.i += 1 #para que recorra el siguiente
        else :
            self.i = 0