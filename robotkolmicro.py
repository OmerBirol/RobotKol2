from machine import Pin, I2C
import utime
from picobricks import MotorDriver, APDS9960

BUTTON_PIN = 4

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
motor = MotorDriver(i2c)
apds = APDS9960(i2c)

pan_angle = 45
tilt_angle = 45

button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

apds.init_gesture_sensor()  

motor.servo(1, pan_angle)
motor.servo(2, tilt_angle)

while True:
    gesture = apds.read_gesture()  

    if gesture:
        print("Gesture:", gesture)

        if gesture == "UP":
            tilt_angle = 0
            print("Gesture: YUKARI")
        elif gesture == "DOWN":
            tilt_angle = 90
            print("Gesture: AŞAĞI")
        elif gesture == "LEFT":
            pan_angle = 0
            print("Gesture: SOL")
        elif gesture == "RIGHT":
            pan_angle = 90
            print("Gesture: SAĞ")

    
    if button.value() == 1:  
        pan_angle = 45
        tilt_angle = 45
        motor.servo(1, pan_angle)
        motor.servo(2, tilt_angle)
        print("Sıfırlandı!")
        utime.sleep_ms(200)

    motor.servo(1, pan_angle)
    motor.servo(2, tilt_angle)
    utime.sleep_ms(100)
