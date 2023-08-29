import pygame as pg
from classes.entity import Entity

class Player(Entity):

    def __init__(self):
        super().__init__()
        self.pos = [100, 100]
        self._cache = (100, 100)
        self.id = "player"

    # def cache_pos(self):
    #     self._cache = tuple(self.pos)

    # def update(self, vector, collision_objects):
    #     self.cache_pos()
        # x_min = self.pos[0] > 10
        # y_min = self.pos[1] > 10
        # x_max = self.pos[0] < 1014
        # y_max = self.pos[1] < 758

        # # Window boundaries
        # if all([x_min, y_min, x_max, y_max]):
        #     self.pos[0] += vector[0]
        #     self.pos[1] += vector[1]
        # elif not x_min:
        #     self.pos[0] = 11
        # elif not y_min:
        #     self.pos[1] = 11
        # elif not x_max:
        #     self.pos[0] = 1013
        # elif not y_max:
        #     self.pos[1] = 757
        
        # object collision is off. shapes do not match Rects.
        # for obj in collision_objects:
        #     inside = False
        #     if not inside:
        #         top_line = all([
        #             self.pos[1] >= obj.top,
        #             self.pos[1] <= obj.top+obj.height,
        #             self.pos[0] >= obj.left,
        #             self.pos[0] <= obj.left+obj.width
        #         ])
        #     if top_line:
        #         self.pos[0], self.pos[1] = self._cache
            
        #     if self.pos[0] <= obj.left + 4:
        #         self.pos[0] += 1
        #     elif self.pos[0] >= obj.left + 96:
        #         self.pos[0] -= 1
        #     elif self.pos[1] <= obj.top + 4:
        #         self.pos[1] += 1
        #     elif self.pos[1] >= obj.top + 96:
        #         self.pos[1] -= 1

