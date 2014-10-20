from distutils.core import setup
import py2exe
from glob import glob
import sys
import os

sys.path.append("C:\\Users\\USER\\Desktop\\Microsoft.VC90.CRT")


data_files = [("Microsoft.VC90.CRT", glob("C:\\Users\\USER\\Desktop\\Microsoft.VC90.CRT"))]

setup(
    name="3-D Street View",version="1.1",
    options = {         
    'py2exe' : {
        'compressed': 1, 
        'optimize': 2,
        'bundle_files': 3, #Options 1 & 2 do not work on a 64bit system
        'dist_dir': 'dist',  # Put .exe in dist/
        'xref': False,
        'skip_archive': False,
        'ascii': False,
        }
        },                   
  zipfile=None, 
  console = [r'C:\\3d-Model\\bin\\Application.py'],
)
