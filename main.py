import sys
from PySide6.QtWidgets import QApplication
from UZSV.desktop import Shell

# Точка входа сохраняет оболочку и цикл Qt отдельно от кода окон
def main():
    app = QApplication(sys.argv)
    window = Shell()
    window.show()
    return app.exec()

if __name__ == "__main__":
    raise SystemExit(main())