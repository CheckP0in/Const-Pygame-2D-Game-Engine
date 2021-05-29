# -- Import dependencies -- #
from multiprocessing import Process
from threading import Thread
from typing import Callable
from numba import jit, njit


# -- Create class -- #
class BatchProcessing:
    # -- Used for making a fast way to create a process that can be ran by the user -- #
    @staticmethod
    def obtain_process(func: Callable, args: tuple) -> Callable:
        def f(): func(*args)

        return f

    @jit(nopython=False)
    def obtain_process_jit(self, func: Callable, args: tuple) -> Callable:
        def f(): func(*args)

        return f

    @njit
    def obtain_process_njit(self, func: Callable, args: tuple) -> Callable:
        def f(): func(*args)

        return f

    # -- Used for running a process concurrently -- #
    @staticmethod
    def run_process_concurrent(func: Callable):
        thread = Thread(target=func)
        thread.start()

    @jit(nopython=False)
    def run_process_concurrent_jit(self, func: Callable):
        thread = Thread(target=func)
        thread.start()

    @njit
    def run_process_concurrent_njit(self, func: Callable):
        thread = Thread(target=func)
        thread.start()

    # -- Used for running a process in parallel with the rest of the program -- #
    @staticmethod
    def run_process_ASYNC(func: Callable):
        process = Process(target=func)
        process.start()

    @jit(nopython=False)
    def run_process_ASYNC_jit(self, func: Callable):
        process = Process(target=func)
        process.start()

    @njit
    def run_process_ASYNC_njit(self, func: Callable):
        process = Process(target=func)
        process.start()
