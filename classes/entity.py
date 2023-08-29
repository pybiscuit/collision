from math import atan, degrees, radians, pi

import pygame as pg
from utilities.setting import *

class Entity(pg.sprite.Sprite):
    """
    base class for game entities player and enemy.
    """

    def __init__(self):
        self.health = 0
        self.max_health = 0
        self.vector = pg.math.Vector2(0,0)
        self.hitbox_rad = 2

    def cache_pos(self):
        self._cache = list(self.pos)

    def update_position(self, update_vector):
        self.cache_pos()
        
        x_min = self.pos[0] > 10
        y_min = self.pos[1] > 10
        x_max = self.pos[0] < 1014
        y_max = self.pos[1] < 758

        # Window boundaries
        if all([x_min, y_min, x_max, y_max]):
            self.pos[0] += update_vector[0]
            self.pos[1] += update_vector[1]
        elif not x_min:
            self.pos[0] = 11
        elif not y_min:
            self.pos[1] = 11
        elif not x_max:
            self.pos[0] = 1013
        elif not y_max:
            self.pos[1] = 757

    def collision_detection(self, collision_objects):
        self.cache_pos()
        for obj in collision_objects:
            print(self.pos, (obj.left, obj.top))
            # inside = False
            # if not inside:
            #     top_line = all([
            #         self.pos[1] >= obj.top,
            #         self.pos[1] <= obj.top+obj.height,
            #         self.pos[0] >= obj.left,
            #         self.pos[0] <= obj.left+obj.width
            #     ])
            # if top_line:
            #     self.pos[0], self.pos[1] = self._cache
            
            # if self.pos[0] <= obj.left + 4:
            #     self.pos[0] += 1
            # elif self.pos[0] >= obj.left + 96:
            #     self.pos[0] -= 1
            # elif self.pos[1] <= obj.top + 4:
            #     self.pos[1] += 1
            # elif self.pos[1] >= obj.top + 96:
            #     self.pos[1] -= 1