import time


def ExecutionTime(func) -> any:
    def Execute(*args, **kwargs):
        start = time.time()
        var = func(*args, **kwargs)
        print(f"Execution time ({func.__name__}): {round(time.time()-start, 10)} seconds")
        return var
    return Execute
