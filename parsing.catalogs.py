import pandas as pd
import numpy as np
import os
from posixpath import join
!unzip '/content/drive/MyDrive/sar.c/SARC.zip'
passes = []
for root,dirs,files in os.walk('/content/SARC'):
  for filename in files:
    root_filename = os.path.join(root,filename)
    if "parcel" not in root_filename :
      passes.append(root_filename)

data_dict = {}

for file_path in passes:
    try:
        df = pd.read_csv(file_path, sep='\t', skiprows=[0,2,3,4,5])
        if 'tpm_unstranded' not in df.columns:
            raise ValueError(f"Столбец 'tpm_unstranded' отсутствует в файле {file_path}")
        series = pd.to_numeric(df['tpm_unstranded'], errors='coerce')
        data_dict[file_path] = series
    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {e}")
final_df = pd.DataFrame(data_dict)
data_dict[file_path]