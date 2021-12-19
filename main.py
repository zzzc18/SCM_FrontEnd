import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_Form

app = QApplication(sys.argv)
# window = QMainWindow()
ui = Ui_Form()
ui.setupUi()
ui.show()

# window.show()
sys.exit(app.exec_())
