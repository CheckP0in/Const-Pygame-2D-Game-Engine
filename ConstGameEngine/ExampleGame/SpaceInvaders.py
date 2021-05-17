import pygame
from ConstGameEngine.Engine.rendering.images.Icon import Icon
from ConstGameEngine.Engine.Window import Window
from ConstGameEngine.Engine.data_management.BatchProcessing import BatchProcessing
from ConstGameEngine.ExampleGame.Background import Background


class SpaceInvaders:
    def __init__(self):
        self.FPS = 60
        self.window_width, self.window_height = 800, 600
        self.window_caption = 'Space Invaders: example game for Const Pygame 2D Game Engine!'
        self.icon_width = self.icon_height = 32
        self.icon_path = 'Assets/icon.png'
        self.icon = self.get_icon()
        self.window = self.create_window()
        self.background_image = Background(self.window_width, self.window_height, 'Assets/background.jpg')
        self.background_image.init()
        self.render_background_process = BatchProcessing.obtain_process(self.background_image.draw, (self.window,))
        self.to_render_background = True

    def create_window(self):
        instance = Window.instance()
        instance.set_size((self.window_width, self.window_height))
        instance.set_title(self.window_caption)
        instance.set_icon(self.icon)
        instance.init()

        return instance.get_window()

    def get_icon(self):
        return Icon(self.icon_width, self.icon_height, self.icon_path).image

    def run(self):
        clock = pygame.time.Clock()

        running = True
        while running:
            clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.to_render_background:
                self.render_background_process()
                self.to_render_background = False

            pygame.display.update()

        pygame.quit()
        exit()


if __name__ == '__main__':
    game = SpaceInvaders()
    game.run()
