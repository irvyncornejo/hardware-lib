from gpiopico import Led, Button
from utime import sleep

if __name__=='__main__':
    led = Led(pin=0, inverted_logic=True)
    button = Button(pin=1)
    
    button.when_pressed = led.on
    button.on_hold = led.off 
    
    while True:
        button.check_state()