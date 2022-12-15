from functools import wraps
import tracemalloc
import time

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def measure_memory(func):
    @wraps(func)
    def memory_wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        print(f"\n\033[37mFunction Name       :\033[35;1m {func.__name__}\033[0m")
        print(f"\033[37mCurrent memory usage:\033[36m {current / 10**6}MB\033[0m")
        print(f"\033[37mPeak                :\033[36m {peak / 10**6}MB\033[0m")
        tracemalloc.stop()
        return result
    return memory_wrapper