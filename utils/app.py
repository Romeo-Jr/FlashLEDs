from utils.gui import set_image, RED_OFF,RED_ON, GREEN_OFF, GREEN_ON, YELLOW_OFF, YELLOW_ON
from utils.flash_led import FlashLED

# FUNCTION THAT TAKES THE PIN NUMBER OF RED LED AND TURN ON
# SET THE IMAGE FOR THE SPECIFIC LEDs
def flash_red():
    red_led = FlashLED(9)
    red_led.turn_on()

    set_image(RED_ON, 0, 0)
    set_image(GREEN_OFF, 0, 1)
    set_image(YELLOW_OFF, 0, 2)

# FUNCTION THAT TAKES THE PIN NUMBER OF GREEN LED AND TURN ON
# SET THE IMAGE FOR THE SPECIFIC LEDs
def flash_green():
    green_led = FlashLED(10)
    green_led.turn_on()

    set_image(RED_OFF, 0, 0)
    set_image(GREEN_ON, 0, 1)
    set_image(YELLOW_OFF, 0, 2)

# FUNCTION THAT TAKES THE PIN NUMBER OF YELLOW LED AND TURN ON
# SET THE IMAGE FOR THE SPECIFIC LEDs
def flash_yellow():
    yellow_led = FlashLED(8)
    yellow_led.turn_on()

    set_image(RED_OFF, 0, 0)
    set_image(GREEN_OFF, 0, 1)
    set_image(YELLOW_ON, 0, 2)
