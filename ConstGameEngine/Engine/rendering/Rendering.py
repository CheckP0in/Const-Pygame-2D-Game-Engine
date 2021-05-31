from numba import jit, njit


# -- Create class -- #
class Rendering:
    # -- Fills the screen with a colour of the users choice -- #
    @staticmethod
    def fill_screen(window, colour: tuple[int, int, int]):
        window.fill(colour)

    @jit(nopython=False)
    def fill_screen_jit(self, window, colour: tuple[int, int, int]):
        window.fill(colour)

    @njit
    def fill_screen_njit(self, window, colour: tuple[int, int, int]):
        window.fill(colour)
