import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_Form
import logging
import os
import time

os.makedirs("Logs", exist_ok=True)

current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

logging.basicConfig(level=logging.INFO,
                    filename=f"Logs/{current_time}.log",
                    format='%(asctime)s - %(message)s')

app = QApplication(sys.argv)
ui = Ui_Form()
ui.setupUi()
ui.show()

sys.exit(app.exec_())
