import time

def timer_decorator(func):
    def timeit(*args):
        start = time.time()
        #print("Starting Timer For Function:")
        value = func(*args)
        end = (time.time()) - start
        print(f"It took: {end} seconds")
        return value
    return timeit