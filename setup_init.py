import os
import zipfile
import tkinter
import tkinter.messagebox
from tkinter import *
import sys
import shutil
from zipfile import ZipFile
#EXE NAME RETRIEVER
try:
    with open('C:\\Users\\{0}\\OneDrive\\Documents\\exe_name'.format(os.environ['USERNAME']), 'r')as file_name:
        exe_name = file_name.readlines()
        print(exe_name)
        file_name.close()
except FileNotFoundError:
    main = Tk()
    tkinter.messagebox.showerror('Could not find the name file', 'The file: exe_name, could not be found. Please run the setup file again and do not delete it or move it from the documents folder.')
    sys.exit()
_exe_name = str(exe_name)
fexe_name = _exe_name[2:-2]
zipPath = 'C:\\Users\\{0}\\OneDrive\\Desktop\\{1}.zip'.format(os.environ['USERNAME'], fexe_name)

def zip_trans(path):
    with ZipFile('C:\\Users\\{0}\\OneDrive\\Desktop\\{1}.zip'.format(os.environ['USERNAME'], fexe_name), 'w')as zw:
        zw.write(path)
        zw.close()

print('Checkpoint')
with ZipFile('C:\\Users\\{0}\\OneDrive\\Desktop\\{1}.zip'.format(os.environ['USERNAME'], fexe_name), 'w')as zr:
    zr.close()
zip_trans('C:\\Users\\{0}\\OneDrive\\Documents\\exe_name'.format(os.environ['USERNAME']))

