import os
import sys

class Setup():
    def initialize(self):
        System = sys.platform
        print(System)
        possible_outcomes = ['win32', 'darwin', 'linux']
        if not System in possible_outcomes:
            print("Sorry, this program is not compatible with your system")
            print("Please look forwared to compatible versions coming out. You can open a issue to the github repository : https://github.com/anrawool/File-Automation stating your request along with your Operting System.")
            exit()
        print("Great, This Program is compatible with your system.")
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
        if not 'win' in self.path:
            self._execute_shell_script_unix()
        else:
            pass
    
    def _execute_shell_script_unix(self):
        python = os.system("which python3")
        os.system("chmod u+x setup.sh")
        os.system(f"./setup.sh {python}")


Setup  = Setup()
Setup.initialize()


