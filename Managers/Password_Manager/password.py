import os
import sys
path = os.path.join('/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/Automation/')
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

    def set_paths(self, db_path, key_path):
        db_obj = self.DataMaker.make_path(db_path, file_path=False)
        key_obj = self.DataMaker.make_path(key_path, file_path=False)
        db_name = db_obj.file + db_obj.ext
        key_name = key_obj.file + key_obj.ext

        return db_obj.path, db_name, key_obj.path, key_name

    def setup_db(self):
        sql = """CREATE TABLE Passwords (
        passid INTEGER PRIMARY KEY AUTOINCREMENT,
        website varchar(255),
        encryption TEXT
        );"""
        self.cursor.execute(sql)

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
        for encryption in results:
            decrypted = self.AEA.decrypt_text(encryption[0])
            print(f"The passoword for {website} is {decrypted}")
        

manager = PasswordManager(64)
website = input("What is the name of the site that you are creating a new password for: ")
password = input("What is the password: ")
manager.insert_password(password, website)
manager.retrieve_password(website)

