from objetos import *
from niveles import *
import inputbox
#Imports del tkinter
from Tkinter import *
import tkMessageBox
from ttk import Frame, Button, Style
from PIL import Image, ImageTk
#Fin

# Dimensiones pantalla
ANCHO  = 800
ALTO = 600


#################################################################################################
# _________                   .__                       .__                                ######
# /   _____/ ____   ____  ____ |__| ____   ____     ____ |  | _____    ______ ____   ______######
# \_____  \_/ __ \_/ ___\/ ___\|  |/  _ \ /    \  _/ ___\|  | \__  \  /  ___// __ \ /  ___/######
# /        \  ___/\  \__\  \___|  (  <_> )   |  \ \  \___|  |__/ __ \_\___ \\  ___/ \___ \ ######
#/_______  /\___  >\___  >___  >__|\____/|___|  /  \___  >____(____  /____  >\___  >____  >######
#        \/     \/     \/    \/               \/       \/          \/     \/     \/     \/ ######
#################################################################################################
class window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent



class splashload():
    def __init__(self):
        self.correr=True
        if(self.correr):
            menu_e = pygame.display.set_mode((700, 700))
            pygame.display.set_caption("Loading files ", 'Spine Runtime')
            image = load_image("loading.jpg", curdir+"/enviroment/main", alpha=False)
            image = pygame.transform.scale(image,(700,700))
            menu_e.blit(image,(0,0))
            pygame.display.flip()
        else:
            print "Cerrado como tu gfa :v"
    def setcorrer(self):
        self.correr=False

class buttonz(pygame.sprite.Sprite):
    def __init__(self,img,img2):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img, curdir+"/enviroment/main", alpha=True)
        self.images = [load_image(img, curdir+"/enviroment/main", alpha=True),load_image(img2, curdir+"/enviroment/main", alpha=True)]
        self.index=0
        self.clicked=False
        self.mousepos=[]
    	self.rect = self.image.get_rect()

    def setclicked(self):
        self.clicked=True
    def getrect(self):
        print self.rect

    def setpos(self,pos):
        self.rect.x=pos[0]
        self.rect.y=pos[1]

    def getrect(self):
        return self.rect[2],self.rect[3]

    def getrectpos(self):
        return self.rect.x,self.rect.y

    def action(self):
        print "Empy button - Report bug"

    def update(self):
        x_len,y_len = self.getrect()
        button_x,button_y = self.getrectpos()
        mos_x, mos_y = pygame.mouse.get_pos()
        if mos_x>button_x and (mos_x<button_x+x_len):
            x_inside = True
        else:
            x_inside = False
        if mos_y>button_y and (mos_y<button_y+y_len):
            y_inside = True
        else:
            y_inside = False
        if x_inside and y_inside:
            if self.clicked:
                self.image=self.images[1]
                self.clicked=False
                self.action()
            else:
                self.image=self.images[1]
        else:
            self.clicked=False
            self.image=self.images[0]



class boton_continuar(buttonz):
    def __init__(self,img,img2):
        buttonz.__init__(self,img,img2)
        self.flag=False

    def action(self):
        if(self.flag):
            return True
        else:
            return False

    def update(self):
        x_len,y_len = self.getrect()
        button_x,button_y = self.getrectpos()
        mos_x, mos_y = pygame.mouse.get_pos()
        if mos_x>button_x and (mos_x<button_x+x_len):
            x_inside = True
        else:
            x_inside = False
        if mos_y>button_y and (mos_y<button_y+y_len):
            y_inside = True
        else:
            y_inside = False
        if x_inside and y_inside:
            if self.clicked:
                self.image=self.images[1]
                self.clicked=False
                self.flag=True
                self.action()
            else:
                self.flag=False
                self.image=self.images[1]
        else:
            self.clicked=False
            self.image=self.images[0]



class boton_inicio(buttonz):
    def __init__(self,img,img2):
        buttonz.__init__(self,img,img2)

    def pause(self,pt):
        menupp=False
        #pygame.image.save(pt, "example.jpg")
        pr = pt.subsurface([0,0,800,600]) #Dibuja una surface sobre la pantalla
        pr.fill((255,255,255))
        ad1 = pygame.image.load(dirimg+'pausa.jpg')
        ad1 = pygame.transform.scale(ad1,(800,600))
        lsbtn = pygame.sprite.Group()
        cerrarpau=False
        btn1 = boton_continuar("btnco.png","btnco_p.png")
        btn2 = boton_ajustes("btn2.png","btn2_p.png",pr,0,(800,600),False)
        btn3 = boton_continuar("btnmenu.png","btnmenu_p.png")
        rex,rey = btn1.getrect()
        btn1.setpos([800/2-rex/2,600/2-rey-50])
        btn2.setpos([800/2-rex/2,600/2-rey+100])
        btn3.setpos([800/2-rex/2,600/2-rey+250])
        lsbtn.add(btn2)
        lsbtn.add(btn1)
        lsbtn.add(btn3)

        cerrar=False
        pr.blit(ad1,(0,0))
        while not(cerrar):
            for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                #    cerrar=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        cerrar=True
                if event.type == pygame.MOUSEBUTTONUP:
                    for btn in lsbtn:
                        btn.setclicked()

                pr.blit(ad1,(0,0))
                lsbtn.draw(pr)
                lsbtn.update()
                cerrar=btn1.action()
                menupp=btn3.action()
                if(menupp):
                    cerrar=True
                pygame.display.flip()
        return menupp
    def action(self):
        pygame.mixer.music.stop()

        pygame.init()
        tam = [ANCHO, ALTO]
        pantalla = pygame.display.set_mode(tam)

        pygame.display.set_caption("Place of Dead - Hunting Rabbits ", 'Spine Runtime')
        tipo = pygame.font.SysFont("monospace", 15)

        # Creamos maximus
        #maximus = Jugador("maximus_der.jpg")
        maximus = Jugador()

        maximus.rect.x = 340
        maximus.rect.y = ALTO - maximus.rect.height
        # Creamos los niveles
        nivel_lista = []
        nivel1 = Nivel_01(maximus,dirimg+"fondo6.jpg",dirsonido+"nivel1.wav")
        nivel_lista.append( nivel1 )
        nivel2 = Nivel_02(maximus,dirimg+"dracula.jpg",dirsonido+"nivel2.wav")
        nivel_lista.append( nivel2 )

        # Establecemos nivel actual
        nivel_actual_no = 0
        maximus.setPos([300, ALTO/2])
        nivel_actual = nivel_lista[nivel_actual_no]

        # Indicamos a la clase jugador cual es el nivel
        maximus.nivel = nivel_actual

        for en in nivel_actual.enemigos_lista:
            en.nivel=nivel_actual

        #sonidos
        shot_s = load_sound('enviroment/levels/sounds/shot.wav',curdir)
        shot_se = load_sound('enviroment/levels/sounds/shot2.wav',curdir)
        grunt = load_sound('enviroment/levels/sounds/gruntsound.wav',curdir)
        scream = load_sound('enviroment/levels/sounds/scream.ogg',curdir)
        moneda = load_sound('enviroment/levels/sounds/coin.ogg',curdir)
        reloj_s = load_sound('enviroment/levels/sounds/ticking_clock.ogg',curdir)
        gotlife = load_sound('enviroment/levels/sounds/gotLife.ogg',curdir)
        charge = load_sound('enviroment/levels/sounds/charge.ogg',curdir)

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

        #Agregando objetos a grupos de sprites
        activos_sp_lista.add(maximus)
        ls_jugadores.add(maximus)

        fin = False
        flag = False
        cont = 0
        flag2 = False
        cont2 = 0
        flag3 = False
        cont3 = 0
        flag4 = False
        cont4 = 0
        flag5 = False
        cont5 = 0
        flag6 = False
        cont6 = 0
        flag7 = False
        cont7 = 0
        flag8 = False
        cont8 = 0
        cont_arena = 400 #tiempo en el que se quedan parados
        countdown = False
        cont_zap = 400 #tiempo en el que tiene zapatos
        countdown_zap = False
        one_time = False
        give_life = True

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

        """for e in ls_enemigos_nivel2:
            e.StartMovements()"""

        closep = False
        Config.read("config.ini")
        Config.sections()
        derecha = ConfigSectionMap("Movimientos")['derecha']
        izquierda = ConfigSectionMap("Movimientos")['izquierda']
        disparo = ConfigSectionMap("Movimientos")['disparo']
        salto = ConfigSectionMap("Movimientos")['salto']
        derecha=int(derecha)
        izquierda=int(izquierda)
        disparo=int(disparo)
        salto=int(salto)

        ls_balasboss = pygame.sprite.Group()
        # -------- Ciclo del juego -----------
        while not fin:
            #maximus.setLife(100)#vida infinita
            for en in nivel_actual.enemigos_lista:
                en.plat = nivel_actual.getElements()

            if(maximus.score >= 100 and give_life): #regala vida si cumple este puntaje
                give_life = False
                maximus.setLife(100)
                gotlife.play()
                print "you got a life!"

            #Colision de las balas con la plataforma
            for bil in ls_balaj:
                for plat in nivel_actual.getElements():
                    if(checkCollision(bil,plat)): # si se choco
                        if not(plat.tipo == "mascota"): #ESCUDO
                            ls_balaj.remove(bil)

            for bile in ls_balase:
                ls_impactos = pygame.sprite.spritecollide(bile,nivel_actual.getElements(), False)
                for impacto in ls_impactos:
                    ls_balase.remove(bile)

            if(maximus.getLife() <= 0): #si muere
                nivel_actual.StopSound()
                reloj.tick(60) #para que no sea un cambio tan repentino
                fin = True #sale del ciclo
                game_over = True

            ##En el nivel2 no puede tocar el suelo, pierde
            if((maximus.getPos()[1] == ALTO - maximus.getMargen()[1]) and nivel_actual_no != 0):
                print "gameover"
                nivel_actual.StopSound()
                fin = True
                game_over = True

            #si mato a todos los enemigos y esta en el nivel2
            if((len(ls_enemigos_nivel2) == 0 ) and (nivel_actual_no == 1)):
                nivel_actual.StopSound()
                reloj.tick(1)
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
            municiones = tipo.render(("Municiones: " + str(maximus.municion)),1, ROJO)

            if(maximus.getLife() > 0):
              point = tipo.render(("Puntos: " + str(maximus.getScore())),1, (255,0,0))

            pantalla.fill(pygame.Color(0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        closep = self.pause(pantalla)

                    if event.key == pygame.K_b:
                        print maximus.getPos()

                    if event.key == pygame.K_LEFT:
                        maximus.ir_izq()
                        maximus.setDir(1)

                        if(nivel_actual_no == 0):

                            for e in ls_enemigos_nivel1:
                                if(e.tipo == 2 ):
                                    e.restartMovements(maximus.getPos())
                                    e.setDir(1)


                            for e in ls_balase:
                                if(e.tipo == "rata"):
                                    e.restartMovements(maximus.getPos())

                    if event.key == pygame.K_RIGHT:
                        maximus.ir_der()
                        maximus.setDir(0)
                        if(nivel_actual_no == 0):

                            for e in ls_enemigos_nivel1:
                                if(e.tipo == 2 ):
                                    e.restartMovements(maximus.getPos())
                                    e.setDir(0)

                            for e in ls_balase:
                                if(e.tipo == "rata"):
                                    e.restartMovements(maximus.getPos())

                    if event.key == pygame.K_UP:
                        maximus.salto()

                        if(nivel_actual_no != 0):
                            maximus.setDir(2)

                        for e in ls_balase:
                            if(e.tipo == "rata"):
                                e.restartMovements(maximus.getPos())

                    if event.key == pygame.K_SPACE:
                        if(maximus.municion > 0): #si tiene municiones
                            bala = Bullet(dirimg+'bala.png',maximus.getPos())#la posicion inicial depende de objeto que este disparando
                            dir = maximus.getDir()
                            bala.setDir(dir)
                            shot_s.play()
                            maximus.municion -= 1 #le quita una municion
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

            #---------------NIVEL1--------------------------
            #----------------Collides-------------------------
            if(nivel_actual_no == 0):
                maximus.enemigos = len(ls_enemigos_nivel1)
                for enemigo in ls_enemigos_nivel1:
                    if(checkCollision(maximus,enemigo)): # si se choco
                        if(cont == 0):
                            maximus.crash()

                            if(enemigo.tipo == 2):
                                aux = maximus.getMargen()[0]
                                if(maximus.getDir() == 0):#der
                                    aux *= -1
                                maximus.setPos([maximus.getPos()[0]+aux,maximus.getPos()[1]])

                            print "life : " , maximus.getLife()
                            lifebars(maximus,pantalla,[ANCHO/2,ALTO])#cambia la bara de vida
                            flag = True


                for enemigo in ls_enemigos_nivel1:
                    for bala in ls_balaj:
                        if(checkCollision(bala,enemigo)): # si se choco
                            if(cont == 0):
                                enemigo.crash()
                                grunt.play() #se queja
                                ls_balaj.remove(bala)
                                ls_todos_nivel1.remove(bala)
                                #ls_todos_nivel2.remove(bala)
                                flag2 = True
                                if(enemigo.getLife() <= 0):
                                    maximus.score += 20
                                    ls_enemigos_nivel1.remove(enemigo)



                #Colision bala enemigo
                for bala in ls_balase:
                    if(checkCollision(bala,maximus)): # si le disparan a maximus
                        if(cont4 == 0):
                            maximus.setLife(maximus.getLife()-1)
                            flag4 = True

                #Colision modificadores con maximus
                ls_modificadores = pygame.sprite.spritecollide(maximus, nivel_actual.plataforma_lista, True)
                for m in ls_modificadores:
                    if(m.tipo == "pavo"):
                        print "pavo"
                        nivel_actual.plataforma_lista.remove(m)
                        maximus.setLife(maximus.getLife() + random.randrange(8,15))
                        print "life : " , maximus.getLife()
                    if(m.tipo == "zapatos"):
                        print "zapatos"
                        nivel_actual.plataforma_lista.remove(m)
                        maximus.increment_x += 5
                        countdown_zap = True
                        one_time = True
                    if(m.tipo == "mascota"):
                        print "mascota"
                        new = Mascota(dirimg+"escudo.png",m.getPos())
                        new.tipo = "mascota"
                        new.tipo2 = "escudo"
                        new.jugador = maximus
                        new.StartMovements()
                        nivel_actual.plataforma_lista.remove(m)
                        nivel_actual.plataforma_lista.add(new)
                    if(m.tipo == "moneda"):
                        print "moneda"
                        nivel_actual.plataforma_lista.remove(m)
                        moneda.play()
                        maximus.score += random.randrange(5,10)
                    if(m.tipo == "reloj"):
                        print "reloj"
                        nivel_actual.plataforma_lista.remove(m)
                        countdown = True
                        reloj_s.play()
                        for e in ls_enemigos_nivel1:
                            if(e.tipo != 4):
                                e.StopMovements()

                    if(m.tipo == "municion"):
                        charge.play()
                        print "municion"
                        nivel_actual.plataforma_lista.remove(m)
                        maximus.municion += 10

                #--------------------Ataques--------------------
                #Ataque zombie3
                for enemigo in ls_enemigos_nivel1:
                    if(enemigo.tipo == 3):
                        if(cont3 == 0):
                            if(abs(enemigo.getPos()[0] - maximus.getPos()[0]) <= 300):#le dispara si se encuentra cerca
                                flag3 = True
                                bala = Bullet(dirimg+'bala2.png',enemigo.getPos())
                                shot_se.play()
                                ls_balase.add(bala) #lista balas enemigos
                                bala.setDir(enemigo.getDir())
                #Ataque zombie4
                for enemigo in ls_enemigos_nivel1:
                    if(enemigo.tipo == 4):
                        if(cont5 == 0):
                            if(abs(enemigo.getPos()[0] - maximus.getPos()[0]) <= 250):#le dispara si se encuentra cerca
                                flag5 = True
                                rata = Rata(dirimg+'rata.png',enemigo.getPos(),nivel_actual)
                                ls_balase.add(rata) #lista balas enemigos
                                scream.play()

                #Salto zombie tipo5
                for enemigo in ls_enemigos_nivel1:
                    if(enemigo.tipo == 5):
                        enemigo.salto()
                        if(cont8 == 0 and abs(enemigo.getPos()[0] - maximus.getPos()[0]) <= 150):
                            bala = RectBullet(dirimg+'bala2.png',enemigo.getPos())
                            bala.restartMovements(maximus.getPos())
                            ls_balase.add(bala)
                            shot_se.play()
                            flag8 = True

                #----------------------Otros--------------------------
                #Muerte ratas
                for e in ls_balase:
                    if(e.tipo == "rata"):
                        if(e.getLife() <= 0):
                            ls_balase.remove(e) #las ratas se mueren
                            ls_todos_nivel1.remove(e)

                for e in ls_enemigos_nivel1:
                    if(countdown <= 0):
                        if(e.tipo != 4): #este no se mueve
                            e.aux = True # se pueden volver a mover
            #--------------------NIVEL2----------------------------
            #--------------------Collides--------------------------
            if(nivel_actual_no == 1):
                maximus.enemigos = len(ls_enemigos_nivel2)
                for enemigo in ls_enemigos_nivel2:
                    if(checkCollision(maximus,enemigo)): # si se choco
                        if(cont == 0):
                            maximus.crash()
                            print "life : " , maximus.getLife()
                            lifebars(maximus,pantalla,[ANCHO/2,ALTO])#cambia la bara de vida
                            flag = True

                #Colision modificadores con maximus
                ls_modificadores = pygame.sprite.spritecollide(maximus, nivel_actual.plataforma_lista, True)
                for m in ls_modificadores:
                    if(m.tipo == "rayo"):
                        print "elimina rayo"
                        nivel_actual.plataforma_lista.remove(m)
                        maximus.setLife(100) #le devuelve toda la vida
                    if(m.tipo == "municion"):
                        charge.play()
                        print "municion"
                        nivel_actual.plataforma_lista.remove(m)
                        maximus.municion += 10

                for enemigo2 in ls_enemigos_nivel2:
                    for bala in ls_balaj:
                        if(checkCollision(bala,enemigo2)): # si se choco
                            if(cont == 0):
                                enemigo2.crash()
                                ls_balaj.remove(bala)
                                ls_todos_nivel1.remove(bala)
                                ls_todos_nivel2.remove(bala)
                                flag2 = True
                                if(enemigo2.getLife() <= 0):
                                    ls_enemigos_nivel2.remove(enemigo2)


                #Colision bala enemigo
                for bala in ls_balase:
                    if(checkCollision(bala,maximus)): # si le disparan a maximus
                        if(cont7 == 0):
                            maximus.setLife(maximus.getLife()-1)
                            flag7 = True

                #------------------Ataques---------------------------
                for enemigo in ls_enemigos_nivel2:
                    if(cont6 == 0):
                        bala = RectBullet(dirimg+'bala3.png',enemigo.getPos())
                        bala.restartMovements(maximus.getPos())
                        ls_balase.add(bala)
                        shot_se.play()
                        flag6 = True

                #----------------------Otros--------------------------
                #Desaparecen balas
                for e in ls_balase:
                    if(e.getLife() <= 0):
                        ls_balase.remove(e) #las ratas se mueren

            #Para collide con enemigos
            if(flag):
                cont += 1
            if(cont >= 8):
                cont = 0
            #Para collide de balas con enemigos
            if(flag2):
                cont2 += 1
            if(cont2 >= 30):
                cont2 = 0
            #Para disparo zombie tipo3
            if(flag3):
                cont3 += 1
            if(cont3 >= 50):
                cont3 = 0
            #Para dano de balaenemigo con maximus
            if(flag4):
                cont4 += 1
            if(cont4 >= 8):
                cont4 = 0
            #Para lanzar ratas
            if(flag5):
                cont5 += 1
            if(cont5 >= 50):
                cont5 = 0
            #Para ataque enemigos nivel2
            if(flag6):
                cont6 += 1
            if(cont6 >= 200):
                cont6 = 0
            #Para colision balas enemigos nivel2 con maximus
            if(flag7):
                cont7 += 1
            if(cont7 >= 8):
                cont7 = 0
            #Para colision balas zombie_tipo5 nivel1 con maximus
            if(flag8):
                cont8 += 1
            if(cont8 >= 200):
                cont8 = 0
            if(closep):
                fin=True
                nivel_actual.StopSound()

            if(countdown): #cuenta regresiva, cogio el reloj
                cont_arena -= 1
            if(cont_arena <= 0):
                countdown = False

            if(countdown_zap): #cuenta regresiva, cogio los zapatos
                cont_zap -= 1
            if(cont_zap <= 0 and one_time):
                countdown_zap = False
                one_time = False
                maximus.increment_x -= 5

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
                    pygame.display.set_caption("Place of Dead - Sake of revenge ", 'Spine Runtime')
                    nivel_actual = nivel_lista[nivel_actual_no]
                    nivel_actual.StartSound()
                    maximus.nivel = nivel_actual
                    maximus.setPos([300, ALTO/2])

                    for e in ls_enemigos_nivel2:
                        e.StartMovements()#ejecuta

                    for e in ls_balase:#limpia
                        ls_balase.remove(e)

            #------------Nivel1--------------
            if(nivel_actual_no == 0):
                #ls_todos_nivel1.draw(pantalla)
                for e in ls_balase:
                    if(e.tipo == "rata"):
                        e.restartMovements(maximus.getPos())


                for balae in ls_balase:
                    for bala in ls_balaj:
                        if(checkCollision(bala,balae)): # si se choco
                            if(balae.tipo == "rata"):
                                ls_balaj.remove(bala)
                                ls_todos_nivel1.remove(bala)
                            else:
                                ls_balaj.remove(bala)
                                ls_todos_nivel1.remove(bala)
                                ls_balase.remove(balae)


            #------------Nivel2--------------
            if(nivel_actual_no == 1):
                ls_todos_nivel2.draw(pantalla)
                ls_todos_nivel2.update()

            # Dibujamos y refrescamos
            nivel_actual.draw(pantalla)
            activos_sp_lista.draw(pantalla)

            #Actualizo las balas del boss
            for bil in ls_balasboss:
                bil.update()
            # Actualizamos al jugador
            activos_sp_lista.update()

            ls_balaj.draw(pantalla)
            ls_balase.draw(pantalla)
            ls_balasboss.draw(pantalla)
            ls_balaj.update()
            ls_balase.update()

            # Actualizamos elementos en el nivel
            nivel_actual.update()
            ls_vida_nivel1
            #------------General--------------
            #renderiza objetos de informacion en la pantalla
            pantalla.blit(blood,[5,ALTO - ALTO+15])
            pantalla.blit(point,[5,(ALTO - ALTO+15) + 15]) #+ 15])
            pantalla.blit(reloj2, [5,(ALTO - ALTO+15) + 15*2])
            pantalla.blit(municiones, [5,(ALTO - ALTO+15) + 15*3])
            lifebars(maximus,pantalla,[120,(ALTO - ALTO+15)])
            pygame.display.flip()
            reloj.tick(tasa_cambio)

        #---------------Fin del ciclo-----------------

        if(game_over):
            nivel_actual.StopSound()
            pygame.init()
            tam = [ANCHO, ALTO]
            pantalla = pygame.display.set_mode(tam)

            pygame.display.set_caption("Place of Dead - Game Over ", 'Spine Runtime')
            tipo = pygame.font.SysFont("monospace", 15)
            ad1 = pygame.image.load(curdir+"/enviroment/main/gameover.jpg")
            ad1 = pygame.transform.scale(ad1,tam)
            pantalla.blit(ad1,(0,0))
            pygame.display.flip()
            time.sleep(2)
            print "Perdiste"
        if(winner):
            nivel_actual.StopSound()
            pygame.init()
            tam = [ANCHO, ALTO]
            pantalla = pygame.display.set_mode(tam)

            pygame.display.set_caption("Place of Dead - Game Over ", 'Spine Runtime')
            tipo = pygame.font.SysFont("monospace", 15)
            ad1 = pygame.image.load(curdir+"/enviroment/main/winner.jpg")
            ad1 = pygame.transform.scale(ad1,tam)
            pantalla.blit(ad1,(0,0))
            pygame.display.flip()
            time.sleep(2)
            print "ganaste"

        pygame.mixer.music.play(-1)

class boton_tutorial(buttonz):
    def __init__(self,img,img2):
        buttonz.__init__(self,img,img2)
    def action(self):
        print "boton de tutorial"

class menu(window):
    def __init__(self, parent):
        window.__init__(self,parent)
        self.initUI()
    def save(self,derechas,izquierdas,saltos,disparos):
        derechas = retornarkeyascii(derechas)
        izquierdas = retornarkeyascii(izquierdas)
        saltos = retornarkeyascii(saltos)
        disparos = retornarkeyascii(disparos)
        if(not(derechas == None or izquierdas==None or saltos == None or disparos==None)):
            try:
                Config.set('Movimientos', 'derecha', derechas)
                Config.set('Movimientos', 'izquierda', izquierdas)
                Config.set('Movimientos', 'salto', saltos)
                Config.set('Movimientos', 'disparo', disparos)
                with open('config.ini', 'w') as configfile:
                    Config.write(configfile)
            except:
                print "Error en la escritura"
        else:
            print "error"
    def initUI(self):

        Config.read("config.ini")
        Config.sections()
        derecha = ConfigSectionMap("Movimientos")['derecha']
        izquierda = ConfigSectionMap("Movimientos")['izquierda']
        disparo = ConfigSectionMap("Movimientos")['disparo']
        salto = ConfigSectionMap("Movimientos")['salto']

        derecha=int(derecha)
        izquierda=int(izquierda)
        disparo=int(disparo)
        salto=int(salto)

        self.parent.title("Place of dead - [Configuration]")
        self.style = Style()
        #self.style.theme_use("default")
        self.style.configure('My.TFrame', background='gray')
        #Layouts
        frame1 = Frame(self)
        frame1.pack(fill=Y)
        frame2 = Frame(self)
        frame2.pack(fill=Y)
        frame3 = Frame(self)
        frame3.pack(fill=Y)
        frame4 = Frame(self)
        frame4.pack(fill=Y)
        frame5 = Frame(self)
        frame5.pack(fill=Y)
        frame6 = Frame(self)
        frame6.pack(fill=Y)

        self.pack(fill=BOTH, expand=1)
        self.labela = Label(frame2, text="Movimiento a la derecha: ")#, textvariable=self.var)
        self.labela.pack(side=LEFT)
        derechae = Entry(frame2,width=9)
        derechae.insert(END, str(retornarletra(derecha)))
        derechae.pack(side=LEFT,padx=1, pady=1, expand=True)

        self.labelb = Label(frame3, text="Movimiento a la derecha: ")#, textvariable=self.var)
        self.labelb.pack(side=LEFT)
        izquierdae = Entry(frame3,width=9)
        izquierdae.insert(END, str(retornarletra(izquierda)))
        izquierdae.pack(side=LEFT,padx=1, pady=1, expand=True)

        self.labelc = Label(frame4, text="Salto: ")#, textvariable=self.var)
        self.labelc.pack(side=LEFT)
        saltoe = Entry(frame4,width=9)
        saltoe.insert(END, str(retornarletra(salto)))
        saltoe.pack(side=LEFT,padx=1, pady=1, expand=True)

        self.labeld = Label(frame5, text="Ataque: ")#, textvariable=self.var)
        self.labeld.pack(side=LEFT)
        disparoe = Entry(frame5,width=9)
        disparoe.insert(END, str(retornarletra(disparo)))
        disparoe.pack(side=LEFT,padx=1, pady=1, expand=True)

        okButton = Button(frame6, text="Save", command=lambda: self.save(derechae.get(),izquierdae.get(),saltoe.get(),disparoe.get()))
        okButton.pack(side=RIGHT)

class boton_ajustes(buttonz):
    def __init__(self,img,img2,ventana,backgrounl,DIM,esmenu):
        buttonz.__init__(self,img,img2)
        self.ventana=ventana
        self.backgrounl=backgrounl
        self.ANCHO = DIM[0]
        self.ALTO = DIM [1]
        self.esmenu=esmenu
    def action(self):
        self.clicked=False
        if(self.esmenu):
            self.backgrounl.draw(self.ventana)
            self.ventana = pygame.display.set_mode((2, 2))
        else:
            self.ventana = pygame.display.set_mode((2, 2))
        #pr = self.ventana.subsurface([0,0,100,100]) #Dibuja una surface sobre la pantalla
        #pr.fill((255,255,255))
        pygame.display.flip()
        #inp = str(inputbox.ask(self.ventana, 'Movimiento a la derecha:'))
        #inp = str(inputbox.ask(self.ventana, 'Movimiento a la izquierda:'))
        #print inp
        root = Tk()
        root.geometry("480x350+300+300")
        app = menu(root)
        def on_closing():
            if tkMessageBox.askokcancel("Quit", "Guardaste los cambios antes de salir?"):
                root.destroy()
                self.ventana = pygame.display.set_mode((self.ANCHO, self.ALTO))
                pygame.display.flip()
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()

class boton_acercade(buttonz):
    def __init__(self,img,img2):
        buttonz.__init__(self,img,img2)
    def action(self):
        print "boton de creditos y mas"

class mainsplash(pygame.sprite.Sprite): #Hereda de la clase sprite
    #cargar_fondo('zombie1.png',ancho,alto)
    def __init__(self):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image("o_7ecb0b0ccb0a3aa5-0.jpg", curdir+"/enviroment/main", alpha=False)
        self.carrusel=[]
        self.index=0
    	self.rect = self.image.get_rect()

    def setpos(self):
        self.rect.x=0
        self.rect.y=0

    def setindex(self,value):
        self.index=value
    def getindex(self):
        return self.index
    def load(self):
        for i in range(0,729):
            self.carrusel.append(load_image(("o_7ecb0b0ccb0a3aa5-"+str(i)+".jpg"),curdir+"/enviroment/main", alpha=False))
        self.setindex(len(self.carrusel)-1)

    def update(self):
        if(self.getindex()<=(len(self.carrusel)-1)):
            self.image=self.carrusel[self.index]
            self.index=self.index+1
        else:
            self.index=0

####################################################################################
################################# _____.__         #################################
#################################_/ ____\__| ____  #################################
#################################\   __\|  |/    \ #################################
################################# |  |  |  |   |  \#################################
################################# |__|  |__|___|  /#################################
################################FIN             \/ #################################
####################################################################################
