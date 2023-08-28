import pygame as pg
import sys
from utilities.setting import *
from random import randint
import math

#randint(10, 1024), randint(10, 768), randint(25,100), randint(25,100))
class Game:

    def __init__(self, player):
        self.game_area = pg.display.set_mode((WIN_SIZE))
        self.clock = pg.time.Clock()
        self.player = player()
        self.update_vector = (0,0)
        self.test_rect = [
            pg.Rect(500, 300, 100, 100),
            pg.Rect(500, 250, 50, 50),
            pg.Rect(600, 200, 50, 50),
        ] + [pg.Rect(randint(10, 1024), randint(10, 768), randint(25,100), randint(25,100)) for i in range(10)]
        pg.init()

    def update(self):
        self.player.update(self.update_vector, self.test_rect)
        self.update_vector = (0,0)

    def normalize_mouse_pos(self, mouse_coords):
        mx, my = mouse_coords
        px, py = self.player.pos

        dx = mx-px
        dy = my-py

        if mouse_coords[0] == self.player.pos[0]:
            dx = 1
            dy = mouse_coords[1] - self.player.pos[1]
            return math.atan(dy/dx)
        if mx > px:
            return math.atan(dy/dx)
        elif mx < px:
            return math.atan(dy/dx) + math.pi
    
    def draw(self): 
        self.game_area.fill((255,255,255))
        pg.draw.circle(self.game_area, (0,0,0), self.player.pos, 4, 0)
        for rect in self.test_rect:
            pg.draw.rect(self.game_area, (0,0,0), rect, 1)
        
        mouse_pos = pg.mouse.get_pos()
        theta = self.normalize_mouse_pos(mouse_pos)
        try:
            pg.draw.circle(self.game_area, (0,0,0,0), (self.player.pos[0] + 25*math.cos(theta), self.player.pos[1] + 25*math.sin(theta)), 1) 
        except TypeError:
            print(mouse_pos,self.player.pos,theta)

        pg.display.flip()

    def check_event(self):
        pressed = pg.key.get_pressed()
        speed = 0.25
        if pressed[pg.K_a] and pressed[pg.K_w]:
            self.update_vector = (-speed, -speed)
        elif pressed[pg.K_d] and pressed[pg.K_w]:
            self.update_vector = (speed, -speed)
        elif pressed[pg.K_a] and pressed[pg.K_s]:
            self.update_vector = (-speed, speed)
        elif pressed[pg.K_d] and pressed[pg.K_s]:
            self.update_vector = (speed, speed)
        elif pressed[pg.K_a]:
            self.update_vector = (-speed, 0)
        elif pressed[pg.K_d]:
            self.update_vector = (speed, 0)
        elif pressed[pg.K_s]:
            self.update_vector = (0, speed)
        elif pressed[pg.K_w]:
            self.update_vector = (0, -speed)
        elif pressed[pg.K_SPACE]:
            end_point = pg.mouse.get_pos()
            start_point = self.player.pos


        for e in pg.event.get():
            if e.type == pg.QUIT or (
                e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
        
    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

