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
    #maximus.setPos([300, ALTO/2])
    nivel_actual = nivel_lista[nivel_actual_no]

    # Indicamos a la clase jugador cual es el nivel
    maximus.nivel = nivel_actual

    #sonidos
    shot_s = load_sound('shot.wav',curdir)

    #Grupos de sprites
    ls_balaj = pygame.sprite.Group() #balas jugador
    ls_enemigos_nivel1 = nivel1.getEnemies() #lista enemigos nivel1
    ls_enemigos_nivel2 = nivel2.getEnemies() #lista enemigos nivel2
    ls_balase = pygame.sprite.Group() #balas enemigos
    ls_jugadores = pygame.sprite.Group() #jugadores
    # Lista de sprites activos
    activos_sp_lista = pygame.sprite.Group()

    #listas para objetos

    #NIVEL1
    ls_todos_nivel1 = pygame.sprite.Group()
    ls_mascota_nivel1 = pygame.sprite.Group()#Mascota
    ls_vida_nivel1 = pygame.sprite.Group()#Pavos(vida)
    ls_mascota_nivel1 = pygame.sprite.Group()#Mascota
    ls_zapatos_nivel1 = pygame.sprite.Group()#Zapatos
    ls_monedas_nivel1 = pygame.sprite.Group()#Monedas
    ls_relojes_nivel1 = pygame.sprite.Group()#Relojes
    ls_municiones_nivel1 = pygame.sprite.Group()#Municiones
    #NIVEL2
    ls_todos_nivel2 = pygame.sprite.Group()
    ls_vida_nivel2 = pygame.sprite.Group()#Rayo
    ls_mascota_nivel2 = pygame.sprite.Group()#Mascota

    #---------------Objetos NIVEL1-----------------------

    mascota = Plataforma("mascota.png",[2150,ALTO - 25])
    ls_mascota_nivel1.add(mascota)
    #ls_todos_nivel1.add(mascota)

    pavos = [
              [1757,ALTO - ALTO/3 - 35],
              [3300,ALTO - 35]
            ]

    for pavo in pavos:
        obj = Plataforma("pavo.png",[pavo[0],pavo[1]])
        ls_vida_nivel1.add(obj)
        ls_todos_nivel1.add(obj)

    zapatos = Plataforma("zapatos.png",[650 + 2*80 + 25,(ALTO - ALTO/2) - 2*80 - 25])
    ls_zapatos_nivel1.add(zapatos)
    ls_todos_nivel1.add(zapatos)

    monedas = [
                [3150,ALTO - 50],
                [3100,ALTO - 50],
                [990 + 50 + 50*1, ALTO/10 - 50],
                [990 + 50 + 50*3, ALTO/10 - 50],
                [990 + 50+ 50*5, ALTO/10 - 50],
              ]

    for moneda in monedas:
        obj = Plataforma("coin.png",[moneda[0],moneda[1]])
        ls_monedas_nivel1.add(obj)
        ls_todos_nivel1.add(obj)

    reloj = Plataforma("reloj.png",[3000 - 400 + 65, ALTO/3 - 25 - 45])
    ls_relojes_nivel1.add(reloj)
    ls_todos_nivel1.add(reloj)

    municiones = [
                   [3500 - 30 - 40*1*2, ALTO/3 - 60],
                   [3500 - 30 - 40*3*2, ALTO/3 - 60],
                   [3500 - 30 - 40*5*2, ALTO/3 - 60]
                 ]

    for municion in municiones:
        obj = Plataforma("municion.png",[municion[0],municion[1]])
        ls_municiones_nivel1.add(obj)
        ls_todos_nivel1.add(obj)

    #---------------Objetos NIVEL2-----------------------
    rayo = Plataforma("rayo.png",[1050,ALTO/4 + 20])
    ls_vida_nivel2.add(rayo)
    ls_todos_nivel2.add(rayo)

    mascota = Plataforma("mascota.png",[500,ALTO/3 + 100 - 60])
    ls_mascota_nivel2.add(mascota)
    ls_todos_nivel2.add(mascota)

    print "len 1 : " ,len(ls_todos_nivel1) , "len 2 : " , len(ls_todos_nivel2)

    #Agregando objetos a grupos de sprites
    activos_sp_lista.add(maximus)
    ls_jugadores.add(maximus)

    fin = False
    flag = False
    cont = 0

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
        total_segundos = con_cuadros // tasa_cambio
        minutos= total_segundos // 60
        segundos = total_segundos % 60
        tiempo_final = "Tiempo: {0:02}:{1:02}".format(minutos,segundos)
        if total_segundos > 60:
          total_segundos=0

        con_cuadros+=1
        #-----------------------------------------

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
                    #ls_todos.add(bala)
                    disparo = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and maximus.vel_x < 0:
                    maximus.no_mover()
                if event.key == pygame.K_RIGHT and maximus.vel_x > 0:
                    maximus.no_mover()

        #Collides NIVEL1
        if(nivel_actual_no == 0):
            maximus.enemigos = len(ls_enemigos_nivel1)
            for enemigo in ls_enemigos_nivel1:
                if(checkCollision(maximus,enemigo)): # si se choco
                    if(cont == 0):
                        maximus.crash()
                        print "life : " , maximus.getLife()
                        lifebars(maximus,pantalla,[ANCHO/2,ALTO])#cambia la bara de vida
                        flag = True

            #collide con pavos
            ls_vidas_i = pygame.sprite.spritecollide(maximus, ls_vida_nivel1, True)
            for vida in ls_vidas_i:
                #ls_vida_nivel1.remove(vida)
                ls_todos.remove(vida)
                #nivel1.removeElement(vida)
                maximus.setLife(maximus.getLife()+10)
                lifebars(maximus,pantalla,[ANCHO/2,ALTO])#cambia la bara de vida

        #Collides NIVEL2
        if(nivel_actual_no == 1):
            maximus.enemigos = len(ls_enemigos_nivel2)
            for enemigo in ls_enemigos_nivel2:
                if(checkCollision(maximus,enemigo)): # si se choco
                    if(cont == 0):
                        maximus.crash()
                        print "life : " , maximus.getLife()
                        lifebars(maximus,pantalla,[ANCHO/2,ALTO])#cambia la bara de vida
                        flag = True

            #collide con pavos
            ls_vidas_i = pygame.sprite.spritecollide(maximus, ls_vida_nivel2, True)
            for vida in ls_vidas_i:
                #ls_vida_nivel1.remove(vida)
                ls_todos.remove(vida)
                #nivel1.removeElement(vida)
                maximus.setLife(maximus.getLife()+10)
                lifebars(maximus,pantalla,[ANCHO/2,ALTO])#cambia la bara de vida

        if(flag):
            cont += 1
        if(cont >= 8):
            cont = 0

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
                #fin = True
                print "se acabo"


        #------------Nivel1--------------
        if(nivel_actual_no == 0):
            #ls_todos_nivel1.draw(pantalla)

            #ls_todos_nivel1
            print "ls_mascota: " , ls_mascota_nivel1
            ls_mascota_nivel1.draw(pantalla)
            """ls_vida_nivel1.draw(pantalla)
            ls_mascota_nivel1.draw(pantalla)
            ls_zapatos_nivel1.draw(pantalla)
            ls_monedas_nivel1.draw(pantalla)
            ls_relojes_nivel1.draw(pantalla)
            ls_municiones_nivel1.draw(pantalla)"""

            #ls_todos_nivel1.update()
            ls_mascota_nivel1.update()
            """ls_vida_nivel1.update()
            ls_mascota_nivel1.update()
            ls_zapatos_nivel1.update()
            ls_monedas_nivel1.update()
            ls_relojes_nivel1.update()
            ls_municiones_nivel1.update()"""

        #------------Nivel2--------------
        if(nivel_actual_no == 1):
            ls_todos_nivel2.draw(pantalla)
            ls_todos_nivel2.update()

        # Dibujamos y refrescamos
        nivel_actual.draw(pantalla)
        activos_sp_lista.draw(pantalla)

        # Actualizamos al jugador
        activos_sp_lista.update()

        ls_balaj.draw(pantalla)
        ls_balaj.update()

        # Actualizamos elementos en el nivel
        nivel_actual.update()

        #------------General--------------
        #renderiza objetos de informacion en la pantalla
        pantalla.blit(blood,[5,ALTO - ALTO+15])
        pantalla.blit(point,[5,(ALTO - ALTO+15) + 15]) #+ 15])
        pantalla.blit(reloj2, [5,(ALTO - ALTO+15) + 15*2])
        lifebars(maximus,pantalla,[120,(ALTO - ALTO+15)])

        pygame.display.flip()
        reloj.tick(tasa_cambio)

    #---------------Fin del ciclo-----------------

    if(game_over):
        print "Perdiste"
    if(winner):
        print "ganaste"
