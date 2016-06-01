from imports import *

def main():
    ANCHO = 800
    ALTO = 600
    pygame.init()
    menu_d = pygame.display.set_mode((0, 0))#, pygame.FULLSCREEN)
    #Seccion de botones
    btn1 = boton_inicio("btn1.png","btn1_p.png")
    btn2 = boton_ajustes("btn2.png","btn2_p.png")
    btn3 = boton_acercade("btn3.png","btn3_p.png")
    rex,rey = btn1.getrect()
    btn1.setpos([ANCHO/2-rex/2,ALTO/2-rey-50])
    btn2.setpos([ANCHO/2-rex/2,ALTO/2-rey+100])
    btn3.setpos([ANCHO/2-rex/2,ALTO/2-rey+250])
    lsbtn = pygame.sprite.Group()
    lsbtn.add(btn1)
    lsbtn.add(btn2)
    lsbtn.add(btn3)
    #Fin seccion de botones
    #seccion del background con su inicializacion
    sl = splashload()
    backgroundm = mainsplash()
    backgroundm.setpos()
    backgroundm.load()
    sl.setcorrer()
    pygame.display.set_caption("Place of dead - [Menu Principal] ", 'Spine Runtime')
    menu_d = pygame.display.set_mode((ANCHO, ALTO))
    ls = pygame.sprite.Group()
    ls.add(backgroundm)
    #Fin seccion del background
    #Carga del sonido
    pygame.mixer.music.load(os.path.join(curdir+"/enviroment/main", 'background.ogg'))
    pygame.mixer.music.play(-1)
    #Fin carga del sonido
    pygame.display.flip() #Refresco la pantalla
    reloj=pygame.time.Clock()
    terminar=False
    repeat=False
    while(not terminar):
        if(repeat):
            s_fondo.play()
            repeat=False
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                terminar=True
            if event.type == pygame.MOUSEBUTTONUP:
                for btn in lsbtn:
                    btn.setclicked()

        ls.draw(menu_d)
        lsbtn.draw(menu_d)
        pygame.display.flip()
        ls.update()
        lsbtn.update()
        reloj.tick(30) #Tiempo del ciclo, tambien de la secuencia del carrusel en el background
    pygame.display.flip()
    terminar = False

if __name__ == "__main__":
    main()
