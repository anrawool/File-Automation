# File for experimentation
import os
import time
from search import *

def search_using_os_walk(target_file):
    found_files = []
    for root, dirs, files in os.walk('/Users/abhijitrawool/'):
        if target_file in files:
            found_files.append(os.path.join(root, target_file))
    return found_files

# Replace 'YourCodeSearchFunction' with the name of your search function.
def search_using_your_code(target_file):
    instance = FileSearch('TEST_TIMER', target_file)
    results = instance.search()
    return results

target_file = "Test_time.jpg"
print("Started")
start_time = time.time()
print("Your code")
result_your_code = search_using_your_code(target_file)
print(result_your_code)
end_time = time.time()
print("Ended")
your_code_time = end_time - start_time

# Measure the time taken by os.walk implementation.
start_time = time.time()
print("Started OS")
result_os_walk = search_using_os_walk(target_file)
print("ended")
end_time = time.time()
os_walk_time = end_time - start_time

# Measure the time taken by your code implementation.


print(f"os.walk time: {os_walk_time} seconds")
print(f"Your code time: {your_code_time} seconds")