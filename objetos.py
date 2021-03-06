from func import *

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
        self.municion = 40


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
            if(bloque.tipo == ""):
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
            if(bloque.tipo == ""):
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

        if(self.cont<3):
            self.cont+=1
        else:
            self.cont=0
        self.image=self.imaged[self.cont]
        self.vel_x = -self.increment_x

    def ir_der(self):
        """ Usuario pulsa flecha derecha """
        if(self.cont<3):
            self.cont+=1
        else:
            self.cont=0
        self.image=self.imagei[self.cont]
        self.vel_x = self.increment_x

    def no_mover(self):
        """ Usuario no pulsa teclas """
        self.vel_x = 0

    def getLife(self):
    	return self.life

    def setLife(self,life):
        if(life > 100):
            self.life = 100
        else:
    	    self.life = life

    def crash(self):
        for e in self.nivel.enemigos_lista:
            #Quita vida segun el tipo de zombie
            if(e.tipo == 1 or e.tipo == 2):
                self.setLife(self.getLife() - 1) #dano normal
            if(e.tipo == 3 or e.tipo == 5 or e.tipo == 10):
                self.setLife(self.getLife() - 3)#dano muy alto
            if(e.tipo == 4):
                self.setLife(self.getLife() - 0.5)#dano bajo

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

class Weapon(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos): #img para cargar, y su padre(de donde debe salir la bala)
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.pos = pos
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.speed = 5
        self.name = img_name.split(".png")[0]

    def getName(self):
        return self.name

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
        self.tipo = "normal"
        self.tipo2 = ""

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

class RectBullet(Weapon):
    def __init__(self, img_name, pos): #img para cargar, y su padre(de donde debe salir la bala)
    	Weapon.__init__(self, img_name, pos)
        self.i = 0
        self.moves = [] #movimientos que debe realizar
        self.life = 300
        self.tipo = "rect"
        self.tipo2 = ""

    def getLife(self):
        return self.life

    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        self.moves = Bresenhamrecta([self.getPos(),pos])
        self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve
        self.life -= 1
        if(self.i < len(self.moves) - 1):
            self.setPos(self.moves[self.i])
            self.i += 2 #para que recorra el siguiente
        else :
            self.i = 0

class CircleBullet(Weapon): #Primero va a la izquierda y despues va todo a la derecha
    owner = None
    def __init__(self, img_name, pos, r): #img para cargar, y su padre(de donde debe salir la bala)
    	Weapon.__init__(self, img_name, pos)
        self.r = r + 5 #radio de la circunferencia
        self.i = 0
        self.moves = [0 for x in range(16)] #movimientos que debe realizar
        self.life = 100
        self.tipo = "circle"
        self.tipo2 = ""
        self.die = False

    def getLife(self):
        return self.life

    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        self.moves = CircunfPtoMedio(self.owner.getPos(),self.r)#carga los nuevos movimientos
        self.order= sorted(self.moves, key=lambda tup: tup[1])
        self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve
        if(self.i < len(self.moves)):
            self.setPos(self.moves[self.i])
            self.i += 2 #para que recorra el siguiente
        else:
            self.die = True

class RectBulletBoss(Weapon):
    def __init__(self, img_name, pos): #img para cargar, y su padre(de donde debe salir la bala)
    	Weapon.__init__(self, img_name, pos)
        self.i = 0
        self.moves = [] #movimientos que debe realizar
        self.tipo = "rect"
        self.tipo2 = "bulletboss"
        self.playerpos = [0,0]
        self.die = False
        self.life = 100 #no importa, pero hay que tenerla definida

    def getLife(self):
        return self.life

    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        self.moves = Bresenhamrecta([self.getPos(),pos])#self.playerpos
        self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve
        if(self.i < len(self.moves) - 1):
            self.setPos(self.moves[self.i])
            self.i += 2 #para que recorra el siguiente
        else :
            self.die = True

class Enemy(pygame.sprite.Sprite): #Hereda de la clase sprite
    nivel = None
    plat = None

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

    def getLife(self):
        return self.life

    def setLife(self,life):
        self.life = life

    def crash(self):
        self.setLife(self.getLife() - random.randrange(10,20))


class Zombie1(Enemy):
    imaged=[]
    imagei=[]
    def __init__(self, img_name, pos):
        Enemy.__init__(self, img_name, pos)
        matrizimg = cargar_fondo(dirimg+"zombie2.png", 32,32)

    	self.image = matrizimg[0][1]
        self.imaged.append(self.image)
        self.image = matrizimg[1][1]
        self.imaged.append(self.image)
        self.image = matrizimg[2][1]
        self.imaged.append(self.image)

        self.image = matrizimg[0][2]
        self.imagei.append(self.image)
        self.image = matrizimg[1][2]
        self.imagei.append(self.image)
        self.image = matrizimg[2][2]
        self.imagei.append(self.image)


        self.i = 1
        self.cont = 0
        self.speed_aux = 0
        self.reloj = 0
        self.life = 100
        self.speed = 1
        self.tipo = 1
        self.aux = True
        self.cont3 = 0

    def move(self): #se mueve solo
        if(self.speed_aux >= 1):
            self.speed_aux = 0
            self.rect.x += self.speed
            self.cont += 1
            for platx in self.nivel.plataforma_lista:
                if(platx.tipo == "mascota"):
                    if(platx.tipo2 == "escudo"):
                        if(checkCollision(self,platx)):
                            self.rect.x -= self.speed
                            self.cont -= 1
            if(self.cont == 350):
                self.cont = 0
                self.speed *= -1
                self.changeDirection()
        else:
            self.speed_aux += 1

    def update(self):
        if(self.aux):
            self.move()
            if(self.getDir() == 0):
                if self.cont3 <= 2:
                    self.image = self.imagei[self.cont3]
                    self.cont3+=1
                else:
                    self.cont3=0
            elif (self.getDir() == 1):
                if self.cont3 <= 2:
                    self.image = self.imaged[self.cont3]
                    self.cont3+=1
                else:
                    self.cont3=0



    def changeDirection(self):
        if(self.getDir() == 0): #der
            self.setDir(1) #izq
        else: #izq
            self.setDir(0)#der


    def StopMovements(self):
        self.aux = False

    def StartMovements(self):
        self.aux = True

class Zombie2(Enemy):#El que me persigue
    vel_x = 0
    vel_y = 0
    imaged=[]
    imagei=[]
    def __init__(self, img_name, pos,nivel):
        Enemy.__init__(self, img_name, pos)
        matrizimg = cargar_fondo(curdir+"/enviroment/levels/images/zombie.png", 32,32)

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

        self.life = 80
        self.speed = 2
        self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.moves = [0 for x in range(ANCHO)] #movimientos que debe realizar
        self.i = 0
        self.nivel = nivel
        self.tipo = 2
        self.dir = 0
        self.cont=0
        self.turn = 0
        self.aux = True
        self.cont = 0

    def setDir(self,dir):
        self.dir = dir

    def getDir(self):
        return self.dir

    def StopMovements(self):
        print "stop moving 2"
        self.aux = False

    def StartMovements(self):
        self.aux = True

    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        if(self.aux):
            self.moves = Bresenhamrecta([self.getPos(),pos])#carga los nuevos movimientos
            last_x = self.moves[-1][0]
            aux =  self.getMargen()[0]
            if(self.getDir() == 0):
                aux *= -1
            self.moves[-1] = [last_x + aux, self.moves[-1][1]]
            self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve
        if(self.aux):
            if self.turn == 0:
                if self.rect.x > 120:
                    if self.cont <= 2:
                        self.image = self.imaged[self.cont]
                        self.cont+=1
                    else:
                        self.cont=0
                    self.setPos([self.rect.x-5,self.rect.y])
                    for platx in self.nivel.plataforma_lista:
                        if(platx.tipo == "mascota"):
                            if(platx.tipo2 == "escudo"):
                                if(checkCollision(self,platx)):
                                    self.setPos([self.rect.x+5,self.rect.y])
                else:
                    self.turn = 1
            if self.turn == 1:
                bloque_col_list = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
                if self.cont <= 2:
                    self.image = self.imagei[self.cont]
                    self.cont+=1
                else:
                    self.cont=0
                if(len(bloque_col_list) == 0):
                    self.setPos([self.rect.x+5,self.rect.y])
                else:
                    self.turn = 0

class Zombie3(Enemy):#El que me dispara y esta en la plataforma de arriba
    imaged=[]
    imagei=[]
    def __init__(self, img_name, pos):
        Enemy.__init__(self, img_name, pos)

        matrizimg = cargar_fondo(curdir+"/enviroment/levels/images/zombie.png", 32,32)

    	self.image = matrizimg[6][1]
        self.imaged.append(self.image)
        self.image = matrizimg[7][1]
        self.imaged.append(self.image)
        self.image = matrizimg[8][1]
        self.imaged.append(self.image)

        self.image = matrizimg[6][2]
        self.imagei.append(self.image)
        self.image = matrizimg[7][2]
        self.imagei.append(self.image)
        self.image = matrizimg[8][2]
        self.imagei.append(self.image)

    	self.rect = self.image.get_rect()

        self.life = 150
        self.speed = 1
        self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.cont = 0
        self.tipo = 3
        self.dir = 0 #derecha
        self.speed_aux = 0
        self.aux = True
        self.cont = 0
        self.cont3 = 0

    def setDir(self,dir):
        self.dir = dir

    def getDir(self):
        return self.dir

    def StopMovements(self):
        self.aux = False

    def StartMovements(self):
        self.aux = True

    def move(self): #se mueve solo
        if(self.speed_aux >= 1):
            self.speed_aux = 0
            self.rect.x += self.speed
            self.cont += 1
            for platx in self.nivel.plataforma_lista:
                if(platx.tipo == "mascota"):
                    if(platx.tipo2 == "escudo"):
                        if(checkCollision(self,platx)):
                            self.rect.x -= self.speed
                            self.cont -= 1
            if(self.cont == 400):
                self.cont = 0
                self.speed *= -1
                self.changeDirection()
        else:
            self.speed_aux += 1

    def update(self):
        if(self.aux):
            self.move()
            if(self.getDir() == 0):
                if self.cont3 <= 2:
                    self.image = self.imagei[self.cont3]
                    self.cont3+=1
                else:
                    self.cont3=0
            elif (self.getDir() == 1):
                if self.cont3 <= 2:
                    self.image = self.imaged[self.cont3]
                    self.cont3+=1
                else:
                    self.cont3=0



    def changeDirection(self):
        if(self.getDir() == 0): #der
            self.setDir(1) #izq
        else: #izq
            self.setDir(0)#der

class Zombie4(Enemy):#El que no se mueve, solo lanza ratas
    def __init__(self, img_name, pos):
        Enemy.__init__(self, img_name, pos)
        self.life = 100
        self.speed = 1
        self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.tipo = 4

class Rata(Enemy):#Hereda de la clase Enemigo
    def __init__(self, img_name, pos,nivel):
        Enemy.__init__(self, img_name, pos)
        self.life = 500
        self.speed = 1
        self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.moves = [0 for x in range(ANCHO)] #movimientos que debe realizar
        self.i = 0
        self.nivel = nivel
        self.dir = 0
        self.name = img_name.split(".png")[0]
        self.tipo = "rata"
        self.tipo2 = ""

    def getName(self):
        return self.name

    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        self.moves = Bresenhamrecta([self.getPos(),pos])#carga los nuevos movimientos
        self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve
        self.life -= 1 #para que se muera
        #print "rata life: ", self.life
        bloques = self.nivel.plataforma_lista

        if(self.i < len(self.moves)):
            pos = self.moves[self.i]
            if(pos == 0):
                self.setPos([self.rect.x,self.rect.y])
            else:
                for e in bloques:
                    if(checkCollision(self,e) == False): # si no se choca con los objetos del nivel
                        self.setPos(pos)

            self.i += 1 #para que recorra el siguiente

class Zombie5(Enemy):#El que salta y dispara
    vel_x = 0
    vel_y = 0
    def __init__(self, img_name, pos):
        Enemy.__init__(self, img_name, pos)
        self.i = 1
        self.cont = 0
        self.reloj = 0
        self.life = 200
        self.speed = 1
        self.tipo = 5
        self.increment_y = 0
        self.jumping = False
        self.aux = True

    def StopMovements(self):
        self.aux = False

    def StartMovements(self):
        self.aux = True

    def calc_grav(self):
        """ Calculamos efecto de la gravedad. """

        if self.increment_y < 0: #esta saltando
            self.jumping = True
            self.increment_y += 1#1.5
            #self.setPos([self.getPos()[0],ALTO + self.increment_y - self.getMargen()[1]])
            self.setPos([self.getPos()[0],self.increment_y +self.pos[1]])

        if self.increment_y >= 0: #ya no salta mas
            self.jumping = False
            #self.setPos([self.getPos()[0],(ALTO - self.getMargen()[1])])
            self.setPos([self.getPos()[0],self.pos[1]])

    def salto(self):
        if(self.jumping == False): #Si ya no esta saltando, puede vovler a saltar
            self.increment_y -= 10

    def update(self):
        if(self.aux):
            self.calc_grav()

class Zombie6(Enemy):#Hereda de la clase Enemigo
    def __init__(self, img_name, pos):
        Enemy.__init__(self, img_name, pos)
        self.i = 1
        self.cont = 0
        self.reloj = 0
        self.life = 100
        self.speed = 1
        self.tipo = 6
        self.r = 10
        self.moves = [0 for x in range(ANCHO)] #movimientos que debe realizar

    def StartMovements(self):#se mueve sobre si mismo
        self.moves = CircunfPtoMedio([random.randrange(30,ANCHO - 30),random.randrange(30,ALTO/2 - 30)],self.r)#carga los nuevos movimientos
        self.order= sorted(self.moves, key=lambda tup: tup[1])
        self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve
        if(self.moves[self.i] != 0):
            if(self.i < len(self.moves) - 1):
                self.setPos(self.moves[self.i])
                self.i += 1 #para que recorra el siguiente
            else :
                self.i = 0


class Boss(Enemy):#Hereda de la clase Enemigo
    def __init__(self, img_name, pos):
        Enemy.__init__(self, img_name, pos)
        self.life = 200
        self.speed = 1
        self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.cont = 0
        self.tipo = 10
        self.dir = 0 #derecha
        self.speed_aux = 0
        self.aux = True
        self.des = 0
        self.playerpos=[0,0]
        self.cont3 = 0
        self.i = 1
        self.speed = 3

    def changeDirection(self):
        if(self.getDir() == 0): #der
            self.setDir(1) #izq
        else: #izq
            self.setDir(0)#der

    def StopMovements(self):
        self.aux = False

    def StartMovements(self):
        self.aux = True

    def move(self): #se mueve solo
        if(self.speed_aux >= 1):
            self.speed_aux = 0
            self.rect.x += self.speed
            self.cont += 1

            if(self.cont == 290/3):
                self.cont = 0
                self.speed *= -1
                self.changeDirection()
        else:
            self.speed_aux += 1

    def update(self):
        if(self.aux):
            self.move()
            if(self.getDir() == 0):
                if self.cont3 <= 2:
                    #self.image = self.imagei[self.cont3]
                    self.cont3 += 1
                else:
                    self.cont3 = 0
            elif (self.getDir() == 1):
                if self.cont3 <= 2:
                    #self.image = self.imaged[self.cont3]
                    self.cont3 += 1
                else:
                    self.cont3 = 0

class Mascota(Enemy):#Hereda de la clase Enemigo

    def __init__(self, img_name, pos):
        Enemy.__init__(self, img_name, pos)
        self.i = 0
        self.cont = 0
        self.reloj = 0
        self.life = 100
        self.speed = 1
        self.tipo = "mascota"
        self.tipo2 = ""
        self.r = 45
        self.moves = [0 for x in range(ANCHO)] #movimientos que debe realizar
        self.aux = False
        self.jugador = None

    def StartMovements(self):#se mueve sobre si mismo
        self.aux = True

    def update(self): #se mueve
        if(self.aux):
            pos = self.jugador.getPos()
            self.setPos([pos[0] - self.jugador.getMargen()[0],pos[1] - self.jugador.getMargen()[1]/2])

class Plataforma(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.pos = pos
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.tipo = ""
        self.tipo2 = ""
