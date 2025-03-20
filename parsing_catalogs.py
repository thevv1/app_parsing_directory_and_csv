
from tkinter import filedialog
import os
import pandas as pd

def browse_folder1():

  global folder_path
  folder_path = filedialog.askdirectory()
  print(f"Выбрана папка: {folder_path}")

def browse_folder():
    # Открываем диалоговое окно для выбора папки
    global folder_path
    folder_path = filedialog.askdirectory()
    print(f"Выбрана папка: {folder_path}")

    # Проверяем, выбрана ли папка
    if folder_path:
        print("Содержимое папки:")
        show_folder_contents(folder_path)

        # Передаем путь к папке в функцию pars
        passes = pars(folder_path)

        # Обрабатываем найденные файлы
        data = reading_file(passes)
        print("Данные успешно обработаны:", data)


def show_folder_contents(path):
    # Получаем список всех файлов и подпапок
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            print(f"Файл: {filename}")
        elif os.path.isdir(file_path):
            print(f"Папка: {filename}")


def pars(folder_path):
    passes = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            root_filename = os.path.join(root, filename)
            if "parcel" not in root_filename:
                passes.append(root_filename)
    return passes


def reading_file(passes):
    data_dict = {}
    for file_path in passes:
        if ".tsv" in file_path:
            try:
                df = pd.read_csv(file_path, sep='\t', skiprows=[0, 2, 3, 4, 5])
                if 'tpm_unstranded' not in df.columns:
                    raise ValueError(f"Столбец 'tpm_unstranded' отсутствует в файле {file_path}")
                series = pd.to_numeric(df['tpm_unstranded'], errors='coerce')
                data_dict[file_path] = series
            except Exception as e:
                print(f"Ошибка при обработке файла {file_path}: {e}")
    return data_dict

