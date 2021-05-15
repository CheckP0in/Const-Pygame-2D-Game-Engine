# -- import dependencies -- #
from ConstGameEngine.Engine.rendering.images.BaseImage import BaseImage


# -- Create class
class PygameImage(BaseImage):
    # -- Constructor -- #
    def __init__(self, x, y, width, height, path):
        super().__init__(width, height, path, x=x, y=y)
