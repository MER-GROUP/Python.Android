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
# импортируем молуль os
# listdir - файлы в текущей директории
# chmod - управление правами доступа у файлам и директориям
# mkdir - создание директории/папки
import os
from os import listdir, chmod, mkdir
# импортируем молуль stat (работа с разрешениями прав доступа файлов и папок)
import stat
# *****************************************************************************************
# platform - определение операционки
from kivy.utils import platform
if 'android' == platform:
    # ---------------------------------------------------------------------------
    # # permissions - права доступа
    # from android.permissions import Permission, request_permissions, check_permission

    # def check_permissions(perms):
    #     for perm in perms:
    #         if check_permission(perm) != True:
    #             return False
    #     return True

    # perms = [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE]
        
    # if  check_permissions(perms)!= True:
    #     request_permissions(perms)
    # ---------------------------------------------------------------------------
    # autoclass - импорт java классов
    from jnius import autoclass, JavaException
    Context = autoclass('android.content.Context')
    PackageManager = autoclass('android.content.pm.PackageManager')
    ApplicationInfo = autoclass('android.content.pm.ApplicationInfo')
    # ---------------------------------------------------------------------------
# *****************************************************************************************
class Main(BoxLayout):
    # ---------------------------------------------------------------------------
    '''Root Widget'''
    # ---------------------------------------------------------------------------
    # variable
    pass
    # ---------------------------------------------------------------------------
    # Return the name of this application's package.
    def getPackageName(self):
        if 'android' == platform:
            try:
                self.ids.label_main.text = str(
                    Context.getPackageName()
                    )
            except BaseException as e:
                self.ids.label_main.text = 'BaseException: ' + str(e)
            except JavaException as e:
                self.ids.label_main.text = 'JavaException: ' + str(e)
        else:
            self.ids.label_main.text = 'It is not Android'
    # ---------------------------------------------------------------------------
    # The SDK version of the software currently running on this hardware device.
    def get_SDK_INT(self):
        if 'android' == platform:
            try:
                VERSION_ = autoclass('android.os.Build.VERSION')
                VERSION = VERSION_()
                # import android.os.Build as Build
                self.ids.label_main.text = str(
                    VERSION.SDK_INT
                    )
            except BaseException as e:
                self.ids.label_main.text = 'BaseException: ' + str(e)
            except JavaException as e:
                self.ids.label_main.text = 'JavaException: ' + str(e)
        else:
            self.ids.label_main.text = 'It is not Android'
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# окно программы
class LinkApp(App):
    # ---------------------------------------------------------------------------
    '''App Widget'''
    # ---------------------------------------------------------------------------
    def build(self):
        self.title = 'Директории'
        return Main()
    # ---------------------------------------------------------------------------
# запуск программы
if __name__ == '__main__':
    LinkApp().run()
# *****************************************************************************************