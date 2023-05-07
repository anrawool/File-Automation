import random
import string
import time
import json
import os

ALL_CHARACTERS = list(string.punctuation + string.ascii_letters + string.digits + " ")
KEY_INORDER = ALL_CHARACTERS.copy()

def shuffle_key(key):
    original_copy = key
    random.shuffle(key)
    for idx, char in enumerate(key):
        char += key[idx-random.randint(1, 5)]
        key[idx] = char
    
    return key, original_copy

def get_max_characters(key):
    char_len = []
    max_cur_length = 0
    for item in key:
        length_of_character = len(item)
        if length_of_character > max_cur_length:
            max_cur_length = length_of_character
    return max_cur_length


def normalize_characters(key, max_chars):
    for index_of_item, item in enumerate(key):
        chracters_to_increase = max_chars - len(item)
        for x in range(0, chracters_to_increase):
            rand_index = random.randint(0, len(ALL_CHARACTERS)-1)
            item += ALL_CHARACTERS[rand_index]
        key[index_of_item] = item
    return key

def check_num_chars(key, max_chars):
    for item in key:
        if len(item) == max_chars:
            pass
        else:
            print("CHARACTERS NOT NORMALIZED PROPERLY...")
            return False
        return True

def encrypt_text(text, key, characters):
    cipher = ''
    for index, character in enumerate(text):
        character_encryption = key[characters.index(character)]
        cipher += character_encryption
    
    return cipher

def decrypt_text(text, key, max_length_chars, all_characters):
    n = max_length_chars
    chunks = [text[i:i+n] for i in range(0, len(text), n)]
    decipher_text = ''
    for chunk in chunks:
        index = key.index(chunk)
        decipher_text += all_characters[index]
    
    return decipher_text

def save_key(file_name, key):
    with open(file_name, "w+") as file:
        json.dump(key, file)

def use_key(file_name):
    with open(file_name, 'r+') as file:
        key = json.load(file)
    return key

if os.path.exists('encrypter_key.json'):
    final_key = use_key('encrypter_key.json')
    maximum_chars = get_max_characters(final_key)
else:
    shuffled, original = shuffle_key(KEY_INORDER)
    if original == KEY_INORDER:
        # print("Original copy is correct!!")
        pass
    maximum_chars = get_max_characters(shuffled)
    final_key = normalize_characters(shuffled, maximum_chars)
    check = check_num_chars(final_key, maximum_chars)
    if not check:
        exit()



if __name__ == '__main__':
    text = input("Enter a message to encrypt: ")
    encryption = encrypt_text(text, final_key, ALL_CHARACTERS)
    save_key('encrypter_key.json', final_key)
    print(f'The text was encrypted into: {encryption}')
    with open('test_file.txt', 'w+') as write_file:
        write_file.write(encryption)