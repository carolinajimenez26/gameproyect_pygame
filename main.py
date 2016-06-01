from imports import *

def main():
    ANCHO = 800
    ALTO = 600
    pygame.init()
    menu_d = pygame.display.set_mode((ANCHO, ALTO))#, pygame.FULLSCREEN)
    btn1 = buttonz("btn1.png","btn1_p.png")
    rex,rey = btn1.getrect()
    btn1.setpos([ANCHO/2-rex/2,ALTO/2-rey])
    lsbtn = pygame.sprite.Group()
    lsbtn.add(btn1)
    backgroundm = mainsplash()
    backgroundm.setpos()
    backgroundm.load()
    ls = pygame.sprite.Group()
    ls.add(backgroundm)
    pygame.display.flip()
    reloj=pygame.time.Clock()
    terminar=False

    while(not terminar):
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
        reloj.tick(30)
    pygame.display.flip()
    terminar = False

if __name__ == "__main__":
    main()
