import pygame
from pygame.draw import *
from random import randint, random
pygame.init()

FPS = 60
screen = pygame.display.set_mode((500, 500))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

print('Введите число шариков')
N = int(input())


def new_balls():
    global x, y, r, Vx, Vy, color
    x = []
    y = []
    r = []
    Vx = []
    Vy = []
    color = []
    for i in range(N):
        x.append(randint(50, 450))
        y.append(randint(50, 450))
        r.append(randint(10, 50))
        Vx.append(random())
        Vy.append(random())
        color.append(COLORS[randint(0, 5)])
        circle(screen, color[i], (x[i], y[i]), r[i])


'''Начальное состояние системы шариков
x,y-координаты центра шарика
r-радиус
Vx,Vy-компоненты скоростей'''


def balls_evolution():
    global k
    for i in range(N):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - x[i]) ** 2 + (event.pos[1] - y[i]) ** 2 < r[i] ** 2:
                x[i] = randint(50, 450)
                y[i] = randint(50, 450)
                r[i] = randint(10, 50)
                Vx[i] = random()
                Vy[i] = random()
                color[i] = COLORS[randint(0, 5)]
                circle(screen, color[i], (x[i], y[i]), r[i])
                k += 1
                print('Rating:', k)
        if x[i]-r[i] <= 0 or x[i]+r[i] >= 500:
            Vx[i]=-Vx[i]
        if y[i]-r[i] <= 0 or y[i]+r[i] >= 500:
            Vy[i]=-Vy[i]
        x[i] += Vx[i]
        y[i] += Vy[i]
        circle(screen, color[i], (x[i], y[i]), r[i])


'''Функция задаёт эволюцию системы шариков'''


print('Введите число квадратов')
NS = int(input())

def new_squares():
    global xS, yS, a, VyS, colorS
    xS = []
    yS = []
    a = []
    VyS = []
    colorS = []
    for i in range(NS):
        xS.append(randint(50, 450))
        yS.append(randint(50, 450))
        a.append(randint(10, 50))
        VyS.append(random())
        colorS.append(COLORS[randint(0, 5)])
        rect(screen, colorS[i], (xS[i], yS[i], a[i], a[i]))


'''Начальное состояние системы квадратов
xS,yS-координаты левого верхнего угла
a-стороны
VyS-скорость вдоль оси y'''


def squares_evolution():
    global k
    for i in range(NS):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0 < (event.pos[0] - xS[i]) < a[i] and 0 < (event.pos[1] - yS[i]) < a[i]:
                xS[i] = randint(50, 450)
                yS[i] = randint(50, 450)
                a[i] = randint(10, 50)
                VyS[i] = random()
                colorS[i] = COLORS[randint(0, 5)]
                rect(screen, colorS[i], (xS[i], yS[i], a[i], a[i]))
                k += 0.5
                print('Rating:', k)
        if yS[i] <= 0 or yS[i]+a[i] >= 500:
            VyS[i] = -VyS[i]
        yS[i] += VyS[i]
        rect(screen, colorS[i], (xS[i], yS[i], a[i], a[i]))


'''Функция задаёт эволюцию системы квадратов'''


new_squares()
new_balls()
pygame.display.update()
clock = pygame.time.Clock()
k = 0
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.fill(BLACK)
    balls_evolution()
    squares_evolution()
    pygame.display.update()

pygame.quit()