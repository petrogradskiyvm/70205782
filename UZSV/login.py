from PySide6.QtWidgets import (
    QDialog, QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
)

# Диалог готовит данные учетных записей для передачи
class LoginDialog(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.setWindowTitle("Вход")
        self.username = QLineEdit()
        self.username.setMaxLength(40)
        self.password = QLineEdit()
        self.password.setMaxLength(30)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.message = QLabel()
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
        )
        buttons.button(QDialogButtonBox.StandardButton.Ok).setText('Войти')
        buttons.button(QDialogButtonBox.StandardButton.Cancel).setText('Отмена')
        buttons.accepted.connect(self.check_input)
        buttons.rejected.connect(self.reject)
        form = QFormLayout(self)
        form.addRow('Логин', self.username)
        form.addRow('Пароль', self.password)
        form.addRow(self.message)
        form.addRow(buttons)

    # Пустые поля оставляют диалог открытым
    def check_input(self):
        if not self.username.text().strip() or not self.password.text():
            self.message.setText('Заполните все поля.')
            return
        self.accept()