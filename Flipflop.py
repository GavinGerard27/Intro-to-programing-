from adafruit_circuitplayground import cp
import time
cp.pixels.brightness = (0.1)
while True:
    if cp.switch:
        for i in range(0, 5):
            cp.pixels[i] =(0, 0, 0)
        for i in range(5, 10):
            cp.pixels[i] = (0, 255, 0)
    
    
    else:
        for i in range(0, 5):
            cp.pixels[i] = (0, 255, 0)
        for i in range(0, 5):
            cp.pixels[i] =(0, 0, 0)



time.sleep

