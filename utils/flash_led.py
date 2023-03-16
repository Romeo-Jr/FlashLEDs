import pyfirmata
from dotenv import load_dotenv
from os import getenv

load_dotenv(".venv")

PORT = getenv("PORT")

BOARD = pyfirmata.Arduino(PORT)

# INDEX 0 = GREEN
# INDEX 1 = RED
# INDEX 2 = YELLOW
LED_LIST = [10, 9, 8]

# CLASS FOR FLASHING LEDs 
# IT LOOP THE LED_LIST FIRST THEN TURN ON THE LED THAT THE USER WANTS
class FlashLED:
    def __init__(self, led_to_flash):
        self.led_to_flash = led_to_flash
    
    def turn_on(self):
        for led in LED_LIST:
            if led == self.led_to_flash:
                BOARD.digital[led].write(1)
            else:
                BOARD.digital[led].write(0)