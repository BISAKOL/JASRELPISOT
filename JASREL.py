import os
import sys 
import importlib

os.system("git pull")

try:
    importlib.import_module("jasrel").menu() 
except Exception as e: 
    exit(str(e))
