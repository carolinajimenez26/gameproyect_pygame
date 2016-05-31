import pygame
from imports import *
from objetos import *
from niveles import *

if __name__ == "__main__":
    """ Programa principal """
    pygame.init()
    tam = [ANCHO, ALTO]
    pantalla = pygame.display.set_mode(tam)

    pygame.display.set_caption("Place of Dead - Hunting Rabbits ", 'Spine Runtime')
    tipo = pygame.font.SysFont("monospace", 15)

    # Creamos maximus
    maximus = Jugador("maximus_der.jpg")

    maximus.rect.x = 340
    maximus.rect.y = ALTO - maximus.rect.height

    # Creamos los niveles
    nivel_lista = []
    nivel_lista.append( Nivel_01(maximus) )
    nivel_lista.append( Nivel_02(maximus) )

    # Establecemos nivel actual
    nivel_actual_no = 0
    nivel_actual = nivel_lista[nivel_actual_no]

    # Indicamos a la clase jugador cual es el nivel
    maximus.nivel = nivel_actual

    #sonidos
    shot_s = load_sound('shot.wav',curdir)

    #Grupos de sprites
    ls_todos = pygame.sprite.Group()
    ls_balaj = pygame.sprite.Group()
    ls_enemigos = pygame.sprite.Group()
    ls_balase = pygame.sprite.Group()
    ls_jugadores = pygame.sprite.Group()
    ls_vidas = pygame.sprite.Group()
    # Lista de sprites activos
    activos_sp_lista = pygame.sprite.Group()

    activos_sp_lista.add(maximus)

    fin = False

    # Controlamos que tan rapido actualizamos pantalla
    reloj = pygame.time.Clock()

    #Variables del reloj
    con_cuadros = 0
    tasa_cambio = 60
    tiempo_ini = 10
    seflim = 0

    terminar = False
    disparo = False

    nivel_actual.StartSound()
    # -------- Ciclo del juego -----------
    while not fin:

        #---------tiempo en pantalla------------
        total_segundos=con_cuadros // tasa_cambio
        minutos= total_segundos // 60
        segundos = total_segundos % 60
        tiempo_final = "Tiempo: {0:02}:{1:02}".format(minutos,segundos)
        if total_segundos >60:
          total_segundos=0

        reloj2 = tipo.render(tiempo_final, True, BLANCO)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    maximus.ir_izq()
                    maximus.setDir(1)
                if event.key == pygame.K_RIGHT:
                    maximus.ir_der()
                    maximus.setDir(0)
                if event.key == pygame.K_UP:
                    print "salto"
                    maximus.salto()
                if event.key == pygame.K_SPACE:
                    bala = Bullet('bala.png',maximus.getPos())#la posicion inicial depende de objeto que este disparando
                    dir = maximus.getDir()
                    bala.setDir(dir)
                    shot_s.play()
                    if(dir == 0):#derecha
                        bala.setPos([maximus.getPos()[0] + maximus.getMargen()[0]/2,maximus.getPos()[1]])
                    if(dir == 1):#izquierda
                        print "left"
                        bala.setPos([maximus.getPos()[0] - maximus.getMargen()[0]/2,maximus.getPos()[1]])

                    ls_balaj.add(bala)
                    ls_todos.add(bala)
                    disparo = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and maximus.vel_x < 0:
                    maximus.no_mover()
                if event.key == pygame.K_RIGHT and maximus.vel_x > 0:
                    maximus.no_mover()

        # Actualizamos al maximus.
        activos_sp_lista.update()

        # Actualizamos elementos en el nivel
        nivel_actual.update()

        #  Si el maximus se aproxima al limite derecho de la pantalla (-x)
        if maximus.rect.x >= 500:
            dif = maximus.rect.x - 500
            maximus.rect.x = 500
            nivel_actual.Mover_fondo(-dif)

        # Si el maximus se aproxima al limite izquierdo de la pantalla (+x)
        if maximus.rect.x <= 120:
           dif = 120 - maximus.rect.x
           maximus.rect.x = 120
           nivel_actual.Mover_fondo(dif)

        #si pos maximus se ha desplazado hasta el limite del nivel
        #Si llegamos al final del nivel
        pos_actual = maximus.rect.x + nivel_actual.mov_fondo
        if pos_actual < nivel_actual.limite:
            maximus.rect.x = 120
            if nivel_actual_no < len(nivel_lista)-1:
                nivel_actual.StopSound()
                nivel_actual_no += 1
                nivel_actual = nivel_lista[nivel_actual_no]
                nivel_actual.StartSound()
                maximus.nivel = nivel_actual
            else: #se acabaron los niveles
                fin = True
                print "se acabo"


        # Dibujamos y refrescamos

        nivel_actual.draw(pantalla)
        activos_sp_lista.draw(pantalla)
        reloj.tick(tasa_cambio)

        #Actualizaciones
        #pantalla.blit(fondo,[0,0])
        ls_todos.draw(pantalla)
        ls_enemigos.draw(pantalla)
        ls_todos.update()

        pygame.display.flip()
