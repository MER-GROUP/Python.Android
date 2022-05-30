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
    path_base_apk = str()
    # ---------------------------------------------------------------------------
    # показать директорию программы
    def show_prog_dir(self):
        if 'android' == platform:          
            # # test - определение DPI
            # DisplayMetrics = autoclass('android.util.DisplayMetrics')
            # metrics = DisplayMetrics()
            # self.ids.label_main.text = str(metrics.getDeviceDensity())

            # test-3
            try:
                # Context = autoclass('android.content.Context')
                # context = Context() - not work
                #
                # Returns the absolute path to the directory on the filesystem 
                # where all private files belonging to this app are stored.
                #
                # Возвращает абсолютный путь к каталогу в файловой системе, 
                # где хранятся все личные файлы, принадлежащие этому приложению.
                self.ids.label_main.text = str(
                    Context.getDataDir().getAbsolutePath()
                    )
            except JavaException as e:
                self.ids.label_main.text = 'JavaException: ' + str(e)

        else:
            self.ids.label_main.text = 'It is not Android'
    # ---------------------------------------------------------------------------
    # показать директорию программы base.apk
    def show_prog_base(self):
        if 'android' == platform:
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
                #
                # Return the full path to this context's primary Android package.
                #
                # Верните полный путь к основному пакету Android этого контекста.
                self.ids.label_main.text = str(
                    Context.getPackageCodePath()
                    )
                self.path_base_apk = str(Context.getPackageCodePath())
            except JavaException as e:
                self.ids.label_main.text = 'JavaException: ' + str(e)
        else:
            self.ids.label_main.text = 'It is not Android'
    # ---------------------------------------------------------------------------
    # разрешить весь доступ к указанному файлу
    def access_full(self, name):
        # определить имя файла
        file_name = join(dirname(__file__), str(name))
        # определяем текущие права файла
        permissions = os.stat(file_name).st_mode
        # test out console
        print(permissions)
        # Convert a file's mode to a string of the form '-rwxrwxrwx'
        permissions = stat.filemode(permissions)
        # test out console
        print(permissions)
        # задаем новые права доступа к файлу
        new_permissions = stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO
        chmod(file_name, new_permissions)
        # test out console
        permissions = os.stat(file_name).st_mode
        permissions = stat.filemode(permissions)
        print(permissions)
    # ---------------------------------------------------------------------------
    # запретить весь доступ к указанному файлу
    def access_not_full(self, name):
        # определить имя файла
        file_name = join(dirname(__file__), str(name))
        # задаем новые права доступа к файлу
        new_permissions = stat.S_ENFMT
        chmod(file_name, new_permissions)
    # ---------------------------------------------------------------------------
    # закрыть доступ к base.apk
    def close_base_apk(self):
        try:
            self.show_prog_base()
            self.access_not_full(self.path_base_apk)
            self.ids.label_main.text = 'ДОСТУП К base.apk ЗАКРЫТ'
        except BaseException as e:
            self.ids.label_main.text = 'НЕТ ДОСТУПА: ' + str(e)
        except JavaException as e:
            self.ids.label_main.text = 'НЕТ ДОСТУПА: ' + str(e)
    # ---------------------------------------------------------------------------
    # открыть доступ к base.apk
    def open_base_apk(self):
        try:
            self.show_prog_base()
            self.access_full(self.path_base_apk)
            self.ids.label_main.text = 'ДОСТУП К base.apk ОТКРЫТ'
        except BaseException as e:
            self.ids.label_main.text = 'НЕТ ДОСТУПА: ' + str(e)
        except JavaException as e:
            self.ids.label_main.text = 'НЕТ ДОСТУПА: ' + str(e)
    # ---------------------------------------------------------------------------
    # Returns an array of strings naming the private files associated 
    # with this Context's application package.
    # Возвращает массив строк, именующих личные файлы, 
    # связанные с пакетом приложений этого контекста.
    def show_file_list(self):
        try:
            self.ids.label_main.text = '\n'.join(Context.fileList())
        except BaseException as e:
            self.ids.label_main.text = 'ОШИБКА: ' + str(e)
        except JavaException as e:
            self.ids.label_main.text = 'ОШИБКА: ' + str(e)
    # ---------------------------------------------------------------------------
    # Returns the absolute path to the directory on the filesystem where files 
    # created with openFileOutput(String, int) are stored.
    # Возвращает абсолютный путь к каталогу в файловой системе, в котором 
    # хранятся файлы, созданные с помощью openFileOutput(String, int).
    def show_files_dir(self):
        try:
            self.ids.label_main.text = str(Context.getFilesDir().getAbsolutePath())
        except BaseException as e:
            self.ids.label_main.text = 'ОШИБКА: ' + str(e)
        except JavaException as e:
            self.ids.label_main.text = 'ОШИБКА: ' + str(e)
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