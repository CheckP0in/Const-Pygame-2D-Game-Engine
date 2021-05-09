from typing import Callable


class BatchProcessing:
    @staticmethod
    def obtain_process(func: Callable, args: tuple) -> Callable:
        def f(): func(*args)
        return f
