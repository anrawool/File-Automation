# File for experimentation
import encrypter

encrypter_AEA = encrypter.AEA()
with open('test_file.txt', 'r') as file:
    text = file.read()

encrypter_AEA.encrypt_file('./data.py')
encrypter_AEA.decrypt_file('./data_encrypted.py')