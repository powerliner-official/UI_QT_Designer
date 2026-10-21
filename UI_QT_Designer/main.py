import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

app = QApplication(sys.argv)

loader = QUiLoader()
ui_file = QFile("main_window.ui")

if not ui_file.open(QIODevice.OpenModeFlag.ReadOnly):
    print("Error: Cannot open main_window.ui")
    sys.exit(1)

window = loader.load(ui_file)
ui_file.close()

if window is None:
    print("Error: Failed to load UI file")
    sys.exit(1)


def calculate_age():
    try:
        # اگر Input_Age از نوع QTextEdit است:
        age_text = window.input_age.toPlainText().strip()

        # اگر از نوع QLineEdit است، خط بالا را با این خط جایگزین کن:
        # age_text = window.Input_Age.text().strip()

        age = int(age_text)

        if age < 0:
            window.Label.setText("Age cannot be negative")
        elif age < 18:
            window.Label.setText("You are under 18")
        elif age < 65:
            window.Label.setText("You are an adult")
        else:
            window.Label.setText("You are a senior")

    except ValueError:
        window.Label.setText("Please enter a valid number")


window.pushButton.clicked.connect(calculate_age)

window.show()
sys.exit(app.exec())