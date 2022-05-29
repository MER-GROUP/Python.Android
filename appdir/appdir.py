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
            
            # # test-1
            # try:
            #     # Context = autoclass('android.content.Context')
            #     # context = Context() - not work
            #     #
            #     # Returns absolute path to application-specific directory 
            #     # on the primary shared/external storage device where 
            #     # the application can place cache files it owns.
            #     #
            #     # Возвращает абсолютный путь к определенному для приложения 
            #     # каталогу на основном общем/внешнем устройстве хранения, 
            #     # где приложение может размещать принадлежащие ему файлы кэша.
            #     self.ids.label_main.text = str(
            #         Context.getExternalFilesDir(None).getAbsolutePath()
            #         )
            # except JavaException as e:
            #     self.ids.label_main.text = 'JavaException: ' + str(e)

            # test-2
            try:
                # Context = autoclass('android.content.Context')
                # context = Context() - not work

                self.ids.label_main.text = str(
                    # Context.getApplicationInfo().getMemtagMode()
                    Context.getPackageCodePath()
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