# -- Create class -- #
class Rendering:
    # -- Fills the screen with a colour of the users choice -- #
    @staticmethod
    def fill_screen(window, colour: tuple[int, int, int]):
        window.fill(colour)
