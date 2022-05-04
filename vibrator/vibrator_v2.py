from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import os.path
from os.path import dirname
from kivy.lang import Builder
from kivy.utils import platform

# Builder.load_file('vibrator.kv') # not work
Builder.load_file(os.path.join(dirname(__file__), 'vibrator.kv'))

class VibrationInterface(BoxLayout):
    '''Root Widget.'''
   
    def is_android(self):
        if 'android' == platform:
            return True
        else:
            return False

    def do_nothing(self):
        pass

class VibrationApp(App):
    def build(self):
        return VibrationInterface()

    def on_pause(self):
        return True

if __name__ == "__main__":
    VibrationApp().run()