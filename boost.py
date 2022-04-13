import os
from shutil import rmtree as OptimizePC
import pathlib
# Windows 10 Optimizer
'''
Automatically computer optimizer
'''

TMP_Folder = f"{pathlib.Path.home()}\\AppData\\Local\\Temp"
ez = os.path

if ez.exists(TMP_Folder):
    OptimizePC(f"{TMP_Folder}", ignore_errors=True) # Ignoring errors like 'This file is in use and removes the files which are not in use'
    exit(0)
else:
    exit(1)
