from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout

# Информационная справка со сведениями
class HelpDialog(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.setWindowTitle('Информационная справка')
        self.resize(510,220)
        description = QLabel(
            'АС УЗСВ управляет площадками и правами VPN.\n'
            'Стендовый режим использует API виртуальной машины.\n'
            'В демонстрационной режиме используется иллюстрационные данные.\n'
            'Автор: Петроградский Вячеслав Максимович - 70205782.'
        )
        description.setWordWrap(True)
        close = QPushButton('Закрыть')
        close.clicked.connect(self.accept)
        layout = QVBoxLayout(self)
        layout.addWidget(description)
        layout.addWidget(close)