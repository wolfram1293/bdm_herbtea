# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:02:32 2020

@author: Souichirou Kikuchi

"""

import spidev
import RPi.GPIO as GPIO
from time import sleep

CHN = 0 # ADコンバーター接続チャンネル
MOTOR_PWM0 = 21 # DC Motor PWM0

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PWM0, GPIO.OUT)
pwm0 = GPIO.PWM(MOTOR_PWM0, 50)  # 周波数50Hz
pwm0.start(0)

spi = spidev.SpiDev()
spi.open(0, 0) # 0：SPI0、0：CE0
spi.max_speed_hz = 1000000 # 1MHz SPIのバージョンアップによりこの指定をしないと動かない

try:
    print('--- start program ---')
    while True:
        val = 3072
        print('val= ',val)
        duty = (val - 2048) * 50 / 2048
        pwm0.ChangeDutyCycle(duty)
        sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    pwm0.stop()
    spi.close()
    GPIO.cleanup()
    print('--- stop program ---')