# -*- coding: utf-8 -*
import os
import kivy
import time

from kivy.app import App
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty  # 追加

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

# 日本語フォント表示対応
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

#フォントへのパスとフォント設定・環境によって要変更！！！！
resource_add_path("./fonts")         
LabelBase.register(DEFAULT_FONT, "ゴシック.ttc")

# kvファイルを画面ごとに分離してバラで読み込む
from kivy.lang import Builder

Builder.load_file('top_window.kv')
Builder.load_file('window_self_blend.kv')
Builder.load_file('window1.kv')
Builder.load_file('window2.kv')
Builder.load_file('window3.kv')
Builder.load_file('popup1.kv')

from kivy.core.window import Window
Window.size = (800,500)


class MainRoot(FloatLayout):
    top_window = None
    window1 = None
    window2 = None
    window3 = None
    window_self_blend = None
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
        self.window_self_blend = Factory.WindowSelfBlend()
        self.popup1 = Factory.Popup1()
        self.popup2 = Factory.Popup2()
        self.popup3 = Factory.Popup3()
        self.popup4 = Factory.Popup4()
        super(MainRoot, self).__init__(**kwargs)

    def show_top(self):
        self.clear_widgets()
        self.add_widget(self.top_window)

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

    def change_disp_self_blend(self):
        self.clear_widgets()
        self.add_widget(self.window_self_blend)

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



class MainApp(App): 
    # 各茶葉の量
    lavandula_num = 0
    rose_num = 0
    chamomile_num = 0
    blue_num = 0
    # テキスト
    lavandula_text = StringProperty()
    rose_text = StringProperty()
    chamomile_text = StringProperty()
    blue_text = StringProperty()

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = 'トップページ'
        #　グローバル変数
        self.lavandula_text = "0 g"
        self.rose_text = "0 g"
        self.chamomile_text = "0 g" 
        self.blue_text = "0 g"
        self.lavandula_num = 0
        self.rose_num = 0
        self.chamomile_num = 0
        self.blue_num = 0
    
    def lavandula_add(self):
        self.lavandula_num += 1
        self.lavandula_text = str(self.lavandula_num)+" g"
    
    def lavandula_delt(self):
        if self.lavandula_num > 0:
            self.lavandula_num -= 1
        self.lavandula_text = str(self.lavandula_num)+" g"

    def rose_add(self):
        self.rose_num += 1
        self.rose_text = str(self.rose_num)+" g"
    
    def rose_delt(self):
        if self.rose_num > 0:
            self.rose_num -= 1
        self.rose_text = str(self.rose_num)+" g"

    def chamomile_add(self):
        self.chamomile_num += 1
        self.chamomile_text = str(self.chamomile_num)+" g"
    
    def chamomile_delt(self):
        if self.chamomile_num > 0:
            self.chamomile_num -= 1
        self.chamomile_text = str(self.chamomile_num)+" g"
    
    def blue_add(self):
        self.blue_num += 1
        self.blue_text = str(self.blue_num)+" g"
    
    def blue_delt(self):
        if self.blue_num > 0:
            self.blue_num -= 1
        self.blue_text = str(self.blue_num)+" g"

    

    pass

if __name__ == "__main__":
    MainApp().run()