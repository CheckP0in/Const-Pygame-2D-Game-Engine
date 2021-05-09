# -- Import needed dependencies -- #
import pygame
import os
from ConstGameEngine.Engine.Window import Window
from ConstGameEngine.Engine.rendering.Colour import Colour
from ConstGameEngine.Engine.rendering.Rendering import Rendering
from ConstGameEngine.Engine.rendering.images.PygameImage import PygameImage
from ConstGameEngine.Engine.data_management.BatchProcessing import BatchProcessing

# -- Initialize pygame -- #
pygame.init()

# -- Set constants -- #
WIDTH, HEIGHT = 800, 600
FPS = 60
ICON = pygame.image.load(os.path.join('Assets', 'icon.png'))

WHITE = (255, 255, 255)
BACKGROUND_COLOUR = Colour(WHITE)

SPACESHIP_WIDTH = SPACESHIP_HEIGHT = 64
SPACESHIP_X, SPACESHIP_Y = (WIDTH // 2) - (SPACESHIP_WIDTH // 2), (HEIGHT // 2) - (SPACESHIP_HEIGHT // 2)

# -- Get the spaceship image -- #
pygame_spaceship_image = PygameImage(SPACESHIP_X, SPACESHIP_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT,
                                     "Assets/spaceship.png")

# -- Initialize the spaceship image -- #
pygame_spaceship_image.init()

# -- Create and initialize the window -- #
window = Window.instance()
window.set_size((WIDTH, HEIGHT))
window.set_title("Space Invaders!")
window.set_icon(ICON)
window.init()


# -- Run the main game loop -- #
def run():
    # -- Create a pygame clock object -- #
    clock = pygame.time.Clock()

    render_background = True
    render_spaceship = True

    # -- Create a process for rendering the background -- #
    render_background_process = BatchProcessing.obtain_process(Rendering.fill_screen,
                                                               (window.get_window(), BACKGROUND_COLOUR.get_RGB()))

    # -- Create a process for rendering the spaceship -- #
    render_spaceship_process = BatchProcessing.obtain_process(pygame_spaceship_image.draw, (window.get_window(),))

    # -- Run the main game loop -- #
    running = True
    while running:
        # -- Set the FPS to the constant variable 'FPS' -- #
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # -- Render background if needed -- #
        if render_background:
            render_background_process()
            render_background = False
            print("Rendered Background!")

        # -- Render spaceship if needed -- #
        if render_spaceship:
            render_spaceship_process()
            render_spaceship = False
            print("Rendered Spaceship!")

        # -- Update display
        pygame.display.update()

    # -- Exit program when main loop finishes
    pygame.quit()
    exit()


# -- Run program -- #
if __name__ == '__main__':
    run()
