import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500,500))
screen.fill(color='grey')

#code
circle(screen,(255,255,0),(250,250),120)
circle(screen, (50,50,50),(250,250),120,2)

circle(screen,(255,0,0),(200,230),25)
circle(screen,(50,50,50),(200,230),25,2)
circle(screen,(0,0,0),(200,230),10)

circle(screen,(255,0,0),(300,230),20)
circle(screen,(50,50,50),(300,230),20,2)
circle(screen,(0,0,0),(300,230),8)

line(screen, (0,0,0), (232.5,217), (147.5,166),20)
line(screen,(0,0,0),(275,217.5),(360,175),15)

rect(screen, (0, 0, 0), (200, 310, 100, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()