from PySide6.QtWidgets import (QWidget, QVBoxLayout, QGridLayout,
                               QPushButton, QLineEdit, QApplication)
from PySide6.QtCore import Qt
import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora")
        self.setGeometry(300, 300, 300, 400)

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("font-size: 20px;")
        vbox.addWidget(self.display)

        # Buttons
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '(',
            '1', '2', '3', '-', ')',
            '0', '.', '=', '+'
        ]

        grid = QGridLayout()
        for i, btn_text in enumerate(buttons):
            button = QPushButton(btn_text)
            button.setStyleSheet("font-size: 30px;")
            button.clicked.connect(self.on_button_click)
            grid.addWidget(button, i // 5, i % 5)

        vbox.addLayout(grid)
        self.setLayout(vbox)

    def on_button_click(self):
        button = self.sender()
        key = button.text()

        if key == 'C':
            self.display.clear()
        elif key == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
