# *****************************************************************************************
# главное окно программы
from kivy.app import App
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# кнопка
# from kivy.uix.button import Button
# импортируем молуль os.path
# dirname - определяем текущую директорию
# join - объеденяем директорию + файл (правильный путь файла)
from os.path import join, dirname
# импорт модуля Строитель - загружает .kv файлы в проект
from kivy.lang import Builder
Builder.load_file(join(dirname(__file__), 'main.kv'))
# импортируем молуль os
# listdir - файлы в текущей директории
import os
from os import listdir
# импортируем молуль stat (работа с разрешениями прав доступа файлов и папок)
import stat
# импорт моей библиотеки по работе с файлами
from File import File as f
# *****************************************************************************************
class Main(BoxLayout):
    # ---------------------------------------------------------------------------
    '''Root Widget'''
    # ---------------------------------------------------------------------------
    # получить все файлы в текущей директории
    # отсортировано по возрастанию
    def __get_files_dir(self):
        # получаем все файлы и папки в текущей директории и сортируем
        files_arr = sorted(listdir())
        return files_arr
    # ---------------------------------------------------------------------------
    # показать все файлы в текущей директории
    # отсортировано по возрастанию
    def show_files_dir(self):
        # хранение информации о файлах и папках
        output_str = '\n'.join(self.__get_files_dir())
        # вывод информации о файлах и папках
        self.ids.label_main_file.text = output_str
    # ---------------------------------------------------------------------------
    # показать все установленные права доступа файлов в текущей директории
    # в виде str (rwx)
    # отсортировано по возрастанию
    def show_files_dir_access_str(self):
        # массив установленных разрешений для файлов и папок
        access_arr = list()
        # заполняем массив установленныз разрешений для файлов и папок
        for file in self.__get_files_dir():
            # Определим установленные разрешения в виде букв -rwx
            access_arr.append(stat.filemode(os.stat(file).st_mode))
        # хранение информации об установленных разрешений для файлов и папок
        output_str = '\n'.join(access_arr)
        # вывод информации об установленных разрешений для файлов и папок
        self.ids.label_main_file_access_str.text = output_str
    # ---------------------------------------------------------------------------
    # показать все файлы в текущей директории с установленными разрешениями
    # отсортировано по возрастанию
    def show_files_dir_all_option(self):
        # константы
        # величина выравнивания
        delta = int(10)

        # получаем все файлы и папки в текущей директории и сортируем
        # self.ids.text_input_main.text = '\n'.join(listdir())
        files_arr = sorted(listdir())

        # выравниваем текст в files_arr_ljust
        files_arr_ljust = list()
        for i in files_arr:
            files_arr_ljust.append(i.ljust(delta, ' '))

        # массив установленныз разрешений для файлов и папок
        access_arr = list()
        # заполняем массив установленных разрешений для файлов и папок
        for i in files_arr:
            # Определим установленные разрешения в виде константных чисел
            # access_arr.append(stat.S_IMODE(os.stat(i).st_mode))
            # Определим установленные разрешения в виде букв -rwx
            # access_arr.append(stat.filemode(os.stat(i).st_mode))
            # Определим установленные разрешения в виде букв -rwx и константных чисел
            access_arr.append(stat.filemode(os.stat(i).st_mode).ljust(delta, ' ') +
                                # ' '.ljust(delta, ' ') +
                                # ' ' +
                                str(stat.S_IMODE(os.stat(i).st_mode)).ljust(delta, ' '))

        # Определим установленные разрешения
        # existing_permissions = stat.S_IMODE(os.stat(files_arr[0]).st_mode)
        # existing_permissions = dict(zip(files_arr, access_arr))
        existing_permissions = dict(zip(files_arr_ljust, access_arr))

        # хранение информации о файлах и папках
        output_str = str()
        # заполнеяем хранение информации о файлах и папках
        for k, v in existing_permissions.items():
            # output_str += f'{k} : {v}\n'
            output_str += f'{k}{v}\n'

        # вывод информации о файлах и папках
        # self.ids.text_input_main.text = '\n'.join(files_arr)
        # self.ids.text_input_main.text = str(existing_permissions)
        self.ids.text_input_main.text = str(output_str)  
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# окно программы
class AccessApp(App):
    # ---------------------------------------------------------------------------
    '''App Widget'''
    # ---------------------------------------------------------------------------
    def build(self):
        self.title = 'Файловая система'
        return Main()
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    AccessApp().run()
# *****************************************************************************************