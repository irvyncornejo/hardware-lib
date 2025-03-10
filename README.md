# Librería para control de Hardware
![kaanbal-chimalli](https://drive.google.com/uc?export=view&id=1O7LklcChPpF3NKHRJjVY-0sa80OAXu5J)

## Raspberry pico o pico w
* Python
GPIO control para raspberry pi pico

### Input Devices
- Touch Sensor
  - Callback Actions
- Potenciometer
- Joystick
- PIR
  - Callback Actions
- LM35
- Nextion Display

### Ouput Devices
- LED
- Relay
- Solid state relay
- Motor DC
- RGB
- Servo motor
- NeoPixel
- Basic Car

### Descargar paquete
```
pip install gpiopico
```
### Uso
```python
from gpiopico import Led

led1 = Led(2, True)
led1.on()
led1.change_pwm(125) #value 0-255
```
