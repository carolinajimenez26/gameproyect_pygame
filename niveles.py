import pygame
from objetos import *


class Nivel(object):
    """ Esta es una superclase usada para definir un nivel
        Se crean clases hijas por cada nivel que desee emplearse """

    plataforma_lista = None
    enemigos_lista = None

    mov_fondo = 0

    def __init__(self, jugador,imagen,sonido):
        self.plataforma_lista = pygame.sprite.Group()
        self.enemigos_lista = pygame.sprite.Group()
        self.jugador = jugador
        self.fondo = pygame.image.load(imagen)
        self.sonido = load_sound(sonido,curdir)

    # Actualizamos elementos en el nivel
    def update(self):
        """ Actualiza todo lo que este en este nivel."""
        self.plataforma_lista.update()
        self.enemigos_lista.update()

    def draw(self, pantalla):
        """ Dibuja lo que se encuentre en el nivel. """

        # Dibujamos fondo
        pantalla.fill(AZUL)

        pantalla.blit(self.fondo, (0,0))

        # Dibujamos todos los sprites en las listas
        self.plataforma_lista.draw(pantalla)
        self.enemigos_lista.draw(pantalla)

    def Mover_fondo(self, mov_x):
        self.mov_fondo += mov_x
        for plataforma in self.plataforma_lista:
            plataforma.rect.x += mov_x
        for enemigo in self.enemigos_lista:
            enemigo.rect.x += mov_x

    def StopSound(self):
        self.sonido.stop()

    def StartSound(self):
        self.sonido.play()

    def getEnemies(self):
        return self.enemigos_lista

    def getElements(self):
        return self.plataforma_lista

    def removeElement(self,e):
        self.plataforma_lista.remove(e)

class Nivel_01(Nivel):
    """ Definition for level 1. """

    ls_vida = None

    def __init__(self, jugador,imagen,sonido):
        """ Creamos nivel 1. """

        # Llamamos al padre
        Nivel.__init__(self, jugador,imagen,sonido)
        self.limite = -3000
        self.jugador = jugador
        self.ls_vida = pygame.sprite.Group()

        #---------------Plataformas-----------------------
        plataforma_tipo1 = [
                             [500, ALTO - ALTO/5],
                             [990, ALTO/10]
                           ]
        plataforma_tipo2 = [
                             [1100, ALTO - ALTO/2 + 30],
                             [1500, ALTO/3 + 30],
                             [3000 - 400, ALTO/3 - 25]
                            ]

        plataforma_tipo3 = [
                             [1900, ALTO/3 - 25],
                             [3000 - 30, ALTO/3 - 25]
                            ]

        for plataforma in plataforma_tipo1:
            bloque = Plataforma("plataforma1.png",[plataforma[0],plataforma[1]])
            self.plataforma_lista.add(bloque)

        for plataforma in plataforma_tipo2:
            bloque = Plataforma("plataforma2.png",[plataforma[0],plataforma[1]])
            self.plataforma_lista.add(bloque)

        for plataforma in plataforma_tipo3:
            bloque = Plataforma("plataforma3.png",[plataforma[0],plataforma[1]])
            self.plataforma_lista.add(bloque)

        caja_tipo1 = [
                        [650,ALTO - ALTO/2 ],
                        [650 + 80,(ALTO - ALTO/2) - 80],
                        [650 + 2*80,(ALTO - ALTO/2) - 2*80],
                        [3000,ALTO - ALTO/7.5],
                        [3200,ALTO - ALTO/7.5],
                        [3200,ALTO - 2*(ALTO/7.5)],
                     ]

        caja_tipo2 = [
                        [-80,(ALTO - ALTO/3) + 80 ],
                        [0,(ALTO - ALTO/3) ],
                        [0 + 80,(ALTO - ALTO/3) - 80],
                        [0 + 2*80,(ALTO - ALTO/3) - 2*80],
                        [1750,ALTO - ALTO/3],
                        [2500,ALTO - ALTO/3],
                        [2600,ALTO - ALTO/3],
                        [2700,ALTO - ALTO/3],
                     ]

        for caja in caja_tipo1:
            bloque = Plataforma("caja.png",[caja[0],caja[1]])
            self.plataforma_lista.add(bloque)

        for caja in caja_tipo2:
            bloque = Plataforma("caja2.png",[caja[0],caja[1]])
            self.plataforma_lista.add(bloque)

        rocas_tipo1 = [
                        [1500,ALTO - ALTO/10],
                        [2200,ALTO - ALTO/10]
                      ]

        rocas_tipo2 = [
                        [1900,ALTO - ALTO/6],
                        [2000,ALTO - ALTO/6]
                      ]

        for roca in rocas_tipo1:
            bloque = Plataforma("rock.png",[roca[0],roca[1]])
            self.plataforma_lista.add(bloque)

        for roca in rocas_tipo2:
            bloque = Plataforma("rock2.png",[roca[0],roca[1]])
            self.plataforma_lista.add(bloque)


        #Casa boss
        casa_boss = Plataforma("casa_boss.png",[4100,ALTO - ALTO/3.5])
        self.plataforma_lista.add(casa_boss)

        #---------------Enemigos-----------------------

        zombies_tipo1 = [
                          [505,ALTO - ALTO/5 - 30],
                          [505 + 490,30]
                        ]

        zombies_tipo2 = [
                          [505 + 100,ALTO - 30],
                          [505 + 490 + 100, ALTO - 30 ]
                        ]

        zombies_tipo3 = [
                          [1900, ALTO/3 - 25 - 30],
                          [3000 - 30, ALTO/3 - 25 - 30]
                        ]

        for zombie in zombies_tipo1:
            e = Zombie1("zombies1.png",[zombie[0],zombie[1]])
            self.enemigos_lista.add(e)

        for zombie in zombies_tipo2:
            e = Zombie2("zombies2.png",[zombie[0],zombie[1]],self)
            self.enemigos_lista.add(e)

        for zombie in zombies_tipo3:
            e = Zombie3("zombies3.png",[zombie[0],zombie[1]],self)
            self.enemigos_lista.add(e)

class Nivel_02(Nivel):
    """ Definicion para el nivel 2. """

    def __init__(self, jugador,imagen,sonido):
        """ Creamos nivel 2. """

        # Llamamos al padre
        Nivel.__init__(self, jugador,imagen,sonido)
        self.limite = -1000

        plataforma_tipo4 = [
                             [100, ALTO/3 - 25],
                             [0, ALTO/2],
                             [1200, ALTO - ALTO/5],
                             [1400, ALTO - ALTO/3]
                            ]

        plataforma_tipo5 = [
                             [400, ALTO - ALTO/7],
                             [300, ALTO - ALTO/4],
                             [500, ALTO - ALTO/7],
                             [600, ALTO - ALTO/4],
                             [1800, ALTO - ALTO/4],
                             [1600, ALTO - ALTO/7],
                            ]

        plataforma_tipo6 = [
                             [800, ALTO/2],
                             [1000, ALTO/3],
                            ]


        for plataforma in plataforma_tipo4:
            bloque = Plataforma("plataforma4.png",[plataforma[0],plataforma[1]])
            self.plataforma_lista.add(bloque)

        for plataforma in plataforma_tipo5:
            bloque = Plataforma("plataforma5.png",[plataforma[0],plataforma[1]])
            self.plataforma_lista.add(bloque)

        for plataforma in plataforma_tipo6:
            bloque = Plataforma("plataforma6.png",[plataforma[0],plataforma[1]])
            self.plataforma_lista.add(bloque)

        caja_tipo3 = [
                       [400, ALTO/3],
                       [400 + 100 - 25, ALTO/3 + 100 - 20],
                       [400 + 100*2 - 45, ALTO/3]
                     ]

        for caja in caja_tipo3:
            bloque = Plataforma("caja3.png",[caja[0],caja[1]])
            self.plataforma_lista.add(bloque)
