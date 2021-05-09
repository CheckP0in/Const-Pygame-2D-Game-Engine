import pygame
import os
from ConstGameEngine.Engine.Window import Window
from ConstGameEngine.Engine.rendering.Colour import Colour
from ConstGameEngine.Engine.rendering.Rendering import Rendering
from ConstGameEngine.Engine.rendering.images.PygameImage import PygameImage
from ConstGameEngine.Engine.data_management.BatchProcessing import BatchProcessing

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
ICON = pygame.image.load(os.path.join('Assets', 'icon.png'))

white = (255, 255, 255)
background_colour = Colour(white)

SPACESHIP_WIDTH = SPACESHIP_HEIGHT = 64
SPACESHIP_X, SPACESHIP_Y = (WIDTH // 2) - (SPACESHIP_WIDTH // 2), (HEIGHT // 2) - (SPACESHIP_HEIGHT // 2)

pygame_spaceship_image = PygameImage(SPACESHIP_X, SPACESHIP_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT,
                                     "Assets/spaceship.png")

pygame_spaceship_image.init()

window = Window.instance()
window.set_size((WIDTH, HEIGHT))
window.set_title("Space Invaders!")
window.set_icon(ICON)
window.init()


def run():
    clock = pygame.time.Clock()

    render_background = True
    render_spaceship = True

    render_background_process = BatchProcessing.obtain_process(Rendering.fill_screen,
                                                               (window.get_window(), background_colour.get_RGB()))

    render_spaceship_process = BatchProcessing.obtain_process(pygame_spaceship_image.draw, (window.get_window(),))

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if render_background:
            render_background_process()
            render_background = False
            print("Rendered Background!")

        if render_spaceship:
            render_spaceship_process()
            render_spaceship = False
            print("Rendered Spaceship!")

        pygame.display.update()

    pygame.quit()
    exit()


if __name__ == '__main__':
    run()
