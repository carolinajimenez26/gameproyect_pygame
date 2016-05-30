import pygame
from objetos import *


class PlataformaChichi(pygame.sprite.Sprite):
    """ Plataforma donde el usuario puede subir """

    def __init__(self, ancho, alto):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([ancho, alto])
        self.image.fill(VERDE)

        self.rect = self.image.get_rect()

class Nivel(object):
    """ Esta es una superclase usada para definir un nivel
        Se crean clases hijas por cada nivel que desee emplearse """

    # Lista de sprites usada en todos los niveles. Add or remove
    plataforma_lista = None
    enemigos_lista = None

    # Imagen de Fondo
    #fondo = None
    fondo = pygame.image.load("images/fondo6.jpg")
    #valor desplazamiento de fondo
    mov_fondo = 0

    def __init__(self, jugador):
        self.plataforma_lista = pygame.sprite.Group()
        self.enemigos_lista = pygame.sprite.Group()
        self.jugador = jugador

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
        sonido.stop()

class Nivel_01(Nivel):
    """ Definition for level 1. """

    def __init__(self, jugador):
        """ Creamos nivel 1. """

        # Llamamos al padre
        Nivel.__init__(self, jugador)
        #self.fondo = pygame.image.load("espacio2.jpg")#cambia la img del nivel
        self.limite = -3000
        self.jugador = jugador
        self.sonido = load_sound("nivel1.wav",curdir).play()
        # Arreglo con posiciones de las plataformas
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

        uno = Zombie("zombies1.png",[505,ALTO - ALTO/5 - 10])

        self.enemigos_lista.add(uno)# = self.createEnemies()

    def StopSound(self):
        self.sonido.stop()


class Nivel_02(Nivel):
    """ Definicion para el nivel 2. """

    def __init__(self, jugador):
        """ Creamos nivel 2. """

        # Llamamos al padre
        Nivel.__init__(self, jugador)
        self.limite=-1000
        self.sonido = load_sound("nivel2.wav",curdir).play()
        # Arreglo con ancho, alto, x, y de la plataforma
        nivel = [ [210, 50, 500, 500],
                 [210, 50, 200, 400],
                 [210, 50, 1000, 520],
                 [210, 50, 1200, 300],
                 ]

        """for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)"""

    def StopSound(self):
        self.sonido.stop()
