# -- Import dependencies -- #
import pygame
from numba import jit, njit


# -- Create class -- #
class Rect:
    # -- constructor -- #
    def __init__(self, x: int, y: int, width: int, height: int, surface, colour: tuple[int, int, int]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = surface
        self.colour = colour

    # -- draws the rectangle onto the surface -- #
    def draw(self):
        pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

    @jit(nopython=False)
    def draw_jit(self):
        pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

    @njit
    def draw_njit(self):
        pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))
