import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

# create the basic application GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
hellomsg = QLabel("<h1>Hello World!</h1>", parent=window)
hellomsg.move(60, 15)

window.show()
sys.exit(app.exec())