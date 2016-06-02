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
