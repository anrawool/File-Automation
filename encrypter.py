import random
import string
import time
import json
import os

ALL_CHARACTERS = list(string.punctuation + string.ascii_letters + string.digits + " " + "\n" + '\t')
KEY_INORDER = ALL_CHARACTERS.copy()

class AEA:
    def __init__(self, max_chars=None, key_name='encrypter_key.json', key_path='./') -> None:
        self.max_chars = max_chars
        self.key_name = key_name
        self.key_path = key_path
        self.encrypter_setup()
    def shuffle_key(self, key):
        original_copy = key
        random.shuffle(key)
        for idx, char in enumerate(key):
            char += key[idx-random.randint(1, 5)]
            key[idx] = char
        
        return key, original_copy

    def get_max_characters(self, key):
        char_len = []
        max_cur_length = 0
        for item in key:
            length_of_character = len(item)
            if length_of_character > max_cur_length:
                max_cur_length = length_of_character
        return max_cur_length


    def normalize_characters(self, key):
        for index_of_item, item in enumerate(key):
            chracters_to_increase = self.max_chars - len(item)
            for x in range(0, chracters_to_increase):
                rand_index = random.randint(0, len(ALL_CHARACTERS)-1)
                item += ALL_CHARACTERS[rand_index]
            key[index_of_item] = item
        return key

    def check_num_chars(self):
        for item in self.final_key:
            if len(item) == self.max_chars:
                pass
            else:
                print("CHARACTERS NOT NORMALIZED PROPERLY...")
                return False
            return True

    def encrypt_text(self, text, characters=ALL_CHARACTERS):
        cipher = ''
        for index, character in enumerate(text):
            character_encryption = self.final_key[characters.index(character)]
            cipher += character_encryption
        return cipher

    def decrypt_text(self, text, all_characters=ALL_CHARACTERS):
        chunks = [text[i:i+self.max_chars] for i in range(0, len(text), self.max_chars)]
        decipher_text = ''
        for chunk in chunks:
            index = self.final_key.index(chunk)
            decipher_text += all_characters[index]
        
        return decipher_text

    def save_key(self):
        with open(f"{self.key_path}{self.key_name}", "w+") as file:
            json.dump(self.final_key, file)

    def use_key(self, file_name):
        with open(file_name, 'r+') as file:
            key = json.load(file)
        return key

    def encrypter_setup(self):
        if os.path.exists(self.key_path + self.key_name):
            self.final_key = self.use_key(self.key_path + self.key_name)
            maximum_chars = self.get_max_characters(self.final_key)
            if self.max_chars == None:
                self.max_chars = maximum_chars
        else:
            shuffled, original = self.shuffle_key(KEY_INORDER)
            if original == KEY_INORDER:
                # print("Original copy is correct!!")
                pass
            maximum_chars = self.get_max_characters(shuffled)
            if self.max_chars == None:
                self.max_chars = maximum_chars
            self.final_key = self.normalize_characters(shuffled)
            check = self.check_num_chars()
            if not check:
                exit()
        return self.final_key, self.max_chars

    def encrypt_file(self, file_path, file_name, extension):
        with open(file_path + '/' + file_name + extension, 'r') as encryption_file:
            file_data = encryption_file.read()
            encrypted_data = self.encrypt_text(file_data)
            with open(file_path + file_name + '_encrypted' + extension, 'w+') as encrypted_file:
                encrypted_file.write(encrypted_data)
    def decrypt_file(self, file_path, file_name, extension):
        with open(file_path+'/' + file_name + extension, 'r') as decryption_file:
            file_data = decryption_file.read()
            for i in range(0, 1):
                max_characters = len(self.final_key[i])
            decrypted_data = self.decrypt_text(file_data)
            with open(file_path + '/' + file_name + '_decrypted' + extension, 'w+') as decrypted_file:
                decrypted_file.write(decrypted_data)

if __name__ == '__main__':
    encrypter = AEA(40)
    encrypter.save_key()
    text = input("Enter a message to encrypt: ")
    encryption = encrypter.encrypt_text(text)
    with open('test_file.txt', 'w+') as write_file:
        write_file.write(encryption)