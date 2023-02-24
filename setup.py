import os
import sys
import subprocess
from data import *

class Setup():
    def __init__(self):
        self.platform = sys.platform
        self.DataMaker = DataMaker()

    def initialize(self):
        possible_outcomes = ['win32', 'darwin', 'linux', 'win64']
        if not self.platform in possible_outcomes:
            print("Sorry, this program is not compatible with your system")
            print("Please look forwared to compatible versions coming out. You can open a issue to the github repository : https://github.com/anrawool/File-Automation stating your request along with your Operting System.")
            exit()
        print("Great, This Setup Program is compatible with your system.")
        start = input("Would you like to start the setup process [Y/n]: ")
        if start != 'Y':
            print("Okay, Thank Your Very Much")
            exit()
        print("Setting up...")

        permission = input("Please give permission to install python modules in your computer [Y/n]: ")
        if permission != 'Y':
            print("Okay, Thank You Very Much")
            exit()
        print("Thank you, setting up...")
        print("This may take a moment...")
        self.path = os.path.abspath(os.getcwd())
        if self.platform != 'win32':
            self._execute_shell_script_unix()
        else:
            pass
    
    def _execute_shell_script_unix(self):
        find_path = subprocess.check_output("which python3", shell=True)
        make_path = input("Please provide the entire path to which you want all your programming projects to be stored in: ")
        make_path = self.DataMaker.make_path(path=make_path, path_file=False)
        print("Path Object", make_path)
        self.python_path = find_path.decode()
        os.system(f"./setup.sh {self.python_path}")


Setup  = Setup()
Setup.initialize()


