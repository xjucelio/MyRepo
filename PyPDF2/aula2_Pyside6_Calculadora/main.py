import sys

from main_window import MainWindow
from info import Info
from button import ButtonsGrid
from display import Display
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # snake_case
    # PascalCase
    # camelCase

    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # label1 = QLabel('O meu texto')
    # label1.setStyleSheet('font-size: 150px;'){}
    # window.vLayout.addWidget(label1)4
    # window.adjustFixedSize()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('sua conta')
    window.addWidgetToVLayout(info)

    # display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # button
    # buttonsGrid.addWidget(Button('0'), 0, 0)
    # buttonsGrid.addWidget(Button('1'), 0, 1)
    # buttonsGrid.addWidget(Button('2'), 0, 2)

    # buttonsGrid.addWidget(Button('3'), 1, 1, 1, 2)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
