from PySide6.QtWidgets import (
    QDialog, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
)

from UZSV.login import LoginDialog
class Shell(QMainWindow):
    # Размещение в главном окне элементов навигации и строки состояния
    def __init__(self):
        super().__init__()
        self.setWindowTitle('АС УЗСВ')
        self.resize(840, 520)
        central = QWidget()
        layout = QVBoxLayout(central)
        layout.addWidget(QLabel('Управление защищенным сетевым взаимодействием'))
        self.state = QLabel('Стенд не подключен')
        layout.addWidget(self.state)
        enter = QPushButton('Вход')
        enter.clicked.connect(self.open_login)
        layout.addWidget(enter)
        layout.addStretch()
        self.setCentralWidget(central)

    def open_panel(self):
        # Модальный диалог показывает панель поверх главного окна
        window = QDialog(self)
        window.setWindowTitle('Панель управления')
        layout = QVBoxLayout(window)
        layout.addWidget(QLabel('Подготовка подключения к стенду'))
        window.exec()

    # Обработчик получает результат формы после закрытия диалога
    def open_login(self):
        login = LoginDialog(self)
        if login.exec() == QDialog.DialogCode.Accepted:
            self.state.setText('Форма завершена. Сервер будет подключен в скором времени.')