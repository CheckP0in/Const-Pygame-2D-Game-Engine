import pygame
from numba import jit, njit


class PygameInput:
    @staticmethod
    def get_focused():
        return pygame.key.get_focused()

    @jit(nopython=False)
    def get_focused_jit(self):
        return pygame.key.get_focused()

    @njit
    def get_focused_njit(self):
        return pygame.key.get_focused()

    @staticmethod
    def get_pressed():
        return pygame.key.get_pressed()

    @jit(nopython=False)
    def get_pressed_jit(self):
        return pygame.key.get_pressed()

    @njit
    def get_pressed_njit(self):
        return pygame.key.get_pressed()

    @staticmethod
    def get_key_pressed(key, pressed):
        return pressed[key]

    @jit(nopython=False)
    def get_key_pressed_jit(self, key, pressed):
        return pressed[key]

    @njit
    def get_key_pressed_njit(self, key, pressed):
        return pressed[key]
