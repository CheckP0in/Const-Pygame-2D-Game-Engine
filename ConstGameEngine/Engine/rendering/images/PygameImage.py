# -- import dependencies -- #
import os
import pygame


# -- Create class
class PygameImage:
    # -- Constructor -- #
    def __init__(self, x, y, width, height, path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = path
        self.image = None

    # -- Initialize the image -- #
    def init(self):
        parsed_path: list = self.path.split('/')
        self.image = pygame.image.load(os.path.join(parsed_path[0], '/'.join(parsed_path[1:])))

    # -- Draw the image -- #
    def draw(self, window: pygame.Surface):
        window.blit(self.image, (self.x, self.y, self.width, self.height))
