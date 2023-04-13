# File for experimentation
import os
import time
from search import *
from duplicate import *

def old_search_algorithm(target_folder, target, mode):
    start = time.time()
    search_instance = FileSearcher_OLD(target_folder, target, mode)
    final = search_instance.search()
    time_taken = time.time() - start
    return final, time_taken

def optimized_search(target_folder, target, mode):
    search_instance = FileSearcher(target_folder, target, mode, record_time=True)
    results = search_instance.search() 
    return results

search_items = {'subsubdir1': "--all-files", "Automation": ".py", "Downloads":"--all-files", "Sarthak":"--all-folders"}
final_time_OLD = []
final_time_NEW = []

for key, val in search_items.items():
    if val == '':
        mode = 'folder'
    else:
        mode = ''
    objects_OLD, time_taken_OLD = old_search_algorithm(key, val, mode)

    objects = optimized_search(key, val, mode)

    if len(objects_OLD[0][0]) == len(objects[1]):
        print("MATCHED")
        print("Time taken for old algorithm:", )
        print("Time taken for optimized algorithm:", objects[-1])
        final_time_OLD.append(time_taken_OLD)
        final_time_NEW.append(objects[-1])
    else:
        print("OLD:", objects_OLD)
        print("\n")
        print("NEW:", objects[0])
        exit()
print("AVERAGE OF OLD TIME:", sum(final_time_OLD)/len(final_time_OLD))
print("AVERAGE OF OLD TIME:", sum(final_time_NEW)/len(final_time_NEW))



