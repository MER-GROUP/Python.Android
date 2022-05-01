from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from plyer.vibrator import vibrator

Builder.load_file('vibrator.kv')

class VibrationInterface(BoxLayout):
    '''Root Widget.'''
    
    def vibro(self, n):
        vibrator.vibrate(n)

    def cancel(self):
        vibrator.cancel()

    def pattern(self):
        # vibrator.pattern([float(n) for n in self.root.ids.ti.text.split(',')])
        vibrator.pattern([float(n) for n in self.ids.ti.text.split(',')])

    def exists(self):
        vibrator.exists()

class VibrationApp(App):
    def build(self):
        return VibrationInterface()

    def on_pause(self):
        return True

if __name__ == "__main__":
    VibrationApp().run()