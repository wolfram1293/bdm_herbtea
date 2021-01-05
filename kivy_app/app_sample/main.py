# -*- coding: utf-8 -*
import os
import kivy
import time

from kivy.app import App
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.properties import ObjectProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

# 日本語フォント表示対応
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path("./fonts")         
LabelBase.register(DEFAULT_FONT, "ゴシック.ttc")

# kvファイルを画面ごとに分離してバラで読み込む
from kivy.lang import Builder

Builder.load_file('top_window.kv')
Builder.load_file('window1.kv')
Builder.load_file('window2.kv')
Builder.load_file('window3.kv')
Builder.load_file('popup1.kv')

from kivy.core.window import Window
Window.size = (800,500)

# raspi
import spidev
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
pwm12 = GPIO.PWM(12, 50)  # 周波数50Hz
pwm16 = GPIO.PWM(16, 50)  # 周波数50Hz
pwm20 = GPIO.PWM(20, 50)  # 周波数50Hz
pwm21 = GPIO.PWM(21, 50)  # 周波数50Hz


class MainRoot(FloatLayout):
    top_window = None
    window1 = None
    window2 = None
    window3 = None
    popup1 = None
    popup2 = None
    popup3 = None
    popup4 = None
 
    def __init__(self, **kwargs):
        # 起動時に各画面を作成して使い回す
        self.top_window = Factory.TopWindow()
        self.window1 = Factory.Window1()
        self.window2 = Factory.Window2()
        self.window3 = Factory.Window3()
        self.popup1 = Factory.Popup1()
        self.popup2 = Factory.Popup2()
        self.popup3 = Factory.Popup3()
        self.popup4 = Factory.Popup4()
        super(MainRoot, self).__init__(**kwargs)

    def change_disp1(self):
        self.clear_widgets()
        self.add_widget(self.window1)

    def change_disp2(self, wait_time):
        self.clear_widgets()
        self.add_widget(self.window2)
        self.hello()
        Clock.schedule_once(lambda dt: self.change_disp3(), wait_time)
    
    def change_disp3(self):
        self.clear_widgets()
        self.add_widget(self.window3)
        Clock.schedule_once(lambda dt: self.change_disp1(), 2)

    def popup_disp1(self):
        self.popup1.open()

    def popup_disp2(self):
        self.popup2.open()

    def popup_disp3(self):
        self.popup3.open()

    def popup_disp4(self):
        self.popup4.open()

    def popup_close1(self):
        self.popup1.dismiss()

    def popup_close2(self):
        self.popup2.dismiss()

    def popup_close3(self):
        self.popup3.dismiss()

    def popup_close4(self):
        self.popup4.dismiss()

    def hello(self):
        print("hello, kivy!")

    def move_dcmoter_gpio12(self):
        pwm12.start(0)
        val = 5000
        print('val= ',val)
        duty = (val - 2048) * 50 / 2048
        pwm12.ChangeDutyCycle(duty)
        Clock.schedule_once(lambda dt: self.stop_dcmoter(pwm12), 10)
    
    def move_dcmoter_gpio16(self):
        pwm16.start(0)
        val = 5000
        print('val= ',val)
        duty = (val - 2048) * 50 / 2048
        pwm16.ChangeDutyCycle(duty)
        Clock.schedule_once(lambda dt: self.stop_dcmoter(pwm16), 10) 
    
    def move_dcmoter_gpio20(self):
        pwm20.start(0)
        val = 5000
        print('val= ',val)
        duty = (val - 2048) * 50 / 2048
        pwm20.ChangeDutyCycle(duty)
        Clock.schedule_once(lambda dt: self.stop_dcmoter(pwm20), 10)
    
    def move_dcmoter_gpio21(self):
        pwm21.start(0)
        val = 5000
        print('val= ',val)
        duty = (val - 2048) * 50 / 2048
        pwm21.ChangeDutyCycle(duty)
        Clock.schedule_once(lambda dt: self.stop_dcmoter(pwm21), 10)
    
    def stop_dcmoter(self, pwm):
        pwm.stop()



class MainApp(App): 
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = 'トップページ'

    pass

if __name__ == "__main__":
    MainApp().run()