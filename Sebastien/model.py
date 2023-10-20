# Fichier: model.py
import os
import random
from PyQt5.QtCore import QObject, QResource

class Model(QObject):
    def __init__(self):
        #print("Model.__init__")
        super().__init__()
        self.button_ronnie_images = []
        self.button_thailand_images = []
        self.button_cambodia_images = []
        self.load_images_with_list()
        #print(self)

    def load_images_with_list(self):
        #self.button_ronnie_images = self.load_images_from_directory("C:/Users/SHO23421/Desktop/Photos/Ronnie")
        #self.button_thailand_images = self.load_images_from_directory("C:/Users/SHO23421/Desktop/Photos/Thailande")
        #self.button_cambodia_images = self.load_images_from_directory("C:/Users/SHO23421/Desktop/Photos/Cambodge")
        self.button_ronnie_images = self.load_images_from_directory("Photos\Ronnie")
        self.button_thailand_images = self.load_images_from_directory("Photos/Thailande")
        self.button_cambodia_images = self.load_images_from_directory("Photos/Cambodge")
        print(self.button_ronnie_images)

    def load_images_from_directory(self, directory):
        print(" ")
        images = []
        if os.path.exists(directory) and os.path.isdir(directory):
            #print("directory = " + directory)
            image_files = [file for file in os.listdir(directory) if file.endswith(".jpg") or file.endswith(".png")]
            for file in image_files:
                #print("New file = " + file)
                image_path = os.path.join(directory, file)
                images.append(image_path)
        else:
            print("Error path does not exist")
        #print(images)
        return images

    def load_images_with_data(self, image_path):
        resource_path = f":/images/{image_path}"
        resource = QResource(resource_path)
        image_data = resource.data()
        return image_data
    
    def get_random_image_from_list(self, button_id):
        if button_id == 'Ronnie':
            print(self.button_ronnie_images)
            return random.choice(self.button_ronnie_images)
        elif button_id == 'Thailande':
            print(self.button_thailand_images)
            return random.choice(self.button_thailand_images)
        elif button_id == 'Cambodge':
            print(self.button_cambodia_images)
            return random.choice(self.button_cambodia_images)
        else:
            return None

    def get_random_image_from_data(self, button_id):
        if button_id == 'Ronnie':
            image_files = [f"image{i}.jpg" for i in range(1, 28)]
            return random.choice(image_files)
        elif button_id == 'Thailande':
            image_files = [f"image{i}.jpg" for i in range(1, 23)]
            return random.choice(image_files)
        elif button_id == 'Cambodge':
            image_files = [f"image{i}.jpg" for i in range(1, 20)]
            return random.choice(image_files)
        else:
            return None