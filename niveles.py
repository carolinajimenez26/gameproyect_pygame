import pygame
from objetos import *


class Plataforma(pygame.sprite.Sprite):
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
        self.limite=-1000
        self.sonido = load_sound("nivel1.wav",curdir).play()
        # Arreglo con ancho, alto, x, y de la plataforma
        nivel = [ [210, 50, 500, 520],
                  [210, 70, 800, 400],
                  [210, 70, 1000, 500],
                  [210, 70, 1120, 300],
                 ]


        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            self.plataforma_lista.add(bloque)


class Nivel_02(Nivel):
    """ Definicion para el nivel 2. """

    def __init__(self, jugador):
        """ Creamos nivel 2. """

        # Llamamos al padre
        Nivel.__init__(self, jugador)
        self.limite=-1000
        # Arreglo con ancho, alto, x, y de la plataforma
        nivel = [ [210, 50, 500, 500],
                 [210, 50, 200, 400],
                 [210, 50, 1000, 520],
                 [210, 50, 1200, 300],
                 ]

        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)
