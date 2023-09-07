import __meta
import paramiko
from Controllers.Password_Manager.password import PasswordManager
from Controllers.encrypter import *
from getpass import getpass

absolute_current_path = __meta.absolute_current_path
class SSH_Connection:
    def __init__(self, username, ip='auto', password='auto', port=22) -> None:
        self.manager =  PasswordManager(db_path = f'{absolute_current_path}databases/passwords.sqlite', key_path=f'{absolute_current_path}keys/passwords_key.json')
        self.AEA = AEA(key_path=f'{absolute_current_path}../keys/passwords_key.json')
        self.port = port
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
        try:
            self.connection.connect(ip, username=username, password=password, port=self.port)
        except:
            print("Something went wrong... Try to check the port configuration on your device")
    
    def exec_command(self, command):
        results = []
        stdin, stdout, stderr = self.connection.exec_command(command)
        for line in stdout:
            results.append(line.strip('\n'))
        print("The command was executed flawlessly!!!")
        return stdin, results, stderr

    def transfer_object(self, local_path, remote_path):
        sftp = self.connection.open_sftp()
        sftp.put(local_path, remote_path)
        sftp.close()

    def close_channel(self):
        self.connection.close()
            

# connector = SSH_Connection('sarthak', ip='192.168.1.58')
# final = connector.exec_command("cd Documents/Automation/ && git pull")
# connector.close_channel()