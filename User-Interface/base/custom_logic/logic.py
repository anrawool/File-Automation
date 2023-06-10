import os

# Paths
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
absolute_working_dir = os.path.abspath(parent_dir)

def get_readable_size(size_in_bytes):
    # Define the suffixes for different size units
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']

    # Determine the appropriate size unit
    index = 0
    while size_in_bytes >= 1024 and index < len(suffixes) - 1:
        size_in_bytes /= 1024
        index += 1

    # Format the size with the appropriate unit and decimal places
    readable_size = f"{size_in_bytes:.2f} {suffixes[index]}"
    return readable_size

def get_file_size(files) -> tuple:
    all_file_sizes = []
    for file in files:
        file_path = file.file.name
        file_size = os.path.getsize(f'{absolute_working_dir}/User-Interface/media/{file_path}')
        readable_size = get_readable_size(file_size)
        all_file_sizes.append(readable_size)
    return all_file_sizes