import __meta
import paramiko
from Controllers.Password_Manager.password import PasswordManager
from encrypter import *
from getpass import getpass
class SSH_Connection:
    def __init__(self, username, ip='auto', password='auto') -> None:
        self.manager =  PasswordManager(db_path = '/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/Automation_Dev/Controllers/Password_Manager/passwords.sqlite', key_path='/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/Automation_Dev/Controllers/Password_Manager/passwords_key.json')
        self.AEA = AEA(key_path='/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/Automation_Dev/Controllers/Password_Manager/passwords_key.json')
        if ip == 'auto':
            ip = '192.168.1.58'
        if password == 'auto':
            results = self.manager.retrieve_password(ip)
            if len(results) == 0:
                print("There is no existing record of this IP address, please enter a new password -")
                new_pass = getpass()
                self.manager.insert_password(new_pass, ip)
            password = results[0]
        else:
            password = password
        self.connection = paramiko.SSHClient()
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection.get_host_keys()
        self.connection.connect(ip, username=username, password=password)
    
    def exec_command(self, command):
        results = []
        stdin, stdout, stderr = self.connection.exec_command(command)
        for line in stdout:
            results.append(line.strip('\n'))
        print("The command was executed flawlessly!!!")
        return stdin, results, stderr
    
    def close_channel(self):
        self.connection.close()
            

# connector = SSH_Connection('sarthak', ip='192.168.1.58')
# final = connector.exec_command("cd Documents/Automation/ && git pull")
# connector.close_channel()