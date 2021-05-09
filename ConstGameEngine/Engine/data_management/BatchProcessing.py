# -- Import dependencies -- #
from multiprocessing import Process
from threading import Thread
from typing import Callable


# -- Create class -- #
class BatchProcessing:
    # -- Used for making a fast way to create a process that can be ran by the user -- #
    @staticmethod
    def obtain_process(func: Callable, args: tuple) -> Callable:
        def f(): func(*args)

        return f

    # -- Used for running a process concurrently -- #
    @staticmethod
    def run_process_concurrent(func: Callable):
        thread = Thread(target=func)
        thread.start()

    # -- Used for running a process in parallel with the rest of the program -- #
    @staticmethod
    def run_process_ASYNC(func: Callable):
        process = Process(target=func)
        process.start()
