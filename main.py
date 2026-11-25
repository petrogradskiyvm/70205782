import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("АС УЗСВ")
    window.resize(500, 300)
    window.setCentralWidget(QLabel('Управление защищенным сетевым взаимодействием'))
    window.show()
    return app.exec()

if __name__ == '__main__':
    raise SystemExit(main())