import pygame


class PygameInput:
    @staticmethod
    def get_focused():
        return pygame.key.get_focused()

    @staticmethod
    def get_pressed():
        return pygame.key.get_pressed()

    @staticmethod
    def get_key_pressed(key, pressed):
        return pressed[key]
