import pygame as pg
import random
import sys

from graph import Graph
from pacman import Pacman
from settings import Settings as S
from ghost import Ghost
from graph_search import *

class Game:

    def __init__(self):
        '''Game constructor'''

        pg.init()

        self.clock = pg.time.Clock()
        self.graph = Graph(self)
        self.screen = pg.display.set_mode((self.graph.width * S.tile_size, self.graph.height * S.tile_size))

        self.pacman = Pacman(self)
        self.blinky = Ghost('redghost', Best_First_Search(), self)
        self.pinky = Ghost('pinkghost', Breadth_First_Search(), self)
        self.inky = Ghost('redghost', Depth_Limited_Search(), self)
        self.clyde = Ghost('redghost', A_Star_Search(), self)

    def play(self):
        '''Play the game'''

        while True:

            self.dt = self.clock.tick(60) / 1000 if not pg.key.get_pressed()[pg.K_SPACE] else 0

            for event in pg.event.get():
                
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))

            self.graph.update()
            self.pacman.update()
            self.blinky.update()
            self.pinky.update()
            self.inky.update()
            self.clyde.update()

            pg.display.update()


if __name__ == '__main__':
    print()

    g = Game()
    g.play()