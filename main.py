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
    nivel1 = Nivel_01(maximus,"images/fondo6.jpg","nivel1.wav")
    nivel_lista.append( nivel1 )
    nivel2 = Nivel_02(maximus,"images/dracula.jpg","nivel2.wav")
    nivel_lista.append( nivel2 )


    # Establecemos nivel actual
    nivel_actual_no = 0
    maximus.setPos([300, ALTO/2])
    nivel_actual = nivel_lista[nivel_actual_no]

    # Indicamos a la clase jugador cual es el nivel
    maximus.nivel = nivel_actual

    #sonidos
    shot_s = load_sound('shot.wav',curdir)

    #Grupos de sprites
    ls_todos = pygame.sprite.Group()
    ls_balaj = pygame.sprite.Group()
    ls_enemigos_nivel1 = nivel1.getEnemies()
    ls_enemigos_nivel2 = nivel2.getEnemies()
    ls_balase = pygame.sprite.Group()
    ls_jugadores = pygame.sprite.Group()
    # Lista de sprites activos
    activos_sp_lista = pygame.sprite.Group()

    activos_sp_lista.add(maximus)
    ls_jugadores.add(maximus)

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

    #para saber que pantalla ejecutar cuando termine el ciclo
    game_over = False
    winner = False

    nivel_actual.StartSound()
    # -------- Ciclo del juego -----------
    while not fin:

        if(maximus.getLife() <= 0): #si muere
            ls_todos.draw(pantalla)
            pygame.display.flip()
            ls_todos.draw(pantalla)
            pygame.display.flip()
            nivel_actual.StopSound()
            reloj.tick(0.3) #para que no sea un cambio tan repentino
            fin = True #sale del ciclo
            game_over = True

        ##En el nivel2 no puede tocar el suelo, pierde
        if((maximus.getPos()[1] == ALTO - maximus.getMargen()[1]) and nivel_actual_no != 0):
            print "gameover"
            #fin = True
            game_over = True

        #si mato a todos los enemigos y esta en el nivel2
        if((len(ls_enemigos_nivel2) == 0 ) and (nivel_actual_no == 2)):
            nivel_actual.StopSound()
            reloj.tick(0.6)
            fin = True
            winner = True

        #---------tiempo en pantalla------------
        total_segundos=con_cuadros // tasa_cambio
        minutos= total_segundos // 60
        segundos = total_segundos % 60
        tiempo_final = "Tiempo: {0:02}:{1:02}".format(minutos,segundos)
        if total_segundos >60:
          total_segundos=0

        reloj2 = tipo.render(tiempo_final, True, BLANCO)
        tipo = pygame.font.SysFont("monospace", 15)
        blood = tipo.render("Vida actual: " ,1, (255,0,0))
        pantalla.blit(blood, (0, ALTO))
        point = tipo.render(("Puntos: " + str(maximus.getScore())),1, (0,0,0))

        if(maximus.getLife() > 0):
          point = tipo.render(("Puntos: " + str(maximus.getScore())),1, (255,0,0))

        pantalla.fill(pygame.Color(0,0,0))

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
                    maximus.salto()
                    if(nivel_actual_no != 0):
                        maximus.setDir(2)
                if event.key == pygame.K_DOWN and nivel_actual_no != 0:
                    maximus.setDir(3)
                if event.key == pygame.K_SPACE:
                    bala = Bullet('bala.png',maximus.getPos())#la posicion inicial depende de objeto que este disparando
                    dir = maximus.getDir()
                    bala.setDir(dir)
                    shot_s.play()
                    if(dir == 0):#derecha
                        bala.setPos([maximus.getPos()[0] + maximus.getMargen()[0]/2,maximus.getPos()[1]])
                    if(dir == 1):#izquierda
                        bala.setPos([maximus.getPos()[0] - maximus.getMargen()[0]/2,maximus.getPos()[1]])
                    if(dir == 2 and nivel_actual_no != 0):#arriba
                        bala.setPos([maximus.getPos()[0],maximus.getPos()[1] - maximus.getMargen()[1]])
                    if(dir == 3 and nivel_actual_no != 0):#abajo
                        bala.setPos([maximus.getPos()[0],maximus.getPos()[1] + maximus.getMargen()[1]])
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
                maximus.setPos([300, ALTO/2])
            else: #se acabaron los niveles
                fin = True
                print "se acabo"


        #renderiza objetos de informacion en la pantalla
        pantalla.blit(blood,[100,ALTO/2])
        pantalla.blit(point,[300,ALTO+15]) #+ 15])
        pantalla.blit(reloj2, [500,ALTO+15])
        lifebars(maximus,pantalla,[120,ALTO+18])

        # Dibujamos y refrescamos
        nivel_actual.draw(pantalla)
        activos_sp_lista.draw(pantalla)
        reloj.tick(tasa_cambio)

        #Actualizaciones
        ls_todos.draw(pantalla)
        ls_todos.update()

        pygame.display.flip()

    if(game_over):
        print "Perdiste"
    if(winner):
        print "ganaste"
