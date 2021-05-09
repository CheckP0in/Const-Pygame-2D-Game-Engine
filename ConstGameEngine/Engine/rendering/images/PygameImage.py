import os

import pygame


class PygameImage:
    def __init__(self, x, y, width, height, path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = path
        self.image = None

    def init(self):
        parsed_path: list = self.path.split('/')
        self.image = pygame.image.load(os.path.join(parsed_path[0], '/'.join(parsed_path[1:])))

    def draw(self, window: pygame.Surface):
        window.blit(self.image, (self.x, self.y, self.width, self.height))
