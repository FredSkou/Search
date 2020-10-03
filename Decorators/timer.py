import time
import Decorators.Write_Log
def timer_decorator(func):
    def timeit(*args):
        start = time.time()
        #print("Starting Timer For Function:")
        value = func(*args)
        end = (time.time()) - start
        print(f"It took: {round(end,1)} seconds")
        Decorators.Write_Log.saveResults(end,"Logs/Time.txt")
        return value
    return timeit