from gpiopico import Led
from utime import sleep

if __name__=='__main__':
    led = Led(pin=0, inverted_logic=True)#common anode
    
    for _ in range(4):
        led.on()
        sleep(1)
        led.off()
        sleep(1)

    for pwm in range(256):
      led.pwm_value(pwm)#0-255
      sleep(0.2)