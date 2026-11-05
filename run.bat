@echo off
python -m pip install -r "%~dp0requirements.txt"
python "%~dp0main.py"
