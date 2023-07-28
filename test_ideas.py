# File for experimentation
import os
def is_executable(file_path):
    return os.access(file_path, os.X_OK)

print(is_executable('/home/nexus/Documents/Nexus/User-Interface/Server/bin/python3'))
