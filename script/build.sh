#!/bin/sh
pyinstaller --onefile --paths unminipy-env/lib/python3.11/site-packages --hidden-import pyperclip -n unminipy unmini.py
