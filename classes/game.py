import pygame as pg
import sys
from utilities.setting import *
from random import randint
import math

from . import player
from . import testing

bullets = []
class Game:

    def __init__(self):
        """
        sets game area, clcok and initializes classes
        """
        pg.init()
        self.game_area = pg.display.set_mode((WIN_SIZE))
        pg.mouse.set_cursor(*pg.cursors.broken_x)
        self.clock = pg.time.Clock()
        self.player = player.Player()
        self.update_vector = (0,0)
        self.entities = [] 
        
        # TODO: Protoype functionalities
        self.test_rect = testing.Tester().build_rects()

    def update(self):
        self.player.update_position(update_vector=self.update_vector)
        self.player.collision_detection(self.test_rect)
        self.update_vector = (0,0)

    def build_theta(self, mouse_coords):
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
        theta = self.build_theta(mouse_pos)
        try:
            pg.draw.circle(self.game_area, 
                           (0,0,0,0), 
                           (self.player.pos[0] + 25*math.cos(theta), 
                            self.player.pos[1] + 25*math.sin(theta)), 
                            1) 
        except TypeError:
            print(mouse_pos,self.player.pos,theta)

        for bullet in bullets:
            pl, ta, ix = bullet

            my = ta[1] - pl[1]
            mx = ta[0] - pl[0]
            mr = my/mx

            b = pl[1] - mr * pl[0]

            dx = pl[0] + 4 * ix
            dy = mr * dx + b

            pg.draw.circle(self.game_area, (0,0,0,0), (dx, dy), 2)
            pg.draw.line(self.game_area, (0,0,0), pl, ta)
            
            bullet[-1] += 1
            
            if bullet[-1] >= 75:
                idx = bullets.index(bullet)
                del bullets[idx]
            
        pg.display.flip()

    def check_event(self):
        pressed = pg.key.get_pressed()
        speed = 0.25
        for e in pg.event.get():
            if e.type == pg.QUIT or (
                e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

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
            if len(bullets) == 0:
                bullets.append([(start_point), (end_point), 0])
        
    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

