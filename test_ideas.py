# FIle for experimentation

from functools import wraps
from time import perf_counter, sleep

def get_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()

        func(*args, **kwargs)

        end_time = perf_counter()
        total_time = round(end_time-start_time, 2)

        print("Time:", total_time, "seconds")

    return wrapper

@get_time
def do_something(param: str):
    sleep(1)
    print(param)



if __name__ == "__main__":
    do_something('Hello')
