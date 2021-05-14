# -- Import dependencies -- #
import pygame
from ConstGameEngine.Engine.rendering.images.PygameImage import PygameImage


# -- Create class
class PygameText:
    # -- Initialize a system font -- #
    @staticmethod
    def init_sys_font(font_name='New Times Roman', font_size=28, bold=False, italic=False):
        return pygame.font.SysFont(font_name, font_size, bold=bold, italic=italic)

    # -- Initialize a custom font -- #
    @staticmethod
    def init_custom_font(path=None, font_size=28):
        return pygame.font.Font(path, font_size)

    # -- Gets all available system fonts -- #
    @staticmethod
    def get_sys_fonts():
        return pygame.font.get_fonts()

    # -- Render a font -- #
    @staticmethod
    def render_font(text, font, colour, antialias=True):
        return font.render(text, antialias=antialias, colour=colour)
