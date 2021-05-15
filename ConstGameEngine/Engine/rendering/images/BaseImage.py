import os
import pygame


class BaseImage:
    # -- Constructor -- #
    def __init__(self, width, height, path, x=None, y=None):
        self.width = width
        self.height = height
        self.path = path
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0
        self.image = None

    # -- Initialize the image -- #
    def init(self):
        parsed_path: list = self.path.split('/')
        self.image = pygame.image.load(os.path.join(parsed_path[0], '/'.join(parsed_path[1:])))

    # -- Draw the image -- #
    def draw_image(self, window: pygame.Surface):
        window.blit(self.image, (self.x, self.y, self.width, self.height))

    # -- Rotate an image -- #
    @staticmethod
    def rotate_image(surface, angle):
        return pygame.transform.rotate(surface, angle)

    # -- Scale an image -- #
    @staticmethod
    def scale_image(surface, width, height):
        return pygame.transform.scale(surface, (width, height))
