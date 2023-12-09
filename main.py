import pygame
from pygame.colordict import THECOLORS
from pygame.locals import *
from life import Field

import random

SCREEN_WIDTH = 800 # ширина окна
SCREEN_HEIGHT = 600 # высота окна
FIELD_WIDTH = 160 # ширина поля кратна ширине окна
FIELD_HEIGHT = 120 # высота поля кратна высоте окна
FPS = 10 # количество смен поколений в секунду
WHITE = THECOLORS['white']
GRAY = THECOLORS['gray']
BLACK = THECOLORS['black']


class GraphGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.field = Field(FIELD_WIDTH, FIELD_HEIGHT, randomize=True)
        self.cell_size = min(SCREEN_WIDTH // FIELD_WIDTH, SCREEN_HEIGHT // FIELD_HEIGHT)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return

            self.field.next_generation()

            self.screen.fill(WHITE)

            for row in range(FIELD_HEIGHT):
                for col in range(FIELD_WIDTH):
                    cell = self.field.field[row][col]
                    color = BLACK if cell.is_alive else GRAY
                    pygame.draw.rect(self.screen, color,
                                     (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = GraphGame()
    game.run()
