from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep_ms
import framebuf
import math
ancho = 128
alto = 64

x=ADC(Pin(32))
y=ADC(Pin(34))
boton=Pin(35,Pin.IN,Pin.PULL_DOWN)
x.atten(ADC.ATTN_11DB)
x.width(ADC.WIDTH_12BIT)
y.atten(ADC.ATTN_11DB)
y.width(ADC.WIDTH_12BIT)
i2c= I2C(-1, scl = Pin(4), sda = Pin(5))
oled= SSD1306_I2C(ancho, alto, i2c)
oled.hline(0,19,128,1)
oled.hline(0,41,128,1)
oled.vline(38,0,64,1)
oled.vline(87,0,64,1)
'''oled.line(12,14,24,5,1)
oled.line(23,14,15,5,1)'''
sleep_ms(200)
'oled.fill(0)'
oled.show()
def escogerFicha():
    print("Hola")
    sleep_ms(200)
    while True:
        ficha=input("Seleccione la ficha que desea usar: X/O\n")
        ficha=ficha.upper()
        if ficha=="X":
            jugador1="X"
            jugador2="O"
            break
while True:
     sleep_ms(200)
     valorx=x.read()
     valory=y.read()
     if valorx==0:
      oled.text("X",105,28,1)
      oled.show()
      sleep_ms(200)
     elif valorx==4095:
      oled.text("O",10,27,1)
      oled.show()
      sleep_ms(200)
     elif valory==0:
      oled.text("O",57,52,1)
      oled.show()
      sleep_ms(200)
     elif valory==4095:
      oled.text("O",56,7,1)
      oled.show()

      
