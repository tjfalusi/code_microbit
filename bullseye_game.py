# Add your Python code here. E.g.
from microbit import *
num = 0
time = 5
display.show(num)
pin0.write_digital(0)
pin1.write_digital(0)

while True:
    if accelerometer.get_z() > 200:
        num = num + 1
        while time > 0:
            pin0.write_digital(1)
            pin1.write_digital(1)
            sleep (100)
            pin0.write_digital(0)
            pin1.write_digital(0)
            sleep (100)
            time = time -1
        display.show(num)
    time = 5
    