import random
import __meta
import string
import json
import os
import Controllers.data as data

ALL_CHARACTERS = list(
    string.punctuation + string.ascii_letters + string.digits + " " + "\n" + "\t"
)
KEY_INORDER = ALL_CHARACTERS.copy()


class AEA:
    # Initialization Function
    def __init__(
        self,
        max_chars=None,
        key_path="./encrypter_key.json",
        write_to_file=False,
        save_key: bool = True,
    ) -> None:
        """
        Encryption Algorithm Code Snippet:

        AEA = AEA(Maximum Characters, Path_to_Save_to)
        encryption = AEA.encrypt_text(text)
        decryption = AEA.decrypt_text(encryption)
        encrypt_file(file_path)
        decrypt_file(file_path)
        """
        self.DataMaker = data.DataMaker()
        self.max_chars = max_chars
        self.write_to_file = write_to_file
        self.save_key_to_file = save_key
        self.key_path, self.key_name = self.set_keys(key_path)
        self.encrypter_setup()

    # Encrypter Setup Function

    def encrypter_setup(self):
        if os.path.exists(self.key_path + self.key_name):
            self.final_key = self.use_key()
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

    # New Key Creation Functions

    def set_keys(self, key_path):
        key_obj = self.DataMaker.make_path(key_path, file_path=False)
        key_path = key_obj.path
        key_name = key_obj.file + key_obj.ext
        return key_path, key_name

    def shuffle_key(self, key):
        original_copy = key
        random.shuffle(key)
        for idx, char in enumerate(key):
            char += key[idx - random.randint(1, 5)]
            key[idx] = char

        return key, original_copy

    def get_max_characters(self, key):
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
                rand_index = random.randint(0, len(ALL_CHARACTERS) - 1)
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

    # Save and Use Options

    def save_key(self):
        with open(f"{self.key_path}{self.key_name}", "w+") as file:
            json.dump(self.final_key, file)

    def use_key(self):
        if not os.path.exists(self.key_path + self.key_name):
            self.save_key()
            with open(self.key_path + self.key_name, "r+") as file:
                key = json.load(file)
        else:
            with open(self.key_path + self.key_name, "r+") as file:
                key = json.load(file)
        return key

    # Text Encrypters

    def encrypt_text(
        self, text, file_path=None, characters=ALL_CHARACTERS, encryption_parent=False
    ):
        cipher = ""
        if file_path == None and self.write_to_file:
            raise Exception("You need to mention a file path to save to!!!")
        for index, character in enumerate(text):
            character_encryption = self.final_key[characters.index(character)]
            cipher += character_encryption
        if not encryption_parent and self.write_to_file:
            path_object = self.DataMaker.make_path(file_path, file_path=False)
            file_path = path_object.path
            file_name = path_object.file
            extension = path_object.ext
            with open(
                file_path + file_name + "_encrypted" + extension, "w+"
            ) as encrypted_file:
                encrypted_file.write(cipher)
        if self.save_key_to_file:
            self.save_key()
        return cipher

    def decrypt_text(
        self, text, all_characters=ALL_CHARACTERS, decryption_parent=False
    ):
        chunks = [
            text[i : i + self.max_chars] for i in range(0, len(text), self.max_chars)
        ]
        decipher_text = ""
        for chunk in chunks:
            index = self.final_key.index(chunk)
            decipher_text += all_characters[index]
        if not decryption_parent and self.write_to_file:
            path_object = self.DataMaker.make_path(file_path, file_path=False)
            file_path = path_object.path
            file_name = path_object.file
            extension = path_object.ext
            with open(
                file_path + file_name + "_decrypted" + extension, "w+"
            ) as decrypted_file:
                decrypted_file.write(decipher_text)
        if self.save_key_to_file:
            self.save_key()
        return decipher_text

    def encrypt_file(self, file_path):
        path_object = self.DataMaker.make_path(file_path, file_path=False)
        org_file_path = file_path
        file_path = path_object.path
        file_name = path_object.file
        extension = path_object.ext
        encryption_parent = True  # Declares that the request came from a parent function and there is no need for the encrypt_text function to create a new instance due to self.write_to_file being set to true
        with open(file_path + file_name + extension, "r") as encryption_file:
            file_data = encryption_file.read()
            encrypted_data = self.encrypt_text(
                file_data, encryption_parent=encryption_parent, file_path=org_file_path
            )
            if self.write_to_file:
                with open(
                    file_path + file_name + "_encrypted" + extension, "w+"
                ) as encrypted_file:
                    encrypted_file.write(encrypted_data)
            if self.save_key_to_file:
                self.save_key()

            return encrypted_data

    def decrypt_file(self, file_path):
        path_object = self.DataMaker.make_path(file_path, file_path=False)
        file_path = path_object.path
        file_name = path_object.file
        extension = path_object.ext
        decryption_parent = True  # Declares that the request came from a parent function and there is no need for the decrypt_text function to create a new instance due to self.write_to_file being set to true
        with open(file_path + file_name + extension, "r") as decryption_file:
            file_data = decryption_file.read()
            for i in range(0, 1):
                max_characters = len(self.final_key[i])
            decrypted_data = self.decrypt_text(
                file_data, decryption_parent=decryption_parent
            )
            if self.write_to_file:
                with open(
                    file_path + file_name + "_decrypted" + extension, "w+"
                ) as decrypted_file:
                    decrypted_file.write(decrypted_data)
            if self.save_key_to_file:
                self.save_key()
            return decrypted_data


if __name__ == "__main__":
    encrypter = AEA(256)
    text = input("Enter a message to encrypt: ")
    encryption = encrypter.encrypt_text(text)
    with open("test_file.txt", "w+") as write_file:
        write_file.write(encryption)
