
# Fichier: controller.py

from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtCore import Qt, QResource, QByteArray

class Controller:
    def __init__(self, model, view):
        #print("Controller.__init__")
        #print(model)
        self.model = model
        self.view = view
        #self.connect_signals_with_data()
        self.connect_signals_with_list()

    def connect_signals_with_list(self):
        print("Controller.connect_signals_with_list")
        self.view.button_ronnie.clicked.connect(lambda: self.display_random_image_from_list('Ronnie'))
        self.view.button_thailand.clicked.connect(lambda: self.display_random_image_from_list('Thailande'))
        self.view.button_cambodia.clicked.connect(lambda: self.display_random_image_from_list('Cambodge'))
    
    def display_random_image_from_list(self, button_id):
        #print("ici")
        image_path = self.model.get_random_image_from_list(button_id)
        if image_path:
            self.set_image_from_path(image_path)
        else:
            self.clear_image()

    def set_image_from_path(self, image_path):
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(self.view.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.view.image_label.setPixmap(scaled_pixmap)
        self.view.image_label.setAlignment(Qt.AlignCenter)
        # Redimensionner la taille de la fenêtre en fonction de l'image
        self.view.adjustSize()

    #############################################################################
    #Data part
    #############################################################################

    def connect_signals_with_data(self):
        self.view.button_ronnie.clicked.connect(lambda: self.display_random_image_from_data('Ronnie'))
        self.view.button_thailand.clicked.connect(lambda: self.display_random_image_from_data('Thailande'))
        self.view.button_cambodia.clicked.connect(lambda: self.display_random_image_from_data('Cambodge'))

    def display_random_image_from_data(self, image_directory):
        random_image_file = self.model.get_random_image_from_data(image_directory)
        random_image_path = f"{image_directory}/{random_image_file}"  # Chemin complet de l'image
        random_image_data = self.model.load_images_with_data(random_image_path)
        self.set_image_from_data(random_image_data)

    def set_image_from_data(self, image_data):
        image = QImage.fromData(image_data)
        pixmap = QPixmap.fromImage(image)
        scaled_pixmap = pixmap.scaled(self.view.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.view.image_label.setPixmap(scaled_pixmap)
        self.view.image_label.setAlignment(Qt.AlignCenter)
        # Redimensionner la taille de la fenêtre en fonction de l'image
        self.view.adjustSize()

    def clear_image(self):
        self.view.image_label.clear()