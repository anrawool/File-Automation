# File for experimentation
import encrypter

encrypter_AEA = encrypter.AEA()
encrypter_AEA.encrypter_setup()
with open('test_file.txt', 'r') as file:
    text = file.read()

extract_key = encrypter_AEA.use_key('encrypter_key.json')
if extract_key == encrypter_AEA.final_key:
    pass
for i in range(0, 1):
    max_characters = len(extract_key[i])
decrypted = encrypter_AEA.decrypt_text(text)
encrypter_AEA.encrypt_file('./', 'data', '.py')
encrypter_AEA.decrypt_file('./', 'data_encrypted', '.py')