from imports import *

def main():
    ANCHO = 800
    ALTO = 600
    pygame.init()
    menu_d = pygame.display.set_mode((ANCHO, ALTO))#, pygame.FULLSCREEN)
    backgroundm = mainsplash()
    backgroundm.rect.x=0
    backgroundm.rect.y=0
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

        ls.draw(menu_d)
        pygame.display.flip()
        ls.update()
        reloj.tick(30)
    pygame.display.flip()
    terminar = False

if __name__ == "__main__":
    main()
