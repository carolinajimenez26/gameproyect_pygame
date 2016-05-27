import pygame
from funciones import *
from objetos import *

# Constantes

# Colores
NEGRO   = (   0,   0,   0)
BLANCO    = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO      = ( 255,   0,   0)
VERDE    = (   0, 255,   0)

# Dimensiones pantalla
ANCHO  = 600 #depende del fondo
ALTO = 600

if __name__ == "__main__":

    #----------------Definiciones generales------------------
    pygame.init()
    tam = [ANCHO, ALTO]
    pantalla = pygame.display.set_mode(tam)

    pygame.display.set_caption("Place of Dead - Hunting Rabbits ", 'Spine Runtime')
    tipo = pygame.font.SysFont("monospace", 15)

    fondo = load_image('fondo5.jpg',curdir, alpha=False)
    fondo = pygame.transform.scale(fondo, tam)
    pantalla.blit(fondo,[0,0])

    pygame.mouse.set_visible(False) #Oculta el puntero del mouse
    reloj = pygame.time.Clock()

    #sonidos
    shot_s=load_sound('shot.wav',curdir)

    #Grupos de sprites
    ls_todos = pygame.sprite.Group()
    ls_balaj = pygame.sprite.Group()
    ls_enemigos = pygame.sprite.Group()
    ls_balase = pygame.sprite.Group()
    ls_jugadores = pygame.sprite.Group()
    ls_vidas = pygame.sprite.Group()

    #--------------Creacion de personajes--------------
    maximus = Player('maximus_der.jpg',[0,0], ANCHO, ALTO)

    maximus.setPos([maximus.getMargen()[0],ALTO-3*maximus.getMargen()[1]])
    maximus.setSpeed([maximus.getMargen()[0]/10, maximus.getMargen()[1]/10])

    #Agrega las imagenes del magician
    """magician.imaged.append(load_image('dere_1.png',curdir,alpha=True))
    magician.imaged.append(load_image('dere_2.png',curdir,alpha=True))
    magician.imagenar.append(load_image('up_1.png',curdir,alpha=True))
    magician.imagenar.append(load_image('up_2.png',curdir,alpha=True))
    magician.imagei.append(load_image('iz_1.png',curdir,alpha=True))
    magician.imagei.append(load_image('iz_2.png',curdir,alpha=True))
    magician.imagena.append(load_image('ab_1.png',curdir,alpha=True))
    magician.imagena.append(load_image('ab_2.png',curdir,alpha=True))"""

    ls_todos.add(maximus)
    ls_jugadores.add(maximus)


    #Variables del reloj
    con_cuadros = 0
    tasa_cambio = 60
    tiempo_ini = 10
    seflim = 0

    terminar = False
    disparo = False

    while (not terminar):

        #---------tiempo en pantalla------------
        total_segundos=con_cuadros // tasa_cambio
        minutos= total_segundos // 60
        segundos = total_segundos % 60
        tiempo_final = "Tiempo: {0:02}:{1:02}".format(minutos,segundos)
        if total_segundos >60:
          total_segundos=0

        reloj2 = tipo.render(tiempo_final, True, blanco)


        #Recibe cual es la tecla que esta siendo presionada
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            #Quitar
            if event.type  == pygame.QUIT:
              terminar = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    bala = Bullet('bala.png',maximus.getPos())#la posicion inicial depende de objeto que este disparando
                    dir = maximus.getDir()
                    bala.setDir(dir)
                    shot_s.play()
                    if(dir == 0):#derecha
                        bala.setPos([maximus.getPos()[0] + maximus.getRect()[2]/2,maximus.getPos()[1]])
                    if(dir == 1):#izquierda
                        bala.setPos([maximus.getPos()[0] - maximus.getRect()[2]/2,maximus.getPos()[1]])
                    if(dir == 2):#arriba
                        bala.setPos([maximus.getPos()[0],maximus.getPos()[1] - maximus.getRect()[3]])
                    if(dir == 3):#abajo
                        bala.setPos([maximus.getPos()[0],maximus.getPos()[1] + maximus.getRect()[3]])

                    ls_balaj.add(bala)
                    ls_todos.add(bala)
                    disparo = True

        if keys[pygame.K_a]:
            maximus.moveLeft()
            maximus.setDir(1)

        if keys[pygame.K_d]:
            maximus.moveRight()
            maximus.setDir(0)

        if keys[pygame.K_ESCAPE]:
          #pantalla_s.stop()
          terminar = True

        #Actualizaciones
        pantalla.blit(fondo,[0,0])
        ls_todos.draw(pantalla)
        ls_enemigos.draw(pantalla)
        ls_todos.update()
        pygame.display.flip()
        reloj.tick(tasa_cambio)
