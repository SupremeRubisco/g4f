import subprocess
import sys

def install(name):
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'g4f'])
  

from g4f.gui import run_gui
run_gui()