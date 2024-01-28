import os


main_path = os.path.abspath("../")


_meta_paths = [
    "./",
    "../",
    "../User-Interface",
    "../Term_Actions",
    "../Scripts",
    "../School/StudyPlanner",
    "../School/Tests",
    "../PvtInfo",
    "../logs",
    "../keys",
    "../downloads",
    "../databases",
    "../Controllers",
    "../Controllers/Password_Manager",
    "../Beta",
]

for path in _meta_paths:
    path = os.path.abspath(path)
    path += "/"
    __meta_code = f"""
import os, sys

absolute_current_path = '{path}'
path = os.path.join(os.path.abspath(absolute_current_path + '../'))
sys.path.append(path)

    """
    with open(path + "__meta.py", "w+") as file:
        file.write(__meta_code)

exit()
