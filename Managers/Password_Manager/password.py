import os
import sys
path = os.path.join(os.path.join(os.path.dirname(__file__), os.pardir), os.pardir)
sys.path.append(path)
import encrypter
from Managers.database_manager import DBManager

class PasswordManager:
    def __init__(self, max_characters, db_name='passwords.sqlite', db_path='./', key_name='passwords_key.json', key_path='./') -> None:
        self.DBM = DBManager(db_path=f'{db_path}{db_name}')
        if max_characters != None:
            self.AEA = encrypter.AEA(max_characters, key_name=key_name, key_path=key_path)
            self.AEA.save_key()
        else:
            self.AEA = encrypter.AEA(key_name=key_name, key_path=key_path)
            self.AEA.save_key()
        self.conn, self.cursor = self.DBM.get_connection
        try:
            self.setup_db()
        except Exception:
            pass

    def setup_db(self):
        sql = """CREATE TABLE Passwords (
            passid INTEGER PRIMARY KEY AUTOINCREMENT,
            website varchar(300),
            encryption (65534));"""
        self.cursor.execute(sql)

    def insert_password(self, plain_text_password, website):
        encrypted_password = self.AEA.encrypt_text(plain_text_password)
        insert_sql = f"""INSERT INTO Passwords VALUES (NULL, '?', '?');"""
        self.cursor.execute(insert_sql, [website, encrypted_password])

    def retrieve_password(self, website):
        sql = f"""SELECT FROM Passwords encrypted_password WHERE website = {website};"""
        results = self.cursor.execute(sql)
        if type(results) != type([list]):
            results = list(results)
        else:
            pass
        for encryption in results:
            decrypted = self.AEA.decrypt_text(encryption)
            print(f"The passoword for {website} is {decrypted}")
        

manager = PasswordManager(64)
website = input("What is the name of the site that you are creating a new password for: ")
password = input("What is the password: ")
manager.insert_password(password, website)

