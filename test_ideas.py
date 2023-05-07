# File for experimentation
import encrypter

with open('test_file.txt', 'r') as file:
    text = file.read()

extract_key = encrypter.use_key('encrypter_key.json')
if extract_key == encrypter.final_key:
    pass
for i in range(0, 1):
    max_characters = len(extract_key[i])
    print(max_characters)
decrypted = encrypter.decrypt_text(text, extract_key, max_characters, encrypter.ALL_CHARACTERS)
print(decrypted)