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
# File - работа с файлами
# from File import File
# f = File()
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
    # permissions - права доступа
    from android.permissions import Permission, request_permissions, check_permission

    def check_permissions(perms):
        for perm in perms:
            if check_permission(perm) != True:
                return False
        return True

    perms = [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE]
        
    if  check_permissions(perms)!= True:
        request_permissions(perms)
    # ---------------------------------------------------------------------------
    # получить Download путь к каталогу в Android
    from android.storage import primary_external_storage_path
    dir = primary_external_storage_path()
    download_dir_path = os.path.join(dir, 'Download/')
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
    # The SDK version of the software currently running on this hardware device.
    def get_SDK_INT(self):
        if 'android' == platform:
            try:
                VERSION = autoclass('android.os.Build$VERSION')
                # import android.os.Build as Build - not work
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
    # создать файл в директории /storage/emulated/0/Download/
    def file_create(self, name):
        if 'android' == platform:
            try:
                # # определяем директорию
                # path = join(dirname(__file__),'')
                # # test path
                # self.ids.label_main.text = str(path)
                # test check_permissions(perms)
                # self.ids.label_main.text = str('check_permissions: ') + str(check_permissions(perms))
                # test
                self.ids.label_main.text = str(download_dir_path)

                # File - работа с файлами
                try:
                    from File import File
                except (ModuleNotFoundError):
                    from delfile.File import File

                f = File()
                # file_name = f.file_name_init('/storage/emulated/0/Download/', str(name))
                file_name = f.file_name_init(str(download_dir_path), str(name))
                f.file_write(file_name, ['test'])              

                
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
class DelFile(App):
    # ---------------------------------------------------------------------------
    '''App Widget'''
    # ---------------------------------------------------------------------------
    def build(self):
        self.title = 'Директории'
        return Main()
    # ---------------------------------------------------------------------------
# запуск программы
if __name__ == '__main__':
    DelFile().run()
# *****************************************************************************************