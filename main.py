from imports import *

FPS = 60

ANCHO = 800
ALTO = 600
pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie(os.path.join(curdirs+"/environment", "resmain.doc"))
screen = pygame.display.set_mode((ANCHO, ALTO))
movie_screen = pygame.Surface(movie.get_size()).convert()

movie.set_display(movie_screen)
movie.play()


playing = True
repeat=False
while playing:
    if(repeat):
        movie.stop()
        movie.rewind()
        movie.play()
        repeat=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False
    if(not movie.get_busy()):
        repeat=True
    screen.blit(movie_screen,(0,0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
