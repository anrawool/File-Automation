import os
import sys
path = os.path.join(os.path.join(os.path.dirname(__file__), os.pardir), os.pardir)
sys.path.append(path)
import encrypter
from Managers.database_manager import DBManager

DBM = DBManager('./passwords.sqlite')
AEA = encrypter.AEA(40)
password = input("Please input your password: ")
encryption_password = AEA.encrypt_text(password)
AEA.save_key('encrypter_key.json')
