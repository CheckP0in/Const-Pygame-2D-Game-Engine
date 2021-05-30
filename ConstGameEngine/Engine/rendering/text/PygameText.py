# -- Import dependencies -- #
import pygame
from numba import jit, njit


# -- Create class
class PygameText:
    # -- Initialize a system font -- #
    @staticmethod
    def init_sys_font(font_name='New Times Roman', font_size=28, bold=False, italic=False):
        return pygame.font.SysFont(font_name, font_size, bold=bold, italic=italic)

    @jit(nopython=False)
    def init_sys_font_jit(self, font_name='New Times Roman', font_size=28, bold=False, italic=False):
        return pygame.font.SysFont(font_name, font_size, bold=bold, italic=italic)

    @jit
    def init_sys_font_njit(self, font_name='New Times Roman', font_size=28, bold=False, italic=False):
        return pygame.font.SysFont(font_name, font_size, bold=bold, italic=italic)

    # -- Initialize a custom font -- #
    @staticmethod
    def init_custom_font(path=None, font_size=28):
        return pygame.font.Font(path, font_size)

    @jit(nopython=False)
    def init_custom_font_jit(self, path=None, font_size=28):
        return pygame.font.Font(path, font_size)

    @njit
    def init_custom_font_njit(self, path=None, font_size=28):
        return pygame.font.Font(path, font_size)

    # -- Gets all available system fonts -- #
    @staticmethod
    def get_sys_fonts():
        return pygame.font.get_fonts()

    @jit(nopython=False)
    def get_sys_fonts_jit(self):
        return pygame.font.get_fonts()

    @njit
    def get_sys_fonts_njit(self):
        return pygame.font.get_fonts()

    # -- Render a font -- #
    @staticmethod
    def render_font(text, font, colour, antialias=True):
        return font.render(text, antialias=antialias, colour=colour)

    @jit(nopython=False)
    def render_font_jit(self, text, font, colour, antialias=True):
        return font.render(text, antialias=antialias, colour=colour)

    @njit
    def render_font_njit(self, text, font, colour, antialias=True):
        return font.render(text, antialias=antialias, colour=colour)

    # -- Renders text to the screen -- #
    @staticmethod
    def draw_text(surface, rendered_font, x, y):
        surface.blit(rendered_font, (x, y))

    @jit(nopython=False)
    def draw_text_jit(self, surface, rendered_font, x, y):
        surface.blit(rendered_font, (x, y))

    @njit
    def draw_text_njit(self, surface, rendered_font, x, y):
        surface.blit(rendered_font, (x, y))
