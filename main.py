import shutil
from pathlib import Path

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog

Gui = Path(__file__).with_name("file_sorter.ui")

app = QApplication([])
ui = uic.loadUi(Gui)  # build the window from the .ui file


def pick_folder():
    ui.sourceEdit.setText(QFileDialog.getExistingDirectory())


def pick_final():
    ui.destEdit.setText(QFileDialog.getExistingDirectory())


def copy_files():
    source = Path(ui.sourceEdit.text())
    dest = Path(ui.destEdit.text())

    # ".jpg, .png" -> [".jpg", ".png"]
    file_types = ui.typesEdit.text().lower().replace(" ", "").split(",")

    dest.mkdir(exist_ok=True)
    ui.logList.clear()

    for file in source.iterdir():  
        if file.suffix.lower() in file_types:  
            shutil.copy2(file, dest / file.name)  
            ui.logList.addItem("Copied " + file.name)

    ui.logList.addItem("Done!")


ui.sourceButton.clicked.connect(pick_folder)
ui.destButton.clicked.connect(pick_final)
ui.copyButton.clicked.connect(copy_files)

ui.show()
app.exec()
