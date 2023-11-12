import __meta
from Controllers.rfid_controller import * 
from Controllers import server_conn

class RFID_Action:

    def __init__(self):
        self.instance = RFID_Instance()
    
    def home_action_selector(self):
        self.id, self.desc = self.instance.read_card()
        print(self.desc)
        if self.id == 771040611745:
            print("Welcome Back Sir!!!")
            # Scrape FIITJEE Stuff
            connection = server_conn.SSH_Connection('abhijitrawool', '192.168.1.13')
            _ = connection.exec_command("open -a Firefox")
            _ = connection.exec_command("open -a \"Visual Studio Code.app\"")
            _ = connection.exec_command("open -a iTerm.app")

            connection.close_channel()
            

action = RFID_Action()
action.home_action_selector()
