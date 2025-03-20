from parsing_catalogs import *
import tkinter as tk
from tkinter import filedialog
import os
import json
import pandas as pd

folder_path = filedialog.askdirectory()
print(f"Выбрана папка: {folder_path}")
passes = pars(folder_path)
data_dict = reading_file(passes)
print(data_dict)
print(passes)
for key in data_dict:
  data_dict[key] = data_dict[key].tolist()

json_data = {
  "passes": passes,
  "data": data_dict
  }


with open('result.json', 'w', encoding='utf-8') as json_file:
  json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print("Данные успешно сохранены в result.json")


root = tk.Tk()
root.title("Менеджер папок")

browse_button = tk.Button(
  root,
  text="Выбрать папку",
  command=browse_folder,
  font=("Arial", 12),
  padx=10,
  pady=5
)
browse_button.pack(pady=20)

root.mainloop()
'''
folder_path:Эта переменная хранит путь к выбранной папке. Она заполняется после вызова метода filedialog.askdirectory(), 
который отображает диалоговое окно для выбора каталога. Позже этот путь передается другим функциям для обработки файлов в этой папке.

passes:Переменная содержит список путей к файлам, которые были найдены функцией pars(folder_path). 
Это файлы, подходящие для дальнейшей обработки (например, с определенным расширением или без строки "parcel" в названии).

data_dict:Словарь, содержащий данные, полученные из файлов. Ключи этого словаря — это пути к файлам, а значения 
— серии данных, извлечённые из столбца tpm_unstranded (если такой столбец существует в файле). 
Данные представлены в виде списка чисел.

key (в цикле for key in data_dict:):Временная переменная цикла, которая принимает значения ключей словаря data_dict. 
Используется для перебора всех элементов словаря.

json_data:Объект JSON, представляющий собой структуру данных, состоящую из двух полей:

"passes": содержит список путей к файлам, найденным в выбранной папке.

"data": содержит данные, прочитанные из файлов (значения столбца tpm_unstranded).
json_file:Указатель на открытый файл result.json, куда сохраняется информация из 
переменной json_data в формате JSON. Этот файл открывается для записи с помощью конструкции open('result.json', 'w', ...).

root:Экземпляр класса Tk из модуля tkinter, который представляет основное окно 

GUI-приложения. Это корневой объект приложения, от которого зависят все остальные виджеты интерфейса.

browse_button:Виджет кнопки, который создается для основного окна приложения. 

Кнопка привязана к команде command=browse_folder, вызывающей соответствующую функцию для выбора папки. 
Параметры стиля кнопки (шрифт, отступы) настраиваются прямо при создании.

'''