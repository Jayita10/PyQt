"""Form Layout"""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("QFormLayout")

layout = QFormLayout()
layout.addRow("Name:", QLineEdit())
layout.addRow("Mail:", QLineEdit())
window.setLayout(layout)

window.show()
sys.exit(app.exec())