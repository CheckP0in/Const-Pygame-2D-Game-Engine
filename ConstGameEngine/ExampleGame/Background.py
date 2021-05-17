from ConstGameEngine.Engine.rendering.images.PygameImage import PygameImage


class Background:
    def __init__(self, width, height, path):
        self.width = width
        self.height = height
        self.path = path
        self.image = None

    def init(self):
        self.image = PygameImage(0, 0, self.width, self.height, self.path)
        self.image.init()

    def draw(self, surface):
        self.image.draw_image(surface)
