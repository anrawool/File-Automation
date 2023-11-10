import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


class RFID_Instance:
    def __init__(self) -> None:
        self.reader = SimpleMFRC522()

    def read_card(self):
        try:
            self.id, self.description = self.reader.read()
            return self.id, self.description
        finally:
            self.end_cycle()
    
    def write_card(self, text):
        try:
            self.reader.write(text)
        finally:
            self.end_cycle()

    def end_cycle(self):
        GPIO.cleanup()