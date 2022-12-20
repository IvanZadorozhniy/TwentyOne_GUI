# -.- coding: utf8 -.-
import pygame
from main import *
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen.fill((120, 244, 150)) # TODO add a picture of the game table

running = True
game = Game(screen)
game.start()
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #  левая кнопка мыши
                game.checkClick(event.pos)
    
    screen.fill((120, 244, 150))
    game.checkScore()
    game.draw()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()





