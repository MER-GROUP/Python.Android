# *****************************************************************************************
# главное окно программы
from kivy.app import App
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# кнопка
from kivy.uix.button import Button
# импортируем молуль os.path
# dirname - определяем текущую директорию
# join - объеденяем директорию + файл (правильный путь файла)
# abspath - определяет абсолютный путь к файлу
from os.path import join, dirname, abspath
# импорт модуля Строитель - загружает .kv файлы в проект
from kivy.lang import Builder
Builder.load_file(join(dirname(__file__), 'main.kv'))
# *****************************************************************************************
# platform - определение операционки
from kivy.utils import platform
if 'android' == platform:
    # autoclass - импорт java классов
    from jnius import autoclass, JavaException
    Context = autoclass('android.content.Context')
    PackageManager = autoclass('android.content.pm.PackageManager')
    ApplicationInfo = autoclass('android.content.pm.ApplicationInfo')
# *****************************************************************************************
class Main(BoxLayout):
    # ---------------------------------------------------------------------------
    '''Root Widget'''
    # ---------------------------------------------------------------------------
    # показать директорию программы
    def shor_prog_dir(self):
        if 'android' == platform:          
            # self.ids.label_main.text = str(PackageManager.getApplicationInfo().dataDir)

            # test - определение DPI
            DisplayMetrics = autoclass('android.util.DisplayMetrics')
            metrics = DisplayMetrics()
            self.ids.label_main.text = str(metrics.getDeviceDensity())

        else:
            self.ids.label_main.text = 'It is not Android'
    # ---------------------------------------------------------------------------
    # показать директорию программы base.apk
    def shor_prog_base(self):
        if 'android' == platform:
            # self.ids.label_main.text = str(PackageManager.getApplicationInfo().sourceDir)
            # self.ids.label_main.text = 'It is Android'
            
            # test
            try:
                # context = Context()
                self.ids.label_main.text = str(
                    Context.getExternalFilesDir(None).getAbsolutePath()
                    )
            except JavaException as e:
                self.ids.label_main.text = 'JavaException: ' + str(e)
        else:
            self.ids.label_main.text = 'It is not Android'
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# окно программы
class DirApp(App):
    # ---------------------------------------------------------------------------
    '''App Widget'''
    # ---------------------------------------------------------------------------
    def build(self):
        self.title = 'Директории'
        return Main()
    # ---------------------------------------------------------------------------
# запуск программы
if __name__ == '__main__':
    DirApp().run()
# *****************************************************************************************