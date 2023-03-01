from functools import wraps
import time

def get_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print("Time Taken:", round(duration, 2))
        
    return wrapper