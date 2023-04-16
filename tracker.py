import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

"""

Track function has four variable attributes: created, deleted, moved and modified
Track function has three attributes for each action: src_path, is_directory and event_type
Every Function using this function must have syntax like:

def example_function(event):
    code

Having the event parameter is necessary to work

"""

def track(path, created_func=None, moved_func=None, deleted_func=None, modified_func=None):
    event_handler = FileSystemEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    if created_func != None:
        event_handler.on_created = created_func
    if deleted_func != None:
        event_handler.on_deleted = deleted_func
    if modified_func != None:
        event_handler.on_modified = modified_func
    if moved_func != None:
        event_handler.on_moved = moved_func
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
        # print("Stopped")