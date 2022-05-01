from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from plyer import vibrator

Builder.load_file('vibrator.kv')

class VibrationInterface(BoxLayout):
    '''Root Widget.'''
    pass

class VibrationApp(App):
    def build(self):
        return VibrationInterface()

    def vibro(self, n):
        vibrator.vibrate(n)

    def cancel(self):
        vibrator.cancel()

    def pattern(self):
        vibrator.pattern([float(n) for n in self.root.ti.text.split(',')])

    def exists(self):
        vibrator.exists()

    def on_pause(self):
        return True

if __name__ == "__main__":
    VibrationApp().run()