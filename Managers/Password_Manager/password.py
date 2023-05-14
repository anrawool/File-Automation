import os
import sys
path = os.path.join('/home/sarthak/Documents/Automation')
sys.path.append(path)
import encrypter
from sqlite3 import OperationalError
from Managers.database_manager import DBManager
from data import *

class PasswordManager:
    def __init__(self, max_characters, db_path='./passwords.sqlite', key_path='./passwords_key.json') -> None:
        self.DataMaker = DataMaker()
        db_path, db_name, key_path, key_name = self.set_paths(db_path, key_path)
        self.DBM = DBManager(db_path=f'{db_path}{db_name}')
        if max_characters != None:
            self.AEA = encrypter.AEA(max_characters, key_path=key_path+key_name)
            self.AEA.save_key()
        else:
            self.AEA = encrypter.AEA(key_path=key_path+key_name)
            self.AEA.save_key()
        self.conn, self.cursor = self.DBM.get_connection
        try:
            self.setup_db()
        except OperationalError:
            pass
        self.authenticate()
    
    
    def authenticate(self):
        correct = False
        for chances in range(0,3):
            if correct == True:
                break
            master_input = input("Please enter your master password: ")
            password_master = self.retrieve_password('master')
            master = password_master[0]
            if master_input == master:
                print("Authenticated, Welcome!!!")
                correct = True
            else:
                print("The Master Password was Wrong")
        if correct != True:
            print("All your chances are over, thank you!!!")        
            exit()
        else:
            pass

    def set_paths(self, db_path, key_path):
        db_obj = self.DataMaker.make_path(db_path, file_path=False)
        key_obj = self.DataMaker.make_path(key_path, file_path=False)
        db_name = db_obj.file + db_obj.ext
        key_name = key_obj.file + key_obj.ext

        return db_obj.path, db_name, key_obj.path, key_name

    # Creating a Master Password

    def master_password_maker(self):
        self.insert_password("Warrior@09", 'master')
 
    def setup_db(self):
        sql = """CREATE TABLE Passwords (
        passid INTEGER PRIMARY KEY AUTOINCREMENT,
        website varchar(255),
        encryption TEXT
        );"""
        self.cursor.execute(sql)
        self.master_password_maker()
        
    def insert_password(self, plain_text_password, website):
        encrypted_password = self.AEA.encrypt_text(plain_text_password)
        insert_sql = f"""INSERT INTO Passwords VALUES (NULL, ?, ?);"""
        self.cursor.execute(insert_sql, (website, encrypted_password))
        self.apply_changes()

    def apply_changes(self):
        self.conn.commit()

    def retrieve_password(self, website):
        sql = f"""SELECT encryption FROM Passwords WHERE website = ?;"""
        results = self.cursor.execute(sql, (website, ))
        if type(results) != type([list]):
            results = list(results)
        else:
            pass
        decrypted_passwords = []
        for encryption in results:
            decrypted = self.AEA.decrypt_text(encryption[0])
            decrypted_passwords.append(decrypted)
        return decrypted_passwords 
        

manager = PasswordManager(64)
manager.insert_password("Warrior@09", "GeeksForGeeks")