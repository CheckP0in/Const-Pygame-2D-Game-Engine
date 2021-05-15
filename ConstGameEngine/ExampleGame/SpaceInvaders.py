import pygame


class SpaceInvaders:
    def __init__(self):
        self.FPS = 60

    def run(self):
        clock = pygame.time.Clock()

        running = True
        while running:
            clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

        pygame.quit()
        exit()


if __name__ == '__main__':
    game = SpaceInvaders()
    game.run()
