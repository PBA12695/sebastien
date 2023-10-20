# Fichier: main.py
import sys
from PyQt5.QtWidgets import QApplication
from controller import Controller
from view import View
from model import Model
from resource_rc import *

if __name__ == "__main__":
    #print("hello")
    app = QApplication(sys.argv)
    model = Model()
    view = View()
    controller = Controller(model, view)
    
    view.show()
    sys.exit(app.exec_())