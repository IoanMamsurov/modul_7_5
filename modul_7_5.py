import os
import time
a = os.getcwd()
for i in os.walk('.'):
    print(i)


for root, dirs, files in os.walk(a):
    for file in files:
        filepath = os.path.join(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.abspath(file)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
          f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

