# File Sorter

A small app that copies files of certain types (like `.jpg` or `.png`) from one folder to another.

## How to use it on another computer

1. Install Python from https://www.python.org/downloads/. On the first installer screen, tick **"Add python.exe to PATH"**.
2. On this GitHub page, click the green **Code** button, then **Download ZIP**, and unzip it.
3. Double-click **run.bat**. The first time, it installs PyQt5 (this needs internet), then opens the app.

## How to use the app

1. Click **Browse…** next to "Copy from" and pick the folder with your files.
2. Click **Browse…** next to "Copy to" and pick where the copies should go.
3. Type the file types you want, separated by commas, for example `.jpg, .png, .pdf`.
4. Click **Copy Files**.

## Files

- `main.py`: the program.
- `file_sorter.ui`: the window layout. Open it with Qt Designer to change how it looks.
- `requirements.txt`: the Python packages the app needs (just PyQt5).
- `run.bat`: installs PyQt5 and starts the app on Windows.
