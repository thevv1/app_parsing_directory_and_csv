import tk

file = r'SARC'
from parsing_catalogs import *
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
'''passes = pars(file)
data_dict = reading_file(passes)
print(data_dict)
print(passes)'''



root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)

button.pack()

root.mainloop()



#endregion
