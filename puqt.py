import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt Example")

layout = QVBoxLayout()
label = QLabel("Hello, PyQt!")
layout.addWidget(label)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
