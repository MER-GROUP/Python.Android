from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import os.path
from os.path import dirname
from kivy.lang import Builder
from kivy.utils import platform

if 'android' == platform:
    from plyer import vibrator

# Builder.load_file('vibrator.kv') # not work
Builder.load_file(os.path.join(dirname(__file__), 'vibrator2.kv'))

class VibrationInterface(BoxLayout):
    '''Root Widget.'''

    def vibro(self, n):
        if self.__is_android():
            vibrator.vibrate(n)
        else:
            self.__do_nothing()

    def exists(self):
        if self.__is_android():
            vibrator.exists()
        else:
            self.__do_nothing()

    def cancel(self):
        if self.__is_android():
            vibrator.cancel()
        else:
            self.__do_nothing()

    def pattern(self, arr):
        if self.__is_android():
            vibrator.pattern(arr)
        else:
            self.__do_nothing()
   
    def __is_android(self):
        if 'android' == platform:
            return True
        else:
            return False

    def __do_nothing(self):
        pass

class VibrationApp(App):
    def build(self):
        return VibrationInterface()

    def on_pause(self):
        return True

if __name__ == "__main__":
    VibrationApp().run()