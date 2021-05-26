import pygame
from ConstGameEngine.Engine.ecs.Entities.EntityManager import EntityManager


class ECSMainApplication:
    def __init__(self, window, fps=60, entity_manager=None, run_systems_concurrent=False, run_systems_parallel=False,
                 join_systems_concurrent=False, join_systems_parallel=False, concurrent_systems_daemon=False,
                 parallel_systems_daemon=False):
        self.window = window
        self.fps = fps
        self.run_systems_concurrent = run_systems_concurrent
        self.run_systems_parallel = run_systems_parallel
        self.join_systems_concurrent = join_systems_concurrent
        self.join_systems_parallel = join_systems_parallel
        self.concurrent_systems_daemon = concurrent_systems_daemon
        self.parallel_systems_daemon = parallel_systems_daemon

        if entity_manager is None:
            self.entity_manager = EntityManager()

        else:
            self.entity_manager = entity_manager

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for entity in self.entity_manager.get_entities():
                if self.run_systems_concurrent:
                    entity.run_concurrent(join=self.join_systems_concurrent, daemon=self.concurrent_systems_daemon)

                elif self.run_systems_parallel:
                    entity.run_parallel(join=self.join_systems_parallel, daemon=self.parallel_systems_daemon)

                else:
                    entity.run()

        pygame.quit()
        exit()
