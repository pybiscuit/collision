import pygame as pg
from random import randint

class Tester:

    def __init__(self):
        self.id = "Testing apparatus"

    def build_rects(self):
       return [
            pg.Rect(500, 300, 100, 100),
            pg.Rect(500, 250, 50, 50),
            pg.Rect(600, 200, 50, 50),
        ] + [pg.Rect(randint(10, 1024), 
                    randint(10, 768), 
                    randint(25,100), 
                    randint(25,100)) for i in range(10)]