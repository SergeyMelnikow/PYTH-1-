import math
from random import choice, randrange

import pygame as pg


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pg.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.collisions = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x+self.r > 800 or self.x-self.r < 0:
            self.vx = -self.vx
            self.collisions += 1
        if self.y+self.r > 600 or self.y-self.r < 0:
            self.vy = -self.vy
            self.collisions += 1
        else:
            self.vy -= 2
        self.x += self.vx
        self.y -= self.vy


    def vanishing(self):

        if self.collisions == 10:
            self.r = 0

    '''Функция уничтожает снаряд при
            self.collisions = 10'''


    def draw(self):
        pg.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
    '''Функция рисует снаряд на экране'''

    def hittest(self, obj):

        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            ob: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x-self.x)**2+(obj.y-self.y)**2 < (obj.r+self.r)**2 and obj.r > 0 and self.r > 0:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        if (event.pos[0]-new_ball.x) != 0:
            self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        else:
            self.an = 1.57
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event and (event.pos[0]-20) != 0:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        else:
            self.an = 1.57
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):

        pg.draw.line(self.screen, self.color, (40,450), (40+math.cos(self.an)*50,450+math.sin(self.an)*50),5)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.x = randrange(600, 780)
        self.y = randrange(300, 550)
        self.r = randrange(10, 20)
        self.vx = randrange(-5, 5)
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.attempts = 0

    def hit(self):
        self.r = 0

    def counter(self):
        self.attempts += 1

    def draw(self):
        pg.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def move(self):
        if self.x+self.r > 800 or self.x-self.r < 0:
            self.vx = -self.vx
        if self.y+self.r > 600 or self.y-self.r < 0:
            self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
target1 = Target(screen)
target2 = Target(screen)
targets = [target1, target2]

clock = pg.time.Clock()
gun = Gun(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for b in balls:
        b.vanishing()
        b.draw()
    for t in targets:
        t.draw()
        t.move()
    pg.display.update()

    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pg.MOUSEBUTTONUP:
            gun.fire2_end(event)
            t.counter()
        elif event.type == pg.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        for t in targets:
            if b.hittest(t):
                t.hit()
                targets.append(Target(screen))
                print('Цель уничтожена, попыток:', t.attempts)

    gun.power_up()

pg.quit()
