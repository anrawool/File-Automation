import os
import sys
import subprocess
from Controllers.data import *

# Currently in Development

class Setup():
    def __init__(self):
        self.platform = sys.platform
        self.DataMaker = DataMaker()

    def initialize(self):
        possible_outcomes = ['win32', 'darwin', 'linux', 'win64']
        if not self.platform in possible_outcomes:
            print("Sorry, this program is not compatible with your system")
            print("Please look forward to compatible versions coming out. You can open a issue to the github repository : https://github.com/anrawool/File-Automation stating your request along with your Operting System.")
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
        if self.platform != 'win32' or self.platform != 'win64':
            self._execute_shell_script_unix()
        else:
            pass
    
    def _execute_shell_script_unix(self):
        find_path = subprocess.check_output("which python3", shell=True)
        self.make_path = input("Please provide the entire path to which you want all your programming projects to be stored in: ")
        print("Path Object:", self.make_path)
        self.python_path = find_path.decode()
        os.system("chmod x+ setup.sh")
        os.system(f"./setup.sh {self.python_path} {self.make_path.path}")


Setup  = Setup()
Setup.initialize()


