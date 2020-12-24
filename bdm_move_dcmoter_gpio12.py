# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:02:32 2020

@author: Souichirou Kikuchi

"""

import spidev
import RPi.GPIO as GPIO
from time import sleep

CHN = 0 # ADコンバーター接続チャンネル
MOTOR_PWM0 = 12 # DC Motor PWM0

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PWM0, GPIO.OUT)
pwm0 = GPIO.PWM(MOTOR_PWM0, 50)  # 周波数50Hz
pwm0.start(0)


try:
    print('--- start program ---')
    while True:
        val = 5000
        print('val= ',val)
        duty = (val - 2048) * 50 / 2048
        pwm0.ChangeDutyCycle(duty)
        sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    pwm0.stop()
    GPIO.cleanup()
    print('--- stop program ---')