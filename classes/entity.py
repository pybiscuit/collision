from math import atan, degrees, radians, pi

import pygame as pg
from utilities.setting import *

class Entity:
    """
    base class for game entities player and enemy.
    """

    def __init__(self):
        self.health = 0
        self.max_health = 0
        # self.pos = [0,0]
        # self._cache = []
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

    def collision_detections(collision_objects):
        pass