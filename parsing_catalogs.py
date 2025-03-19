import tkinter
from doctest import master
from idlelib.searchengine import get_selection

import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog


def cancel_command(event):
    pass


def UploadAction(event=None):
    filename = filedialog.Directory(master=None)
    filedialog.FileDialog(master, title=None)
    cancel_command(event=None)
    print('Selected:', filename)


def pars(file_path):
    passes = []
    for root, dirs, files in os.walk(file_path):
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


'''final_df = pd.DataFrame(data_dict)
data_dict[file_path]'''
