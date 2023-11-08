from time import time


class Timer:
    def __init__(self):
        self.start_time = time()
        self.end_time = time()

    def end(self, verbose: bool = False):
        self.end_time = time()
        used_time = self.end_time - self.start_time
        if verbose:
            print(f"Used time: {used_time:.3f}s")
        return used_time

    @classmethod
    def start(cls):
        return cls()
