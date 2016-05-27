import pygame
from funciones import *
#from objetos import *

# Constantes

# Colores
NEGRO   = (   0,   0,   0)
BLANCO    = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO      = ( 255,   0,   0)
VERDE    = (   0, 255,   0)

# Dimensiones pantalla
ANCHO  = 600 #depende del fondo
ALTO = 400

if __name__ == "__main__":

    pygame.init()
    tam = [ANCHO, ALTO]
    pantalla = pygame.display.set_mode(tam)

    pygame.display.set_caption("Place of Dead - Level 1 ", 'Haunting Rabits')
    tipo = pygame.font.SysFont("monospace", 15)

    fondo = load_image('fondo5.jpg',curdir, alpha=False)
    fondo = pygame.transform.scale(fondo, tam)
    pantalla.blit(fondo,[0,0])

    terminar = False

    while (not terminar):

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                terminar = True

        pygame.display.flip()

"""
    # Creamos jugador
    jugador = Jugador()

    # Creamos los niveles
    nivel_lista = []
    nivel_lista.append( Nivel_01(jugador) )
    nivel_lista.append( Nivel_02(jugador) )

    # Establecemos nivel actual
    nivel_actual_no = 0
    nivel_actual = nivel_lista[nivel_actual_no]

    # Lista de sprites activos
    activos_sp_lista = pygame.sprite.Group()
    # Indicamos a la clase jugador cual es el nivel
    jugador.nivel = nivel_actual

    jugador.rect.x = 340
    jugador.rect.y = ALTO - jugador.rect.height
    activos_sp_lista.add(jugador)

    fin = False

    # Controlamos que tan rapido actualizamos pantalla
    reloj = pygame.time.Clock()

     # -------- Ciclo del juego -----------
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jugador.ir_izq()
                if event.key == pygame.K_RIGHT:
                    jugador.ir_der()
                if event.key == pygame.K_UP:
                    print "salto"
                    jugador.salto()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and jugador.vel_x < 0:
                    jugador.no_mover()
                if event.key == pygame.K_RIGHT and jugador.vel_x > 0:
                    jugador.no_mover()

        # Actualizamos al jugador.
        activos_sp_lista.update()

        # Actualizamos elementos en el nivel
        nivel_actual.update()

        #  Si el jugador se aproxima al limite derecho de la pantalla (-x)
        if jugador.rect.x >= 500:
            dif = jugador.rect.x - 500
            jugador.rect.x = 500
            nivel_actual.Mover_fondo(-dif)

        # Si el jugador se aproxima al limite izquierdo de la pantalla (+x)
        if jugador.rect.x <= 120:
           dif = 120 - jugador.rect.x
           jugador.rect.x = 120
           nivel_actual.Mover_fondo(dif)

        #si pos jugador se ha desplazado hasta el limite del nivel
        #Si llegamos al final del nivel
        pos_actual=jugador.rect.x + nivel_actual.mov_fondo
        if pos_actual < nivel_actual.limite:
           jugador.rect.x=120
           if nivel_actual_no < len(nivel_lista)-1:
              nivel_actual_no += 1
              nivel_actual = nivel_lista[nivel_actual_no]
              jugador.nivel=nivel_actual

        # Dibujamos y refrescamos

        nivel_actual.draw(pantalla)
        activos_sp_lista.draw(pantalla)
        reloj.tick(60)
        pygame.display.flip()

"""
