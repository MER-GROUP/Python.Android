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
    from jnius import autoclass
    # package_manager = autoclass('android.content.pm.PackageManager')
    # application_info = autoclass('android.content.pm.ApplicationInfo')
# *****************************************************************************************
class Main(BoxLayout):
    # ---------------------------------------------------------------------------
    '''Root Widget'''
    # ---------------------------------------------------------------------------
    # показать директорию программы
    def shor_prog_dir(self):
        if 'android' == platform:
            # self.ids.label_main.text = package_manager.getApplicationInfo().dataDir

            # определение DPI
            # DisplayMetrics = autoclass('android.util.DisplayMetrics')
            # metrics = DisplayMetrics()
            # self.ids.label_main.text = metrics.getDeviceDensity()

            # Получение языка установленного в системе
            lang = autoclass("Local").getDefault().getDisplayLanguage()
            self.ids.label_main.text = str(lang)

            # Вибрация телефона
            # Для начала нам нужна ссылка на Java Activity, в которой
            # запущено приложение, она хранится в загрузчике Kivy PythonActivity
            PythonActivity = autoclass('org.renpy.android.PythonActivity')
            activity = PythonActivity.mActivity
            Context = autoclass('android.content.Context')
            vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
            vibrator.vibrate(10000)  # аргумент указывается в миллисекундах
        else:
            self.ids.label_main.text = 'It is not Android'
    # ---------------------------------------------------------------------------
    # показать директорию программы base.apk
    def shor_prog_base(self):
        if 'android' == platform:
            # self.ids.label_main.text = package_manager.getApplicationInfo().sourceDir
            self.ids.label_main.text = 'It is Android'
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