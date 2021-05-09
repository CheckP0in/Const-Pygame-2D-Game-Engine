from multiprocessing import Process
from threading import Thread
from typing import Callable


class BatchProcessing:
    @staticmethod
    def obtain_process(func: Callable, args: tuple) -> Callable:
        def f(): func(*args)

        return f

    @staticmethod
    def run_process_concurrent(func: Callable):
        thread = Thread(target=func)
        thread.start()

    @staticmethod
    def run_process_ASYNC(func: Callable):
        process = Process(target=func)
        process.start()
