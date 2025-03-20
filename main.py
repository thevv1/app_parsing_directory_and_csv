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