# Fichier: view.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QGridLayout, QLabel
from PyQt5.QtCore import QResource, Qt
import os

class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.create_UI()
        self.style_UI()

    def create_UI(self):
        self.create_elements()
        self.create_layout()
        self.create_central_widget()

    def style_UI(self):
        css_data = QResource(":/style.css").data()
        self.setStyleSheet(css_data.decode())
    
    def create_elements(self):
        self.setWindowTitle("Photo picker")
        self.setGeometry(200,200,960,600)
        self.title = QLabel("Que veux-tu voir ?")
        self.title.setAlignment(Qt.AlignHCenter)
        self.button_ronnie = QPushButton("Ronnie")
        self.button_thailand = QPushButton("Thailande")
        self.button_cambodia = QPushButton("Cambodge")
        self.image_label = QLabel()
        self.image_label.setMinimumSize(1200, 900)  # Définir une taille minimale pour le QLabel de l'image

    def create_layout(self):
        #Layout part
        # Configuration du layout vertical pour le titre
        self.title_layout = QVBoxLayout()
        self.title_layout.addWidget(self.title)

        # Configuration du layout horizontal pour les boutons
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.button_ronnie)
        self.button_layout.addWidget(self.button_thailand)
        self.button_layout.addWidget(self.button_cambodia)

        # Configuration du layout total = les 2 layouts  + l'image
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.image_label)

    def create_central_widget(self):
        # Création du widget central et application du layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
